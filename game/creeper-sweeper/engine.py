#!/usr/bin/env python3
"""Creeper Sweeper — an issue-driven Minesweeper that lives inside a GitHub profile README.

Anyone can play by opening an issue whose title is a command:

    cs|reveal|<row>|<col>     dig a block
    cs|flag|<row>|<col>       plant / remove a flag
    cs|mode|flag              switch every board link to flag mode
    cs|mode|reveal            switch back to digging
    cs|new                    start a fresh board

A GitHub Action runs this script, which mutates state.json, re-renders the board
into README.md between the CS:BOARD markers, and prints a reply for the issue.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "state.json"
REPO_ROOT = HERE.parent.parent
README_PATH = REPO_ROOT / "README.md"

BOARD_START = "<!-- CS:BOARD:START -->"
BOARD_END = "<!-- CS:BOARD:END -->"

WIDTH, HEIGHT, MINES = 8, 8, 10
COLS = "ABCDEFGH"

HIDDEN = "⬛"
EMPTY = "⬜"
FLAG = "🚩"
CREEPER = "🟩"
BOOM = "💥"
DEFUSED = "💚"
NUMBERS = ["⬜", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]

ROW_LABELS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
COL_LABELS = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭"]


# --------------------------------------------------------------------------- state


def new_state() -> dict:
    return {
        "w": WIDTH,
        "h": HEIGHT,
        "mines": MINES,
        "mines_placed": False,
        "board": [[0] * WIDTH for _ in range(HEIGHT)],
        "revealed": [[False] * WIDTH for _ in range(HEIGHT)],
        "flags": [[False] * WIDTH for _ in range(HEIGHT)],
        "status": "playing",
        "mode": "reveal",
        "moves": 0,
        "exploded": None,
        "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scoreboard": {"wins": 0, "losses": 0, "games": 1},
        "log": [],
    }


def load_state() -> dict:
    if not STATE_PATH.exists():
        return new_state()
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return new_state()
    # A malformed or hand-edited file should never wedge the game.
    for key in ("board", "revealed", "flags"):
        grid = state.get(key)
        if not isinstance(grid, list) or len(grid) != HEIGHT or any(len(row) != WIDTH for row in grid):
            return new_state()
    return state


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def reset_board(state: dict) -> dict:
    scoreboard = state.get("scoreboard", {"wins": 0, "losses": 0, "games": 0})
    log = state.get("log", [])
    fresh = new_state()
    scoreboard["games"] = scoreboard.get("games", 0) + 1
    fresh["scoreboard"] = scoreboard
    fresh["log"] = log
    return fresh


# --------------------------------------------------------------------------- rules


def neighbours(state: dict, r: int, c: int):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < state["h"] and 0 <= nc < state["w"]:
                yield nr, nc


def place_mines(state: dict, safe_r: int, safe_c: int) -> None:
    """Mines are placed on the first dig so the opening move can never explode."""
    forbidden = {(safe_r, safe_c)} | set(neighbours(state, safe_r, safe_c))
    cells = [
        (r, c)
        for r in range(state["h"])
        for c in range(state["w"])
        if (r, c) not in forbidden
    ]
    for r, c in random.sample(cells, state["mines"]):
        state["board"][r][c] = -1

    for r in range(state["h"]):
        for c in range(state["w"]):
            if state["board"][r][c] == -1:
                continue
            state["board"][r][c] = sum(
                1 for nr, nc in neighbours(state, r, c) if state["board"][nr][nc] == -1
            )
    state["mines_placed"] = True


def flood_reveal(state: dict, r: int, c: int) -> int:
    """Reveal a cell, cascading through the connected region of zeroes."""
    opened = 0
    stack = [(r, c)]
    seen = set()
    while stack:
        cr, cc = stack.pop()
        if (cr, cc) in seen:
            continue
        seen.add((cr, cc))
        if state["revealed"][cr][cc] or state["flags"][cr][cc]:
            continue
        state["revealed"][cr][cc] = True
        opened += 1
        if state["board"][cr][cc] == 0:
            stack.extend(neighbours(state, cr, cc))
    return opened


def check_win(state: dict) -> bool:
    for r in range(state["h"]):
        for c in range(state["w"]):
            if state["board"][r][c] != -1 and not state["revealed"][r][c]:
                return False
    return True


def flags_used(state: dict) -> int:
    return sum(1 for row in state["flags"] for f in row if f)


# --------------------------------------------------------------------------- moves


def do_reveal(state: dict, r: int, c: int, user: str) -> str:
    if state["status"] != "playing":
        return "That board is already finished — open `cs|new` for a fresh one."
    if state["flags"][r][c]:
        return f"**{COLS[c]}{r + 1}** is flagged. Unflag it first (`cs|flag|{r}|{c}`)."
    if state["revealed"][r][c]:
        return f"**{COLS[c]}{r + 1}** is already dug out. Pick another block."

    if not state["mines_placed"]:
        place_mines(state, r, c)

    state["moves"] += 1

    if state["board"][r][c] == -1:
        state["revealed"][r][c] = True
        state["exploded"] = [r, c]
        state["status"] = "lost"
        state["scoreboard"]["losses"] = state["scoreboard"].get("losses", 0) + 1
        push_log(state, user, f"dug {COLS[c]}{r + 1} — 💥 creeper")
        return f"💥 **Aw man.** {COLS[c]}{r + 1} was a creeper. `@{user}` blew up the board after {state['moves']} moves."

    opened = flood_reveal(state, r, c)
    push_log(state, user, f"dug {COLS[c]}{r + 1} (+{opened})")

    if check_win(state):
        state["status"] = "won"
        state["scoreboard"]["wins"] = state["scoreboard"].get("wins", 0) + 1
        return f"🏆 **Cleared!** `@{user}` dug the last safe block. {state['moves']} moves, zero creepers triggered."

    hint = state["board"][r][c]
    detail = "empty pocket — the cascade opened it up" if hint == 0 else f"**{hint}** creeper(s) touching that block"
    return f"⛏️ `@{user}` dug **{COLS[c]}{r + 1}** — {detail}. {opened} block(s) revealed."


def do_flag(state: dict, r: int, c: int, user: str) -> str:
    if state["status"] != "playing":
        return "That board is already finished — open `cs|new` for a fresh one."
    if state["revealed"][r][c]:
        return f"**{COLS[c]}{r + 1}** is already dug out — nothing to flag."

    state["flags"][r][c] = not state["flags"][r][c]
    state["moves"] += 1
    verb = "planted a flag on" if state["flags"][r][c] else "pulled the flag off"
    push_log(state, user, f"{verb} {COLS[c]}{r + 1}")
    return f"🚩 `@{user}` {verb} **{COLS[c]}{r + 1}**. {state['mines'] - flags_used(state)} flag(s) left."


def push_log(state: dict, user: str, what: str) -> None:
    entry = {
        "user": user,
        "what": what,
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }
    state["log"] = ([entry] + state.get("log", []))[:5]


# --------------------------------------------------------------------------- render


def issue_link(repo: str, title: str) -> str:
    # Kept short on purpose: this string is repeated 64+ times inside the README.
    query = urllib.parse.urlencode({"title": title, "body": "Press Create — a bot plays this move."})
    return f"https://github.com/{repo}/issues/new?{query}"


def cell_markdown(state: dict, repo: str, r: int, c: int) -> str:
    revealed = state["revealed"][r][c]
    flagged = state["flags"][r][c]
    value = state["board"][r][c]
    finished = state["status"] != "playing"

    if revealed:
        if value == -1:
            return BOOM if state.get("exploded") == [r, c] else CREEPER
        return NUMBERS[value]

    if finished:
        # Show where the creepers were hiding once the round is over.
        if value == -1:
            return DEFUSED if state["status"] == "won" else CREEPER
        return FLAG if flagged else HIDDEN

    face = FLAG if flagged else HIDDEN
    if state["mode"] == "reveal" and flagged:
        return face  # protected: unflag before you can dig it
    action = "flag" if state["mode"] == "flag" else "reveal"
    return f"[{face}]({issue_link(repo, f'cs|{action}|{r}|{c}')})"


def render_board(state: dict, repo: str) -> str:
    lines: list[str] = []

    # HTML tags, not markdown asterisks — GitHub does not reliably parse markdown
    # emphasis inside an inline HTML block element.
    if state["status"] == "won":
        banner = "🏆 &nbsp;<b>BOARD CLEARED</b> — every creeper found. Rack a new one below."
    elif state["status"] == "lost":
        banner = "💥 &nbsp;<b>BOOM</b> — a creeper got clicked. Board locked. Rack a new one below."
    else:
        mode_word = "FLAG" if state["mode"] == "flag" else "DIG"
        banner = (
            f"🎮 &nbsp;<b>LIVE</b> &nbsp;·&nbsp; mode <b>{mode_word}</b> &nbsp;·&nbsp; "
            f"🚩 {state['mines'] - flags_used(state)} flags left &nbsp;·&nbsp; "
            f"{state['moves']} moves played"
        )

    lines.append(f"<p align=\"center\">{banner}</p>")
    lines.append("")

    header = "|   | " + " | ".join(COL_LABELS) + " |"
    divider = "|:-:|" + ":-:|" * state["w"]
    lines.append(header)
    lines.append(divider)
    for r in range(state["h"]):
        cells = " | ".join(cell_markdown(state, repo, r, c) for c in range(state["w"]))
        lines.append(f"| {ROW_LABELS[r]} | {cells} |")

    lines.append("")

    # Controls
    if state["status"] == "playing":
        if state["mode"] == "reveal":
            toggle = f"[![flag mode](https://img.shields.io/badge/🚩_switch_to_FLAG_mode-0d1117?style=for-the-badge&labelColor=0d1117&color=22d3ee)]({issue_link(repo, 'cs|mode|flag')})"
        else:
            toggle = f"[![dig mode](https://img.shields.io/badge/⛏️_switch_to_DIG_mode-0d1117?style=for-the-badge&labelColor=0d1117&color=3ddb7d)]({issue_link(repo, 'cs|mode|reveal')})"
    else:
        toggle = ""

    new_game = f"[![new game](https://img.shields.io/badge/🔄_NEW_BOARD-0d1117?style=for-the-badge&labelColor=0d1117&color=3ddb7d)]({issue_link(repo, 'cs|new')})"

    lines.append("<p align=\"center\">")
    lines.append(f"  {toggle}")
    lines.append(f"  {new_game}")
    lines.append("</p>")
    lines.append("")

    board = state["scoreboard"]
    lines.append(
        f"<p align=\"center\"><sub>🏆 {board.get('wins', 0)} cleared &nbsp;·&nbsp; "
        f"💥 {board.get('losses', 0)} exploded &nbsp;·&nbsp; 🎲 board #{board.get('games', 1)}</sub></p>"
    )

    if state.get("log"):
        lines.append("")
        lines.append("<details align=\"center\">")
        lines.append("<summary><sub><b>recent moves</b></sub></summary>")
        lines.append("")
        for entry in state["log"]:
            lines.append(f"- `{entry['at']}` — **@{entry['user']}** {entry['what']}")
        lines.append("")
        lines.append("</details>")

    return "\n".join(lines)


def update_readme(state: dict, repo: str) -> None:
    if not README_PATH.exists():
        return
    readme = README_PATH.read_text(encoding="utf-8")
    if BOARD_START not in readme or BOARD_END not in readme:
        print("::warning::CS board markers missing from README.md, skipping render", file=sys.stderr)
        return
    block = f"{BOARD_START}\n\n{render_board(state, repo)}\n\n{BOARD_END}"
    pattern = re.compile(re.escape(BOARD_START) + r".*?" + re.escape(BOARD_END), re.DOTALL)
    README_PATH.write_text(pattern.sub(lambda _: block, readme, count=1), encoding="utf-8")


# --------------------------------------------------------------------------- entry


def safe_commit_subject(command: str, user: str) -> str:
    """Issue titles and logins are attacker-controlled, so strip them to a known charset.

    The result is written to a file and passed to `git commit -F`, never through a shell.
    """
    move = re.sub(r"[^A-Za-z0-9|_-]", "", command.strip())[:40] or "move"
    who = re.sub(r"[^A-Za-z0-9_-]", "", user)[:39] or "someone"
    return f"game(creeper-sweeper): {move} by @{who}"


def apply_command(state: dict, command: str, user: str) -> tuple[dict, str]:
    parts = [p.strip().lower() for p in command.strip().split("|")]
    if not parts or parts[0] != "cs":
        return state, "That title isn't a Creeper Sweeper command — ignoring."

    verb = parts[1] if len(parts) > 1 else ""

    if verb == "new":
        state = reset_board(state)
        push_log(state, user, "started a fresh board")
        return state, f"🔄 `@{user}` racked a fresh 8×8 board with {MINES} creepers. First dig is always safe."

    if verb == "mode":
        wanted = parts[2] if len(parts) > 2 else ""
        if wanted not in ("flag", "reveal"):
            return state, "Mode must be `flag` or `reveal`."
        state["mode"] = wanted
        label = "🚩 flag mode" if wanted == "flag" else "⛏️ dig mode"
        return state, f"`@{user}` switched the board to **{label}**. Every cell link now does that."

    if verb in ("reveal", "flag"):
        try:
            r, c = int(parts[2]), int(parts[3])
        except (IndexError, ValueError):
            return state, "Coordinates missing. Use `cs|reveal|<row>|<col>` with 0-based numbers."
        if not (0 <= r < state["h"] and 0 <= c < state["w"]):
            return state, f"Out of bounds. Rows and columns both run 0–{state['w'] - 1}."
        if verb == "reveal":
            return state, do_reveal(state, r, c, user)
        return state, do_flag(state, r, c, user)

    return state, "Unknown command. Try `cs|reveal|0|0`, `cs|flag|0|0`, `cs|mode|flag` or `cs|new`."


def main() -> int:
    parser = argparse.ArgumentParser(description="Creeper Sweeper move processor")
    parser.add_argument("--command", required=True, help="issue title, e.g. cs|reveal|3|4")
    parser.add_argument("--user", default="someone", help="GitHub login of the player")
    parser.add_argument("--repo", default="YanIanZ/YanIanZ", help="owner/name used for move links")
    parser.add_argument("--reply-file", default="", help="write the issue reply here")
    parser.add_argument("--commit-file", default="", help="write a shell-safe commit message here")
    parser.add_argument("--render-only", action="store_true", help="re-render the board, play no move")
    args = parser.parse_args()

    state = load_state()

    if args.render_only:
        reply = "Board re-rendered."
    else:
        state, reply = apply_command(state, args.command, args.user)

    save_state(state)
    update_readme(state, args.repo)

    if args.reply_file:
        Path(args.reply_file).write_text(reply + "\n", encoding="utf-8")
    if args.commit_file:
        Path(args.commit_file).write_text(safe_commit_subject(args.command, args.user) + "\n", encoding="utf-8")
    print(reply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
