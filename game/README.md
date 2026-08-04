<div align="center">

# 🕹️ &nbsp;THE ARCADE

**Games that live inside a GitHub profile. No install, no server, no JavaScript.**

</div>

---

## 💣 &nbsp;Creeper Sweeper — `creeper-sweeper/`

Minesweeper (8×8, 10 creepers) played by **anyone with a GitHub account**.

Board state lives in [`creeper-sweeper/state.json`](creeper-sweeper/state.json) and is rendered
into the profile [`README.md`](../README.md) between the `CS:BOARD` markers.

**How a move happens**

1. You click a cell in the README. That's a link to `issues/new` with a pre-filled title like `cs|reveal|3|4`.
2. You press **Create**.
3. [`.github/workflows/creeper-sweeper.yml`](../.github/workflows/creeper-sweeper.yml) fires on `issues: opened`.
4. [`engine.py`](creeper-sweeper/engine.py) validates the move, mutates state, re-renders the board, commits.
5. The bot comments the result on your issue and closes it.

**Commands**

| Title | Effect |
|:--|:--|
| `cs\|reveal\|<row>\|<col>` | Dig a block — 0-based, so rows and cols are `0`–`7` |
| `cs\|flag\|<row>\|<col>` | Plant or remove a flag |
| `cs\|mode\|flag` | Every board link becomes a flag action |
| `cs\|mode\|reveal` | Back to digging |
| `cs\|new` | Rack a fresh board |

**Rules of the implementation**

- **First dig is always safe** — mines are placed *after* the opening click, excluding that cell and its eight neighbours.
- Zeroes cascade; flagged cells cannot be dug until unflagged.
- Anything that isn't a valid command gets a polite reply and changes nothing.
- Issue titles are untrusted input — they never reach a shell. The commit subject is regenerated from a whitelist charset.

Run it locally:

```bash
python3 game/creeper-sweeper/engine.py --command "cs|reveal|0|0" --user you --repo YanIanZ/YanIanZ
```

---

## 🗺️ &nbsp;The Deep Dark Descent — `deep-dark/`

A choose-your-own-adventure built out of nothing but markdown links.
Thirteen rooms, **four endings**, one of them hidden.

**[▶ Start here](deep-dark/start.md)**

| Ending | How you get it |
|:--|:--|
| 💎 The Haul | Get out alive and rich |
| 🖤 Sonic Boom | Make noise near something blind |
| 🕳️ Still Down There | Break your last tool on scenery |
| 📘 ??? | Find the book. Then find what it unlocks. |

---

## 🧠 &nbsp;Block Quiz + 🐍 Snake

Both live directly in the profile [`README.md`](../README.md) — the quiz is `<details>` blocks,
the snake is generated every 12 hours by
[`.github/workflows/snake.yml`](../.github/workflows/snake.yml) and pushed to the `output` branch.

---

<div align="center">
<sub><a href="../README.md">← back to the profile</a></sub>
</div>
