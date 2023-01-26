# i3_config
Config i3+i3status.py for quick start on new instalation (Debian based)


# KEYBOARD CONFIGURATION FILE /etc/default/keyboard

XKBLAYOUT="us" add ",ru"
XKBOPTIONS="" add "grp:alt_shift_toggle"

# test configuration
```bash
setupcon
```
# make changes
```bash
setupcon -k -f
```
# 2 Enable tap for laptops
Make a new file 
```bash
sudo nano /etc/X11/xorg.conf.d/touchpad-tap.conf
```
and add the following:

Add below text
```bash
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
        Option "Tapping" "on"
EndSection
```
# 3 Backlight control for laptops
```bash
sudo apt install light
sudo chmod +s /usr/bin/light
```
# 4 Prepare for i3wm installation
```bash
sudo apt install arandr autorandr j4-dmenu-desktop \
python3-pip lm-sensors git curl nitrogen flameshot \
libsensors4-dev libiw-dev i3lock-fancy i3pystatus i3 fonts-font-awesome
pip install -U pip setuptools
pip install git+https://github.com/bastienleonard/pysensors.git basiciw xkbgroup
```

# 5 Dark theme by default I think it'll work only if install before i3 some other desktop
create file if not exists 
```bash
nano ~/.config/gtk-3.0/settings.ini
```
Add lines
```bash
[Settings]
gtk-application-prefer-dark-theme=1
```
