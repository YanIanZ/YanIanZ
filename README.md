<!-- ════════════════════════════════ BANNER ════════════════════════════════ -->
<p align="center">
  <img src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/main/assets/banner.svg" alt="YanIanZ — Minecraft Plugin Engineer" width="100%" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=3DDB7D&center=true&vCenter=true&width=680&lines=Folia-safe+plugins+for+Paper+26.2;Region-threaded%2C+async%2C+zero+main-thread+I%2FO;Panels%2C+proxies+and+the+boring+infra+that+keeps+it+up;Scroll+down+%E2%80%94+there+are+playable+games+in+this+README" alt="what I do" />
</p>

<p align="center">
  <a href="https://sourby.my.id"><img src="https://img.shields.io/badge/sourby.my.id-0d1117?style=flat-square&logo=googlechrome&logoColor=3ddb7d&labelColor=0d1117" alt="website" /></a>
  <img src="https://img.shields.io/badge/Surabaya,_ID-0d1117?style=flat-square&logo=googlemaps&logoColor=22d3ee&labelColor=0d1117" alt="location" />
  <a href="https://github.com/YanIanZ?tab=followers"><img src="https://img.shields.io/github/followers/YanIanZ?style=flat-square&logo=github&logoColor=3ddb7d&label=followers&labelColor=0d1117&color=0d1117" alt="followers" /></a>
  <img src="https://komarev.com/ghpvc/?username=YanIanZ&label=views&style=flat-square&color=0d1117&labelColor=0d1117" alt="views" />
</p>

<br>

<!-- ════════════════════════════════ WHOAMI ════════════════════════════════ -->

## `~/` &nbsp;whoami

I build **Minecraft server software** — plugins, forks and the infrastructure underneath them.
Most of my work lives in the **SourbyCraft** ecosystem: a Folia-based server stack where every
feature has to survive region threading, which is a polite way of saying *nothing is allowed to
touch the main thread and hope for the best*.

```java
public final class YanIanZ extends JavaPlugin {

    @Override
    public void onEnable() {
        stack     = List.of("Java 25", "Paper / Folia", "Mixins", "Go", "PHP", "Bash");
        building  = "SourbyCraft — server core, economy, essentials, anticheat";
        alsoDoing = "KaNeil — game panel, daemon, plugin registry";
        learning  = "JVM tuning, region schedulers, clean plugin architecture";
        openTo    = "Minecraft open-source collaboration";
        fuel      = List.of("coffee", "lo-fi", "3AM commits");
    }

    @Override
    public void onDisable() {
        // never called. the server does not go down.
    }
}
```

<table>
<tr>
<td width="50%" valign="top">

**🔭 &nbsp;Right now**
- Folia-safe plugin suites for **Paper 26.2 / Java 25**
- `Cherry` — unified server-side mixin + AT system
- Panel + daemon work in **Go** and **PHP**

</td>
<td width="50%" valign="top">

**💬 &nbsp;Ask me about**
- Region scheduling & why your task threw *"failed main thread check"*
- Plugin architecture that survives 300 concurrent players
- Self-hosting: nginx, Docker, VPS, game panels

</td>
</tr>
</table>

<br>

<!-- ════════════════════════════════ STACK ════════════════════════════════ -->

## `~/` &nbsp;stack

<table>
<tr>
<td align="center" width="25%"><b>🎮 &nbsp;Minecraft</b></td>
<td align="center" width="25%"><b>⚙️ &nbsp;Languages</b></td>
<td align="center" width="25%"><b>🛠️ &nbsp;Infra</b></td>
<td align="center" width="25%"><b>🗄️ &nbsp;Data</b></td>
</tr>
<tr>
<td align="center"><img src="https://skillicons.dev/icons?i=java,gradle,maven,idea&theme=dark&perline=2" /></td>
<td align="center"><img src="https://skillicons.dev/icons?i=java,kotlin,go,php&theme=dark&perline=2" /></td>
<td align="center"><img src="https://skillicons.dev/icons?i=linux,docker,nginx,bash&theme=dark&perline=2" /></td>
<td align="center"><img src="https://skillicons.dev/icons?i=mysql,redis,sqlite,mongodb&theme=dark&perline=2" /></td>
</tr>
<tr>
<td align="center"><sub>Paper · Folia · Velocity<br>Spigot · Mixins</sub></td>
<td align="center"><sub>Python · JavaScript<br>Shell</sub></td>
<td align="center"><sub>Cloudflare · Vultr<br>AWS · Git</sub></td>
<td align="center"><sub>HikariCP<br>Flat-file / YAML</sub></td>
</tr>
</table>

<br>

<!-- ════════════════════════════════ WORK ════════════════════════════════ -->

## `~/` &nbsp;featured work

<p align="center">
  <a href="https://github.com/YanIanZ/SourbyCraft"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SourbyCraft&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=3ddb7d&icon_color=22d3ee" /></a>
  <a href="https://github.com/YanIanZ/SEssentials"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SEssentials&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=3ddb7d&icon_color=22d3ee" /></a>
</p>
<p align="center">
  <a href="https://github.com/YanIanZ/SourbyEconomy"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SourbyEconomy&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=3ddb7d&icon_color=22d3ee" /></a>
  <a href="https://github.com/YanIanZ/Cherry"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=Cherry&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=3ddb7d&icon_color=22d3ee" /></a>
</p>

<details>
<summary><b>📦 &nbsp;More things I've shipped</b></summary>

<br>

| Project | Stack | What it does |
|:--|:--|:--|
| **[ReMinions](https://github.com/YanIanZ/ReMinions)** | Java | High-performance minion plugin for Paper 26.2+ |
| **[SourbyAntiCheat](https://github.com/YanIanZ/SourbyAntiCheat)** | Java | Server-side anticheat for the SourbyCraft stack |
| **[sourby-st](https://github.com/YanIanZ/sourby-st)** | JavaScript | Load-test bot swarm — hundreds of exploring bots from one VPS |
| **[KaNeil-Panel](https://github.com/YanIanZ/KaNeil-Panel)** | PHP | Game server control panel |
| **[KaNeil-Ship](https://github.com/YanIanZ/KaNeil-Ship)** | Go | Node daemon for the panel |
| **[KaNeil-plugins](https://github.com/YanIanZ/KaNeil-plugins)** | Python | Plugin registry + tooling |
| **[pelican-go](https://github.com/YanIanZ/pelican-go)** | Go | Pelican panel experiments |
| **[SourbySkyBlock](https://github.com/YanIanZ/SourbySkyBlock)** | Java | SkyBlock gamemode implementation |

</details>

<br>

<!-- ════════════════════════════════ ARCADE ════════════════════════════════ -->

<div align="center">

# 🕹️ &nbsp;T H E &nbsp; A R C A D E

**Four games. All of them actually work. None of them need an install.**

<sub>Yes, really — the board below is live state committed into this repo.</sub>

</div>

---

### 💣 &nbsp;Game 1 — Creeper Sweeper &nbsp;<sub>`multiplayer · live · anyone can play`</sub>

Minesweeper, 8×8, **10 creepers**, played by clicking cells in this README.
Every click opens a pre-filled GitHub issue; a bot plays the move, redraws the
board below, and closes the issue. **The first dig is always safe.**

<!-- CS:BOARD:START -->

<p align="center">🎮 &nbsp;<b>LIVE</b> &nbsp;·&nbsp; mode <b>DIG</b> &nbsp;·&nbsp; 🚩 10 flags left &nbsp;·&nbsp; 0 moves played</p>

|   | 🇦 | 🇧 | 🇨 | 🇩 | 🇪 | 🇫 | 🇬 | 🇭 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C0%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 2️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C1%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 3️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C2%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 4️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C3%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 5️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C4%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 6️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C5%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 7️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C6%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |
| 8️⃣ | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C0&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C1&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C2&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C3&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C4&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C5&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C6&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) | [⬛](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Creveal%7C7%7C7&body=Press+Create+%E2%80%94+a+bot+plays+this+move.) |

<p align="center">
  [![flag mode](https://img.shields.io/badge/🚩_switch_to_FLAG_mode-0d1117?style=for-the-badge&labelColor=0d1117&color=22d3ee)](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Cmode%7Cflag&body=Press+Create+%E2%80%94+a+bot+plays+this+move.)
  [![new game](https://img.shields.io/badge/🔄_NEW_BOARD-0d1117?style=for-the-badge&labelColor=0d1117&color=3ddb7d)](https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Cnew&body=Press+Create+%E2%80%94+a+bot+plays+this+move.)
</p>

<p align="center"><sub>🏆 0 cleared &nbsp;·&nbsp; 💥 0 exploded &nbsp;·&nbsp; 🎲 board #1</sub></p>

<!-- CS:BOARD:END -->

<details>
<summary><sub><b>how it works / play from the terminal</b></sub></summary>

<br>

Every board link just opens an issue whose **title** is the move. You can do the same by hand:

```bash
gh issue create --repo YanIanZ/YanIanZ --title "cs|reveal|3|4" --body "dig"
gh issue create --repo YanIanZ/YanIanZ --title "cs|flag|0|7"   --body "flag"
gh issue create --repo YanIanZ/YanIanZ --title "cs|new"        --body "reset"
```

| Command | Effect |
|:--|:--|
| `cs\|reveal\|<row>\|<col>` | Dig a block (0-based coordinates) |
| `cs\|flag\|<row>\|<col>` | Plant or remove a flag |
| `cs\|mode\|flag` / `cs\|mode\|reveal` | Switch what every board link does |
| `cs\|new` | Rack a fresh board |

Engine: [`game/creeper-sweeper/engine.py`](game/creeper-sweeper/engine.py) ·
State: [`state.json`](game/creeper-sweeper/state.json) ·
Workflow: [`creeper-sweeper.yml`](.github/workflows/creeper-sweeper.yml)

</details>

<br>

---

### 🗺️ &nbsp;Game 2 — The Deep Dark Descent &nbsp;<sub>`single player · 4 endings`</sub>

A choose-your-own-adventure that runs entirely on markdown links. You wake at
**Y = -59** with three hearts, a wooden pickaxe and one torch. Something down
there is listening.

<p align="center">
  <a href="game/deep-dark/start.md">
    <img src="https://img.shields.io/badge/▶_START_THE_DESCENT-0d1117?style=for-the-badge&logo=minecraft&logoColor=3ddb7d&color=3ddb7d&labelColor=0d1117" height="40" />
  </a>
</p>

<p align="center">
  <sub>💎 The Haul &nbsp;·&nbsp; 🖤 Sonic Boom &nbsp;·&nbsp; 🕳️ Still Down There &nbsp;·&nbsp; 📘 <b>???</b></sub>
</p>

<br>

---

### 🧠 &nbsp;Game 3 — Block Quiz &nbsp;<sub>`click to reveal`</sub>

<details>
<summary><b>1.</b> &nbsp;I glow blue underground and enchanters fight over me. What am I?</summary>
<br>

> **Lapis Lazuli Ore.** The enchanting table's best friend. 💙

</details>

<details>
<summary><b>2.</b> &nbsp;I'm silent, I'm green, and I'll delete your build in one second flat.</summary>
<br>

> **Creeper.** *Aw man.* 💥 &nbsp;(There are ten of them in Game 1. Good luck.)

</details>

<details>
<summary><b>3.</b> &nbsp;On Folia, why does this crash with <code>Thread failed main thread check</code>?</summary>
<br>

```java
@EventHandler
public void onJoin(PlayerJoinEvent e) {
    Bukkit.getScheduler().runTask(plugin, () -> e.getPlayer().openInventory(menu));
}
```

> Because Folia has **no global main thread**. Per-player work must run on that
> player's **region/entity scheduler**, not the global one:
>
> ```java
> e.getPlayer().getScheduler().run(plugin, t -> e.getPlayer().openInventory(menu), null);
> ```
>
> Same rule for teleports, titles, and giving items. 🧵

</details>

<details>
<summary><b>4.</b> &nbsp;I have light level 15, I can't be enchanted, and mobs hate me most.</summary>
<br>

> **Torch.** Cheapest anti-mob defence in the game — and the thing you drop at the
> worst possible moment in Game 2. 🔥

</details>

<details>
<summary><b>5.</b> &nbsp;How many shrieks before the Warden is summoned?</summary>
<br>

> **Four.** Three is a warning. The fourth one is a spawn.
> *(Wool absorbs vibration. Sneaking produces none. Sprinting produces all of it.)* 🖤

</details>

<br>

---

### 🐍 &nbsp;Game 4 — Snake eats my contributions &nbsp;<sub>`auto · every 12h`</sub>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake.svg" />
    <img alt="snake eating the contribution graph" src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake.svg" width="100%" />
  </picture>
</p>

<br>

<!-- ════════════════════════════════ STATS ════════════════════════════════ -->

## `~/` &nbsp;stats

<p align="center">
  <img height="165" src="https://github-readme-stats.shion.dev/api?username=YanIanZ&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=3ddb7d&icon_color=22d3ee&text_color=8b96a5" alt="stats" />
  <img height="165" src="https://github-readme-stats.shion.dev/api/top-langs/?username=YanIanZ&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&layout=compact&langs_count=8&bg_color=0d1117&title_color=3ddb7d&text_color=8b96a5" alt="top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=YanIanZ&theme=github-dark-blue&hide_border=true&background=0d1117&ring=3ddb7d&fire=22d3ee&currStreakLabel=3ddb7d&sideLabels=8b96a5&dates=8b96a5" alt="streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=YanIanZ&bg_color=0d1117&color=8b96a5&line=3ddb7d&point=22d3ee&area=true&area_color=3ddb7d&hide_border=true&custom_title=commits%20per%20day" width="100%" alt="activity graph" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=YanIanZ&theme=matrix&no-frame=true&no-bg=true&column=7&margin-w=6&margin-h=6" alt="trophies" />
</p>

<br>

<!-- ════════════════════════════════ CONNECT ════════════════════════════════ -->

## `~/` &nbsp;connect

<p align="center">
  <a href="https://sourby.my.id"><img src="https://img.shields.io/badge/Website-0d1117?style=for-the-badge&logo=googlechrome&logoColor=3ddb7d" /></a>
  <a href="https://github.com/YanIanZ"><img src="https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=3ddb7d" /></a>
  <a href="https://github.com/YanIanZ/YanIanZ/issues/new?title=cs%7Cnew&body=start%20a%20fresh%20board"><img src="https://img.shields.io/badge/Play_a_round-0d1117?style=for-the-badge&logo=gamejolt&logoColor=22d3ee" /></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/main/assets/footer.svg" alt="" width="100%" />
</p>
