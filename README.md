<div align="right">
</div>

# Innioasis Updater
<img src="mtkclient/gui/images/icon.png" alt="Innioasis Updater Icon" width="128"/>
Innioasis Updater is an easy, one-click firmware installer for the Innioasis Y1 MP3 player running Android firmwares. It is a modification of mtkclient to enable the installation of Updates, Factory Restore and installation of Custom Firmwares like the Multiwirth ROM with Rockbox.

## 🐍 Python Script written in 🧠💻Cursor AI by
- Ryan Specter of Team Slide

## Special Thanks to

r/innioasis Mods
- u/wa-a-melyn
- u/multiwirth
- u/TwitchyMcJoe
- u/Key-Brilliant5623
Team Slide branding lead
- u/_allstar
TikTok / YouTube creator
- Ryan/ Corduroy cat - @catsteal3r on TikTok
  
## MTKclient Credits

- bkerler for creating mtkclient
- kamakiri [xyzz]
- linecode exploit [chimera]
- Chaosmaster
- Geert-Jan Kreileman (GUI, design & fixes)


## Install

### Windows

Easy Install: You can easily install this with the Windows and Driver setup packages [here](https://www.github.com/team-slide/Innioasis-Updater/releases/latest)

### macOS Easy App Setup (Needs work)

An experimental .app version is available to try [here](https://www.github.com/team-slide/Innioasis-Updater/releases/latest) this is intended to be easy for most users to install but if it doesnt run for you, please file an issue with a copy of your launcher.log from /Users/yourname/Library/Application Support/Innioasis Updater (you'll need to press cmd, shift, . to reveal this in Finder)

### macOS Manual Setup

#### Install brew, macFUSE, OpenSSL

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install libusb openssl
```

You may need to **reboot**

#### Grab files
```
git clone https://github.com/team-slide/Innioasis-Updater
cd Innioasis-Updater
```

#### Create python 3.9 venv and install dependencies
```
python3.9 -m venv mtk_venv
source mtk_venv/bin/activate
pip3 install --pre --no-binary capstone capstone
pip3 install PySide6 libusb
pip3 install -r requirements.txt
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

### Windows Manual Python Script Setup

#### Install python + git
- Install python >= 3.9 and git
- If you install python from microsoft store, "python setup.py install" will fail, but that step isn't required.
- WIN+R ```cmd```

#### Install Winfsp (for fuse)
Download and install [here](https://winfsp.dev/rel/)

#### Install OpenSSL 1.1.1 (for python scrypt dependency)
Download and install [here](https://sourceforge.net/projects/openssl-for-windows/files/)

#### Grab files and install
```
git clone https://github.com/team-slide/Innioasis-Updater
cd Innioasis-Updater
pip3 install -r requirements.txt
```

#### Get latest UsbDk 64-Bit
- Install normal MTK Serial Port driver (or use default Windows COM Port one, make sure no exclamation is seen)
- Get usbdk installer (.msi) from [here](https://github.com/daynix/UsbDk/releases/) and install it
- Test on device connect using "UsbDkController -n" if you see a device with 0x0E8D 0x0003
- Works fine under Windows 10 and 11 :D

#### Building wheel issues (creds to @Oyoh-Edmond)
##### Download and Install the Build Tools:
    Go to the Visual Studio Build Tools [download](https://visualstudio.microsoft.com/visual-cpp-build-tools) page.
    Download the installer and run it.

###### Select the Necessary Workloads:
    In the installer, select the "Desktop development with C++" workload.
    Ensure that the "MSVC v142 - VS 2019 C++ x64/x86 build tools" (or later) component is selected.
    You can also check "Windows 10 SDK" if it’s not already selected.

###### Complete the Installation:
    Click on the "Install" button to begin the installation.
    Follow the prompts to complete the installation.
    Restart your computer if required.

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

### Using Innioasis Updater:
To start installing firmwares:
```
python updater.py
```
