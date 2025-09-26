# Please ignore any tutorials or guides that brought you here, 

# take care to ensure you use the www.innioasis.app website to install the app. 

[<img src="start_here.png" alt="Innioasis Updater Screenshot"/>](https://innioasis.app)
[<img src="mtkclient/gui/images/screenshot.jpg" alt="Innioasis Updater Screenshot"/>](https://innioasis.app)

# Innioasis Updater
<img src="mtkclient/gui/images/icon.png" alt="Innioasis Updater Icon" width="128"/>
Innioasis Updater is an easy, one-click firmware installer for the Innioasis Y1 MP3 player running Android firmwares. It is a modification of mtkclient to enable the installation of Updates, Factory Restore and installation of Custom Firmwares like the Multiwirth ROM with Rockbox.

# [Download and guide for Mac and Windows at Innioasis.app](https://innioasis.app)



## Devloped using Cursor IDE by
- Ryan Specter of Team Slide

## Special Thanks to

### Team Slide branding lead
- u/_allstar
  
### r/innioasis Mods
- u/wa-a-melyn
- u/TwitchyMcJoe
- u/Key-Brilliant5623

### ROM Developer
 - [@Multiwirth](https://www.github.com/multiwirth)

### Rockbox Y1 Port Developer and custom ROM packager
 - [@rockbox-y1 (u/After-Acanthaceae547)](https://www.github.com/rockbox-y1)
 ### TikTok / YouTube creators
- Ryan /@catsteal3r on TikTok
- Corduroy cat - YouTuber
- Edit: I previously credited these as the same individual but it turns out they are actually seperate content creators. Sorry for any confusion caused. - Ryan Specter 
## MTKclient Credits

- bkerler for creating mtkclient
- kamakiri [xyzz]
- linecode exploit [chimera]
- Chaosmaster
- Geert-Jan Kreileman (GUI, design & fixes)

## Installing on Linux

### Linux - (Ubuntu recommended)

#### Install python >=3.8, git and other deps

#### For Debian/Ubuntu
```
sudo apt install python3 git libusb-1.0-0 python3-pip android-sdk-platform-tools
```
#### For ArchLinux
```
(sudo) pacman -S  python python-pip python-pipenv git libusb
```
or
```
yay -S python python-pip git libusb
```

#### For Fedora
```
sudo dnf install python3 git libusb1 android-tools
```

#### Grab files
```
git clone https://github.com/team-slide/Innioasis-Updater
cd Innioasis-Updater
pip3 install -r requirements.txt
pip3 install .
```

### Using venv
```
python3 -m venv ~/.venv
git clone https://github.com/team-slide/Innioasis-Updater
cd Innioasis-Updater
. ~/.venv/bin/activate
pip install -r requirements.txt
pip install .
```

#### Install rules
```
sudo usermod -a -G plugdev $USER
sudo usermod -a -G dialout $USER
sudo cp mtkclient/Setup/Linux/*.rules /etc/udev/rules.d
sudo udevadm control -R
sudo udevadm trigger
```
Make sure to reboot after adding the user to dialout/plugdev. If the device
has a vendor interface 0xFF (like LG), make sure to add "blacklist qcaux" to
the "/etc/modprobe.d/blacklist.conf".

---------------------------------------------------------------------------------------------------------------
## Usage
### Activating your venv
In order to activate your venv you'll need to run these commands
```
. ~/.venv/bin/activate
```
You should see something like this...
```
(.venv) [user@hostname]$ 
```
This means you are on venv folder!

### Using Innioasis Updater on Linux:
To start installing firmwares:
```
python updater.py
```
or:
```
python3 updater.py
```





















# Windows 64Bit Intel/AMD Only 
# Please follow the setup steps at [drivers.innioasis.app](https://innioasis.app) to get the drivers you need.
