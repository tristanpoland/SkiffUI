# Warning!: It's a bit broken and very incomplete, this is in-dev and nothing is for sure, use with care!
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ce462fd37100447190f567eaf09e38ff)](https://app.codacy.com/gh/Gameplex-Software/SkiffUI/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) ![Contribs Badge](https://img.shields.io/github/contributors/gameplex-software/skiffui) ![Version](https://img.shields.io/github/v/release/gameplex-software/skiffui) ![License](https://img.shields.io/github/license/gameplex-software/skiffui) ![](https://img.shields.io/discord/773279144896757761)
<p align=center>
<img width=100% src='https://user-images.githubusercontent.com/34868944/224514426-5096788f-780f-40b5-b391-7697e3e2a237.png'/>
</p>

## Contents
* [Why SkiffUI](https://github.com/Gameplex-Software/SkiffUI/#why-use-skiffui)
* [How it works](https://github.com/Gameplex-Software/SkiffUI/#how-it-works)
* [Installation](https://github.com/Gameplex-Software/SkiffUI/#installation)
    * [InDev](https://github.com/Gameplex-Software/SkiffUI/#latest-stable)
        * [Windows](https://github.com/Gameplex-Software/SkiffUI/#windows)
        * [Mac](https://github.com/Gameplex-Software/SkiffUI/#macos)
        * [Linux](https://github.com/Gameplex-Software/SkiffUI/#linux)



# The worlds first container network manager
Development is a work in progress, please follow us on social media for updates (socials are in the footer of our website)
  
## Why Use SkiffUI
SkiffUI provides the first easy to use, Drag-and-Drop user interface for modifying, or networking containers after creation. SkiffUI currently supports only Docker but could easily be expanded to interact with Docker Swarms and Kubernetes clusters later on.

## How it works
SkiffUI interacts with docker by converting graphical node data into commands for your container service, these commands are then executed as root on the host.

[Visit our company website](https://gameplexsoftware.com)

[SkiffUI Website](https://gameplexsoftware.com/skiffui)

# Beta UI

<video src='https://user-images.githubusercontent.com/34868944/230649903-c31c8283-a296-4e4a-934e-79477725112f.mp4'></video>

# Installation

##Requirements
- Docker (either desktop or command line) Temporary requirement to prevent app crashing, soon to be un-needed

## Latest Beta
### News
- Now uses 94mb of memory idle compared to the previous 780mb, this is due to removing excess code that was no longer needed and fixing some accidental looping code as well as clearing out un-needed variables and several other improvements
- Now uses 0-2% CPU idle on Ryzen 5 5600g (Compared to 12% before the performance improvements)
- Cache improvements now mean a more responsive interface.

### Windows
Note: you need python 3.8 for this project

```
git clone https://github.com/Gameplex-Software/SkiffUI/
cd .\SkiffUI-master\
pip3.8 install -r requirements.txt
cd .\src
python3.8 main.py
```

### Linux
```
coming soon
```

### MacOS
```
coming soon
```


## Windows

git clone https://github.com/Gameplex-Software/SkiffUI/
1. Make sure you have Python 3.8, 3.9 or 3.10 installed on your system.
2. Run ``setup.bat``
4. Run ``cd src`` then ``python main.py`` to navigate to the src directory and run Gimel Studio.
5. To build an executable, make sure you are in the root directory and run ``python build.py``. The executable will be generated in the ``dist`` folder.

## Linux

*This has been tested on Debian-based systems (Ubuntu, Linux Mint). Other distros may require extra configuration.*

1. Make sure you have Python 3.9 installed on your system.
2. Navigate to the root folder and in your terminal, run ``python3 build.py``. This will begin a process to install all of the neccesary libraries and will give you the option to create a standalone executable or just run the code with Python.

## macOS

1. Make sure you have Python 3.8 or 3.9 installed on your system.
2. Navigate to the root folder and in your terminal, run ``python3 build.py``. This will install all of the neccesary libraries and will give you the option to create a standalone executable or just run the code with Python.
