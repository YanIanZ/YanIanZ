<!-- ════════════════════════════════ BANNER ════════════════════════════════ -->
<p align="center">
  <img src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/main/assets/banner.svg" alt="YanIanZ — Minecraft Plugin Engineer" width="100%" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=4D9FFF&center=true&vCenter=true&width=680&lines=Folia-safe+plugins+for+Paper+26.2;Region-threaded%2C+async%2C+zero+main-thread+I%2FO;Panels%2C+proxies+and+the+boring+infra+that+keeps+it+up" alt="what I do" />
</p>

<p align="center">
  <a href="https://sourby.my.id"><img src="https://img.shields.io/badge/sourby.my.id-0d1117?style=flat-square&logo=googlechrome&logoColor=4d9fff&labelColor=0d1117" alt="website" /></a>
  <img src="https://img.shields.io/badge/Surabaya,_ID-0d1117?style=flat-square&logo=googlemaps&logoColor=ffc83d&labelColor=0d1117" alt="location" />
  <a href="https://github.com/YanIanZ?tab=followers"><img src="https://img.shields.io/github/followers/YanIanZ?style=flat-square&logo=github&logoColor=4d9fff&label=followers&labelColor=0d1117&color=0d1117" alt="followers" /></a>
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
  <a href="https://github.com/YanIanZ/SourbyCraft"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SourbyCraft&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=4d9fff&icon_color=ffc83d" /></a>
  <a href="https://github.com/YanIanZ/SEssentials"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SEssentials&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=4d9fff&icon_color=ffc83d" /></a>
</p>
<p align="center">
  <a href="https://github.com/YanIanZ/SourbyEconomy"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=SourbyEconomy&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=4d9fff&icon_color=ffc83d" /></a>
  <a href="https://github.com/YanIanZ/Cherry"><img width="49%" src="https://github-readme-stats.shion.dev/api/pin/?username=YanIanZ&repo=Cherry&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=4d9fff&icon_color=ffc83d" /></a>
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

<!-- ════════════════════════════════ SNAKE ════════════════════════════════ -->

## `~/` &nbsp;snake

<div align="center">

<sub>Regenerated every 12 hours by <a href=".github/workflows/snake.yml">a workflow</a> — it eats the contribution graph one commit at a time.</sub>

<br><br>

<table>
<tr>
<td align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake.svg" />
    <img alt="snake eating the contribution graph" src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/output/snake-dark.svg" />
  </picture>
</td>
</tr>
</table>

</div>

<br>

<!-- ════════════════════════════════ STATS ════════════════════════════════ -->

## `~/` &nbsp;stats

<p align="center">
  <img height="165" src="https://github-readme-stats.shion.dev/api?username=YanIanZ&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=4d9fff&icon_color=ffc83d&text_color=8b96a5" alt="stats" />
  <img height="165" src="https://github-readme-stats.shion.dev/api/top-langs/?username=YanIanZ&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&layout=compact&langs_count=8&bg_color=0d1117&title_color=4d9fff&text_color=8b96a5" alt="top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.vercel.app/?user=YanIanZ&theme=github-dark-blue&hide_border=true&background=0d1117&ring=4d9fff&fire=ffc83d&currStreakLabel=4d9fff&sideLabels=8b96a5&dates=8b96a5" alt="streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=YanIanZ&bg_color=0d1117&color=8b96a5&line=4d9fff&point=ffc83d&area=true&area_color=4d9fff&hide_border=true&custom_title=commits%20per%20day" width="100%" alt="activity graph" />
</p>

<p align="center">
  <img src="https://github-trophies.vercel.app/?username=YanIanZ&theme=nord&no-frame=true&no-bg=true&column=7&margin-w=6&margin-h=6" alt="trophies" />
</p>

<br>

<!-- ════════════════════════════════ CONNECT ════════════════════════════════ -->

## `~/` &nbsp;connect

<p align="center">
  <a href="https://sourby.my.id"><img src="https://img.shields.io/badge/Website-0d1117?style=for-the-badge&logo=googlechrome&logoColor=4d9fff" /></a>
  <a href="https://github.com/YanIanZ"><img src="https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=4d9fff" /></a>
  <a href="https://github.com/YanIanZ?tab=repositories"><img src="https://img.shields.io/badge/Repositories-0d1117?style=for-the-badge&logo=git&logoColor=ffc83d" /></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/YanIanZ/YanIanZ/main/assets/footer.svg" alt="" width="100%" />
</p>
