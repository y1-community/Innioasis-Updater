<div align="right">
</div>

# Innioasis Updater
<img src="mtkclient/gui/images/icon.png" alt="Innioasis Updater Icon" width="128"/>
Innioasis Updater is an easy, one-click firmware installer for the Innioasis Y1 MP3 player running Android firmwares. It is a modification of mtkclient to enable the installation of Updates, Factory Restore and installation of Custom Firmwares like the Multiwirth ROM with Rockbox.

[How to Install](https://github.com/team-slide/Innioasis-Updater/tree/main?tab=readme-ov-file#mtkclient-credits)

## Devloped by
- Ryan Specter of Team Slide

## Special Thanks to

### Team Slide branding lead
- u/_allstar
  
### r/innioasis Mods
- u/wa-a-melyn
- u/multiwirth
- u/TwitchyMcJoe
- u/Key-Brilliant5623

### ROM Developer
 - [@Multiwirth](https://www.github.com/multiwirth)

### Rockbox Y1 Port Developer
 - [@rockbox-y1 (u/After-Acanthaceae547)](https://www.github.com/rockbox-y1)
### TikTok / YouTube creator
- Ryan / Corduroy cat - @catsteal3r on TikTok
  
## MTKclient Credits

- bkerler for creating mtkclient
- kamakiri [xyzz]
- linecode exploit [chimera]
- Chaosmaster
- Geert-Jan Kreileman (GUI, design & fixes)


## Install

### Windows (64bit Intel/AMD Only)

Easy Install: You can easily install this with the Windows and Driver setup packages 

[Download here](https://www.github.com/team-slide/Innioasis-Updater/releases/latest)

#### Driver Setup
- Install normal MTK Serial Port driver ([driver_mtk.exe](https://github.com/team-slide/Innioasis-Updater/releases/download/1.0.0/driver_mtk.exe))
- Install USB Development Kit ([driver_usbdk.msi](https://github.com/team-slide/Innioasis-Updater/releases/download/1.0.0/driver_usbdk.msi)
- Restart your PC

 Notice to ARM64 Users: You can only use the Remote Control, Screenshot and App Install features of Y1 Helper (part of Innioasis Updater on Windows), 
 you'll need to use another OS / computer to install your firmware if you have an ARM64 (e.g Snapdragon) Windows PC or run it in WSL with USBIPD. (Advanced)

### macOS Easy App Setup (Needs work)

[Download here](https://www.github.com/team-slide/Innioasis-Updater/releases/latest)
An experimental .app version is available to try [here](https://www.github.com/team-slide/Innioasis-Updater/releases/latest) this is intended to be easy for most users to install
if it doesnt run for you, please file an issue with a copy of your launcher.log from /Users/yourname/Library/Application Support/Innioasis Updater (you'll need to press cmd, shift, . to reveal this in Finder)

### Troubleshooting: If the Mac .app doesn't work after two tries, please run these commands a line at a time, by copy-pasting into Terminal and hitting Enter/Return after each.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install libusb openssl cmake pkg-config
cd "$HOME/Library/Application Support/Innioasis Updater"
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade wheel setuptools pyusb pycryptodome pycryptodomex colorama shiboken6 pyside6 mock pyserial flake8 keystone-engine capstone unicorn keystone requests
python3 updater.py
```

### If the .app doesnt work below you can...

#### Set up and run Python Script Manuall on Mac

Open Terminal and run each of these a line at a time.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install libusb openssl cmake pkg-config
git clone https://github.com/team-slide/Innioasis-Updater
cd Innioasis-Updater
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade wheel setuptools pyusb pycryptodome pycryptodomex colorama shiboken6 pyside6 mock pyserial flake8 keystone-engine capstone unicorn keystone requests
pip install -r requirements.txt
```

Then reboot your mac, and run Innioasis Updater in terminal with 

```
cd Innioasis-Updater
python3 updater.py
```


---------------------------------------------------------------------------------------------------------------

### Linux - (Ubuntu recommended, no patched kernel needed except for kamakiri)

#### Install python >=3.8, git and other deps

#### For Debian/Ubuntu
```
sudo apt install python3 git libusb-1.0-0 python3-pip
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
sudo dnf install python3 git libusb1
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

### Using Innioasis Updater om Windows
Run Innioasis Updater from the Start Menu

### Using Innioasis Updater.app on Mac
Launch the app, if it doesnt work, try again.
if it still doesnt work check the Mac troubleshooting instructions.

### Using Innioasis Updater on Linux:
To start installing firmwares:
```
python updater.py
```

or:
```
python3 updater.py
```
