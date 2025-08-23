import gifos, dotenv, os
from datetime import datetime
from zoneinfo import ZoneInfo

FONT_FILE_BITMAP = "./assets/fonts/JetBrainsMonoNerdFont-Regular.ttf"
GITHUB_TOKEN = os.getenv("TOKEN")


nitch = f"""
 \x1b[36m  _  ___      ____  ____
  / |/ (_)_ __/ __ \/ __/
 /    / /\ \ / /_/ /\ \
/_/|_/_//_\_\\\\____/___/
\x1b[0m
  ╭───────────╮
  │ \x1b[31m\x1b[0m  user   │ \x1b[31mhotln\x1b[0m
  │ \x1b[33m\x1b[0m  hname  │ \x1b[33mnixos\x1b[0m
  │ \x1b[32m󰻀\x1b[0m  distro │ \x1b[32mNixOS 24.11 (Vicuna)\x1b[0m
  │ \x1b[36m󰌢\x1b[0m  kernel │ \x1b[36m6.6.48\x1b[0m
  │ \x1b[34m\x1b[0m  uptime │ \x1b[34m20 sumtin\x1b[0m
  │ \x1b[35m\x1b[0m  shell  │ \x1b[35mzsh\x1b[0m
  │ \x1b[31m󰏖\x1b[0m  pkgs   │ \x1b[31m2229\x1b[0m
  │ \x1b[33m󰍛\x1b[0m  memory │ \x1b[33m4506 | 64174 MiB\x1b[0m
  ├───────────┤
  │ 󰏘  colors │  \x1b[31m  \x1b[0m\x1b[32m  \x1b[0m\x1b[33m  \x1b[0m\x1b[34m  \x1b[0m\x1b[35m  \x1b[0m\x1b[36m  \x1b[0m\x1b[37m  \x1b[0m
  ╰───────────╯
    """


# Initialize Terminal
t = gifos.Terminal(1300, 1200, 15, 15, FONT_FILE_BITMAP, 15)

def get_stats():
    ignore_repos = ['github-readme-stats']
    git_user_details = gifos.utils.fetch_github_stats("hotln", ignore_repos)

    return git_user_details

def string_format(stats):
    for x, lang in enumerate(stats.languages_sorted):
        stats.languages_sorted[x] = list(stats.languages_sorted[x])
        stats.languages_sorted[x][0] = "{:<25}".format(lang[0])
        stats.languages_sorted[x][1] = "{:<5}".format(lang[1])

    # Set length of strings so that btm stays the same size even when stats change
    stats.account_name = "{:<16}".format(stats.account_name)
    stats.total_commits_all_time = "{:<10}".format(stats.total_commits_all_time)
    stats.total_pull_requests_made = "{:<6}".format(stats.total_pull_requests_made)
    stats.user_rank.level = "{:<9}".format(stats.user_rank.level)
    stats.user_rank.percentile = str(stats.user_rank.percentile) + " %"
    stats.user_rank.percentile = "{:<7}".format(stats.user_rank.percentile)

    return stats

def shell(row, delay=0, contin=False, save=True):
    time_now = datetime.now(ZoneInfo("Europe/Paris")).strftime(
        "%a %b %d %I:%M:%S %Y"
    )
    t.gen_text(text=f"\x1b[37m \x1b[0m \x1b[31mnixos\x1b[0m \x1b[33mhotln\x1b[0m \x1b[32m ~\x1b[0m ................................................................... \x1b[35m12ms\x1b[0m \x1b[34m󰔟 {time_now}\x1b[0m", row_num=row, contin=False)
    t.gen_text(text=f"\x1b[32m❯ \x1b[0m", row_num=row+1, contin=False)
    t.clone_frame(20)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")

def main():

    # Obtain stats from Github
    stats = get_stats()
    stats = string_format(stats)


    t.set_font(FONT_FILE_BITMAP, 16)
    shell(1)
    col = t.curr_col
    t.gen_typing_text("\x1b[31mnitc", 2, contin=True)
    t.delete_row(2, col)
    t.gen_text("\x1b[32mnitch\x1b[0m", 2, contin=True)
    t.clone_frame(5)
    t.gen_text(text=nitch, row_num=3, contin=True)

    shell(22)
    col = t.curr_col
    t.gen_typing_text("\x1b[31mbt", 23, contin=True)
    t.delete_row(23, col)
    t.gen_text("\x1b[32mbtm\x1b[0m", 23, contin=True)
    t.clone_frame(10)
    t.clear_frame()

    t.set_font(FONT_FILE_BITMAP, 16, 0)
    t.toggle_show_cursor(False)

    bottom0 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     6%     │
│    │                                                                                                     ││\x1b[31mCPU0    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[32mCPU1    8%\x1b[0m     │
│    │                                                                                                     ││\x1b[33mCPU2    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[34mCPU3    6%\x1b[0m     │
│    │\x1b[31m                             ⣀⣀⠤⠤⠔⠒⠒⠤⠤⠤⣀⣀⡀                                                          \x1b[0m ││\x1b[35mCPU4    8%\x1b[0m     │
│    │\x1b[31m                   ⣀⣀⡠⠤⠤⠒⠒⠊⠉⠉            ⠈⠉⠉⠒⠒⠒⠤⠤⢄⣀⣀⡀                                               \x1b[0m ││\x1b[36mCPU5    3%\x1b[0m     │
│    │\x1b[31m         ⢀⣀⣀⠤⠤⠔⠒⠒⠉⠉                                 ⠈⠉⠉⠒⠒⠢⠤⠤⢄⣀⣀                                     \x1b[0m ││\x1b[37mCPU6    6%\x1b[0m     │
│    │\x1b[31m ⣀⡠⠤⠤⠒⠒⠉⠉⠁                 ⢀⣀⣀⣀⣀⡠⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⡀                   ⠉⣀⣀⣀⣀⣀⣀⣀⣀⡀⣀⣀⣀                        \x1b[0m ││\x1b[31mCPU7    6%\x1b[0m     │
│    │\x1b[32m   ⢀⣀⣀⣀⢀⣀⣀⣀⣀⠤⠤⠤⠤⠤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⣀⣀⣀⣀⣀⡀⠤⠤ \x1b[0m   ││\x1b[32mCPU8    3%\x1b[0m     │
│  0%│\x1b[33m⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⠒⠒ \x1b[0m   ││\x1b[33mCPU9    5%\x1b[0m     │
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   7%\x1b[0m     │
│  60s                                                                                                   0s││\x1b[35mCPU11   6%\x1b[0m     │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│
│    │                                     │RAM: 15%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │\x1b[33m⢣                               ⡠⡀                     \x1b[0m││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│\x1b[33m⠈⢆                             ⡰⠁⠱⡀                    \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│     │\x1b[33m ⠘⡄                           ⡰⠁  ⠱⡀                   \x1b[0m││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │\x1b[33m  ⠱⡀          ⢀⣀⣀⣀           ⡜     ⠱⡀                ⣀⠤\x1b[0m││1473      X                    0.2%      0.3%      0B/s     │
│     │\x1b[33m   ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁   ⠑⢄        ⡜       ⠱⡀          ⣀⠤⠔⠊⠉  \x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m                    ⠑⠤⡀   ⢀⠎         ⠱⡀     ⢀⠤⠒⠉       \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m                      ⠈⠢⡀⢀⠎           ⠱⡀ ⣀⠔⠊⠁          \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m                        ⠈⠊             ⠑⠉              \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m                                                       \x1b[0m││4235      brave                1.1%      0.8%      0B/s     │
│  0Mb│\x1b[35m⠒⠒⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤\x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││230964    nvim                 0.0%      0.1%      0B/s     │
│   60s                                                     0s││3864      brave                0.0%      0.8%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    bottom1 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     9%     │
│    │                                                                                                     ││\x1b[31mCPU0    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[32mCPU1    8%\x1b[0m     │
│    │                                                                                                     ││\x1b[33mCPU2    12%\x1b[0m    │
│    │                                                                                                     ││\x1b[34mCPU3    8%\x1b[0m     │
│    │\x1b[31m                                              ⢀                                                      \x1b[0m││\x1b[35mCPU4    9%\x1b[0m     │
│    │\x1b[31m                                           ⣀⢀⡠⠔⠤⣀⢄                       ⣀⡀                          \x1b[0m││\x1b[36mCPU5    4%\x1b[0m     │
│    │\x1b[31m                                        ⣀⣀⠔⠊⠁⠤⠒⠢⢄⠉⠒⠤⣀                ⣀⠤⠒⠉⣀⣀⡀⠑⠒⠢⠤⢄⣀⡀⣀                 \x1b[0m││\x1b[37mCPU6    10%\x1b[0m    │
│    │\x1b[35m                                     ⢀⠤⠒⠉⠒⠊⢀⣀⡠⠤⠤⣀⣀⠉⠒⠢⠉⠒⠤⣀        ⣀⠤⢀⣀⡠⠤⠒⠒⠉⠉⠉⠒⠒⠒⠒⠢⠤⠤⠤⠤⣀⣀⣀⣀⡀⣀⡀⣀⣀⣀⡀⣀⣀⣀⡀⡀\x1b[0m││\x1b[31mCPU7    7%\x1b[0m     │
│    │\x1b[34m⣀⣀⣀⢀⣀⣀⣀⣀⣀⣀⢀⢀⣀⡠⠤⠤⠒⠒⠉⠉⠁⠉⠁⣀⣀⠉⠉⠉⠉⠑⠒⠢⠤⠤⣀⣀⠤⣀⣀⣀⠤⠔⠒⠉⠉⠉⠉⠁⠉          ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⠒⠒⠢⠤⠤⠤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⣀⣀⣀⣀⣀⣀\x1b[0m││\x1b[32mCPU8    8%\x1b[0m     │
│  0%│\x1b[33m⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠁⠉⠉⠉⠉⠉⠉⠉⠁\x1b[0m││\x1b[33mCPU9    2%\x1b[0m     │
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%\x1b[0m     │
│  60s                                                                                                   0s││\x1b[35mCPU11   6%\x1b[0m     │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)\x1b[0m           │
│    │                                     │RAM: 16%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │                         
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│                                                                             nt(t) \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││4235      brave                1.1%      0.8%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │\x1b[33m       ⡠⡀                                            \x1b[0m  ││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│\x1b[33m      ⡰⠁⠱⡀                                            \x1b[0m ││1473      X                    0.2%      0.3%      0B/s     │
│     │\x1b[33m     ⡰⠁  ⠱⡀                                           \x1b[0m ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │\x1b[33m    ⡜     ⠱⡀                ⣀⠤⡀          ⢀⣀⣀⣀         \x1b[0m ││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│     │\x1b[33m    ⡜       ⠱⡀          ⣀⠤⠔⠊⠉  ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁   ⠑⢄      \x1b[0m ││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m  ⢀⠎         ⠱⡀     ⢀⠤⠒⠉                        ⠑⠤⡀    \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m ⢀⠎           ⠱⡀ ⣀⠔⠊⠁                             ⠈⠢⡀  \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m ⠊             ⠑⠉                                   ⠈  \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m                                                       \x1b[0m││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│  0Mb│\x1b[35m⠒⠒⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤\x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││230964    nvim                 0.0%      0.1%      0B/s     │
│   60s                                                     0s││3864      brave                0.0%      0.8%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    bottom2 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     3%     │
│    │                                                                                                     ││\x1b[31mCPU0    1%     \x1b[0m│
│    │                                                                                                     ││\x1b[32mCPU1    8%     \x1b[0m│
│    │                                                                                                     ││\x1b[33mCPU2    8%     \x1b[0m│
│    │                                                                                                     ││\x1b[34mCPU3    13%    \x1b[0m│
│    │                                                                                                     ││\x1b[35mCPU4    9%     \x1b[0m│
│    │                                                                                                     ││\x1b[36mCPU5    10%    \x1b[0m│
│    │\x1b[34m⣀                                                                        ⣀⡀                          \x1b[0m││\x1b[37mCPU6    10%    \x1b[0m│
│    │\x1b[37m⣀             ⢀⣀⡠⠤⣀    ⣀⠤⣀    ⢀⣀     ⣀⠤⣀⡀          ⣀⣀⣀⣀⣀⣀⣀⣀⣀    ⣀⠤⠒⠤⠤⣀⡀        ⢀⣀      ⣀    ⣀⡠⠤⣀     \x1b[0m││\x1b[31mCPU7    7%     \x1b[0m│
│    │\x1b[32m⣀⣀⣤⡴⠶⢖⣒⣒⠤⠤⠤⠤⠒⠒⠉⠁    ⣀⠤⠒⠉   ⠉⠒⠢⢄⡀⣀⢀⣀⣀⠤⠤⠒⠒⠢⠤⠤⣀⣀⢄⣀⣀⠒⠒⠉⠉     ⣀⣀⣀⣀⣀⠤⠒⠉⢀⣀⣀⡀  ⣈⣉⣑⣒⣤⠤⣀⡀⠊⠁ ⠉⠒⣀⠤⠒⠉⣀⠉⠑⠒⠤⣀⡀  ⠉⠑⠒⠤\x1b[0m││\x1b[32mCPU8    3%     \x1b[0m│
│  0%│\x1b[31m⣀⠒⠒⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││\x1b[33mCPU9    2%     \x1b[0m│
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%     \x1b[0m│
│  60s                                                                                                   0s││\x1b[35mCPU11   6%     \x1b[0m│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│                                                       t)    \x1b[0m│
│    │                                     │RAM: 17%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││4235      brave                1.1%      0.8%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │                                                       ││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│                                                       ││230964    nvim                 0.0%      0.1%      0B/s     │
│     │                                                       ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │                                                       ││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │ \x1b[33m⢠                                      ⢠⢣          ⡇⠸⡇\x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m⢀⢀⢣                                    ⢀⠇⠈⢆        ⡸⠃ ⠸\x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m⢀⠎⢣⢣                                   ⡜\x1b[35m⠜⠘⠘\x1b[0m\x1b[33m⡄      ⢀⠇  ⠈\x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m⠊  ⠣⡀                                 ⡸⠃  ⠈⢱      ⡜    \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m    ⠱⡀⠤⠤⠤⠤⢄⣀                        ⣀⢠⠃     ⢣    ⢠⠃    \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│  0Mb│\x1b[33m     ⠑⠒⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⣀⡠⠤⠔⠒⠒⠢⠤⠤⠤⠔⠒⠃      ⠈⠦⠤⢄⣀⡜     \x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││3864      brave                0.0%      0.8%      0B/s     │
│   60s                                                     0s││1473      X                    0.2%      0.3%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    bottom3 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│\x1b[31m            ⢠⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠒⠤⣀               \x1b[0m││\x1b[36mCPU     Use    \x1b[0m│
│    │\x1b[31m           ⢠⠃                                                                         ⠑⠢⢄⡀           \x1b[0m││               │
│    │\x1b[31m          ⢀⠎                                                                             ⠘⡄          \x1b[0m││All            │
│    │\x1b[31m         ⢀⠎                                                                               ⠘⡄         \x1b[0m││AVG     3%     │
│    │\x1b[31m         ⡜                                                                                 ⠘⡄        \x1b[0m││\x1b[31mCPU0    24%    \x1b[0m│
│    │\x1b[31m        ⡜                                                                                   ⠱⡀       \x1b[0m││\x1b[32mCPU1    8%     \x1b[0m│
│    │\x1b[31m       ⡰⠁                                                                                    ⠱⡀ ⢀ ⢀  \x1b[0m││\x1b[33mCPU2    32%    \x1b[0m│
│    │\x1b[31m      ⡰⠁\x1b[0m                                                                                \x1b[32m      ⢣⢠⠃⢣⡜  \x1b[0m││\x1b[34mCPU3    5%     \x1b[0m│
│    │\x1b[31m       ⡰⠁ \x1b[0m                                                                                \x1b[32m    ⡰⠁⠞⡰⢣⠁⠞\x1b[0m││\x1b[35mCPU4    9%     \x1b[0m│
│    │\x1b[31m   ⡔⠁  \x1b[0m                                                                                \x1b[34m      ⡔⠁⠋⢣⠃⢣⠋⢣\x1b[0m││\x1b[36mCPU5    10%    \x1b[0m│
│    │\x1b[31m  ⢀⠜    \x1b[0m                                                                                \x1b[36m   ⢀⠎⢀⡠⠔⠊⠒⢄⠔⠊\x1b[0m││\x1b[37mCPU6    13%    \x1b[0m│
│    │\x1b[31m⠤⢠⠊\x1b[0m\x1b[34m⣀⣀⣀⣀                                                                                   ⣀⠤⠒⠁⢀⡠⠔⠢⢄  \x1b[0m││\x1b[31mCPU7    19%    \x1b[0m│
│    │\x1b[31m⡠⠃ \x1b[0m\x1b[34m⣀   ⠉⣀⣀⣀⡠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠔⠒⠒⠒⠉⠉⠃⠉⠔⠊⠁  ⠔⠒⠒⠒\x1b[0m││\x1b[32mCPU8    2%     \x1b[0m│
│  0%│\x1b[37m⠒⠒⠒⠉⠉⠉⠉⠉⠒⠒⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⠔⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠁⠉⠉⠉⠁          \x1b[0m││\x1b[33mCPU9    24%    \x1b[0m│
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%     \x1b[0m│
│  60s                                                                                                   0s││\x1b[35mCPU11   15%    \x1b[0m│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│                                                       t)    \x1b[0m│
│    │                                     │RAM: 17%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││230964    nvim                 0.0%      0.1%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │                                                       ││25228     zellij               0.0%      0.2%      0B/s     │
│  0.8│                                                       ││4235      brave                1.1%      0.8%      0B/s     │
│     │                                                       ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │                                                       ││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │ \x1b[33m                             ⢀                        \x1b[0m││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.4│\x1b[33m ⢀⢆           ⢠⢣              ⡎⢆           ⡜⡄          \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m ⡜⠈⡆         ⢀⠇⠈⡆            ⡸⠃⠈⢆         ⡜⠁⢱          \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m⢰⠁ ⠘⡄        ⡜\x1b[0m\x1b[35m⠎⠘⢸  \x1b[0m\x1b[33m        ⢰⠁  ⠈⢆   ⡀   ⡰⠁ ⠈⢇         \x1b[0m ││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m⠇   ⠸⡀      ⡸\x1b[0m\x1b[35m⠊  ⠘⢇ \x1b[0m \x1b[33m       ⢀⠇    ⠈⠦⠤⠤⠤⣀⡀⡰⠁   ⠘⡄        \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│  0Mb│\x1b[33m     ⠱⠤⢄⣀⣀⡠⠴⠁    ⠘⣄⣀⠤⠤⠤⠤⠤⠔⠒⠉           ⠈⠁  \x1b[0m \x1b[35m  ⠱⠤⢄⣀⣀⡠⠤⠤⠤\x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│     └───────────────────────────────────────────────────────││3864      brave                0.0%      0.8%      0B/s     │
│   60s                                                     0s││1473      X                    0.2%      0.3%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    # Loop over Bottom command
    for x in range(2):
        t.gen_text(bottom0, 10, count=30)
        t.gen_text(bottom1, 10, count=30)
        t.gen_text(bottom2, 10, count=30)
        t.gen_text(bottom3, 10, count=30)

    t.toggle_show_cursor(True)


    t.gen_gif()

if __name__ == "__main__":
    main()
