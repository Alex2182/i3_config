#1 KEYBOARD CONFIGURATION FILE /etc/default/keyboard
XKBLAYOUT="us" add ",ru"
XKBOPTIONS="" add "grp:alt_shift_toggle"

#test configuration
setupcon
#make changes
setupcon -k -f

#2Enable tap
#Make a new file at /etc/X11/xorg.conf.d/touchpad-tap.conf and add the following:
#Add below text
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

#3Backlight control
sudo apt install light
sudo chmod +s /usr/bin/light

#4Prepare for i3wm installation
sudo apt install arandr autorandr j4-dmenu-desktop python3-pip lm-sensors git curl nitrogen flameshot libsensors4-dev libiw-dev i3lock-fancy i3pystatus i3 fonts-font-awesome
pip install -U pip setuptools
pip install git+https://github.com/bastienleonard/pysensors.git basiciw xkbgroup


#5Dark theme by default I think it'll work only if install before i3 some other desktop
# create file if not exists ~/.config/gtk-3.0/settings.ini
#Add lines
[Settings]
gtk-application-prefer-dark-theme=1
