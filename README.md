# Warning!: ITS a bit broken and very incomplete, this is in-dev and nothing is for sure, use with care!

<p align=center>
<img width=100% src='https://user-images.githubusercontent.com/34868944/224514426-5096788f-780f-40b5-b391-7697e3e2a237.png'>
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

<video src='https://user-images.githubusercontent.com/34868944/224881139-1548ec4b-c939-4480-854c-ad3d6c7d708d.mp4'></video>



# Installation


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


