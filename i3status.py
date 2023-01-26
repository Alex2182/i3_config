import subprocess
import os
import os.path
import requests
from i3pystatus import Status
from i3pystatus.updates import pacman, cower


status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week

#status.register("updates",
#    format = "Updates: {count}",
#    format_no_updates = "",
#    on_leftclick="termite --geometry=1200x600 --title=updates -e 'pacaur --needed --noconfirm --noedit -Syu'",
#    backends = [pacman.Pacman(), cower.Cower()])
status.register("xkblayout", layouts=["us", "ru"])

status.register("clock",
    format=" %H:%M:%S",
    color='#C678DD',
    interval=5,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="  %a %d-%m-%Y ",
    color='#61AEEE',
    interval=1000,)


status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted=' [muted]',
    format=" {volume}%")

status.register("network",
    interface="eth0",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up=": {v4cidr}",
    format_down="",
     interval=10)

status.register("network",
    interface="wlan0",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up="  {essid} ({quality}%)",
    format_down="",
    interval=10)

status.register("backlight",
    interval=10,
    format=" {percentage:.0f}%",
    backlight="intel_backlight",)


status.register("battery",
    battery_ident="BAT0",
    interval=10,
    format="{status}{percentage:.0f}%({remaining})",
    alert=True,
    alert_percentage=15,
    color="#6799AA",
    critical_color="#FF1919",
    charging_color="#E5E500",
    full_color="#D19A66",
    status={
        "DIS": " ",
        "CHR": "  ",
        "FULL": "   ",
},)

status.register("temp",
    interval=10,
    format=" {Package_id_0}°C",
    hints={"markup": "pango"},
    lm_sensors_enabled=True,
    dynamic_color=True
                )

status.register("cpu_usage",
    on_leftclick="termite --title=htop -e 'htop'",
    format="  {usage}%",
    interval=10,)

status.register("mem",
    color="#56B6C2",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {avail_mem}/{total_mem} GB",
    divisor=1073741824,)

status.register("disk",
    color='#56B6C2',
    path="/home",
    on_leftclick="pcmanfm",
    format=" {avail} GB",)

#status.register("text",
#    text = requests.get('https://wttr.in/Tver?format=2').text.replace('\n',''),
#    color="#ffffff")

status.register("shell",
        format = "Tver {output}",
        command = "curl -k https://wttr.in/Tver?format=2",
        interval=600
)

#read_file WEATHER{
#    format = “%content”
#    path = “/home/abonin/.config/i3/wttr”
#}

#status.register("disk",
#    hints = {"separator": False, "separator_block_width": 3},
#    color='#ABB2BF',
#    path="/",
#    format=": {avail} GB",)

#status.register('ping',
#    format_disabled='',
#    color='#61AEEE')

status.run() 
