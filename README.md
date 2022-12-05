<p align="center">
<img width="460" height="300" src="https://user-images.githubusercontent.com/34868944/205726457-355d7d05-63c5-4695-bf15-0172d5f67926.png"></img>
</p>
   
## _Contents_
* [Why SkiffUI](https://github.com/Gameplex-Software/SkiffUI/#why-use-skiffui)
* [How it works](https://github.com/Gameplex-Software/SkiffUI/#how-it-works)
* [Installation](https://github.com/Gameplex-Software/SkiffUI/#installation)
    * [Stable](https://github.com/Gameplex-Software/SkiffUI/#latest-stable)
        * [Windows]()
        * [Mac](https://github.com/Gameplex-Software/SkiffUI/#macos)
        * [Linux](https://github.com/Gameplex-Software/SkiffUI/#linux)
    * [Beta](https://github.com/Gameplex-Software/SkiffUI/#latest-beta)
        * [Windows]()
        * [Mac](https://github.com/Gameplex-Software/SkiffUI/#macos-1)
        * [Linux](https://github.com/Gameplex-Software/SkiffUI/#linux-1)


# The worlds first container network manager
Development is a work in progress, please follow us on social media for updates (socials are in the footer of our website)
  
## Why Use SkiffUI
SkiffUI provides the first easy to use, Drag-and-Drop user interface for modifying, or networking containers after creation. SkiffUI currently supports only Docker but could easily be expanded to interact with Docker Swarms and Kubernetes clusters later on.

## How it works
SkiffUI interacts with docker by converting graphical node data into commands for your container service, these commands are then executed as root on the host.

## Future plans for SkiffUI
- Integration with Kubernetes
- Integration with Docker Swarm
- GUI based container generator (drag software into container from a toolbox to generate a docker image)
- Remote system connection via SSH

[Visit our company website](https://gameplexsoftware.com)

[SkiffUI Website](https://skiffdev.gameplexsoftware.com)

# Sketch for Version 2.0!
![SkiffUI drawio](https://user-images.githubusercontent.com/34868944/152663999-d0b31fe7-ea31-44b4-ab12-3b73e9e6d9b9.png)

# Installation

## Latest Stable

### Linux
```
sudo sh get.docker.com
docker run -p 8443:8443 -p 1027:1027 gameplexsoftware/skiffui
```

### MacOS
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew cask install docker
docker run -p 8443:8443 -p 1027:1027 gameplexsoftware/skiffui
```

## Latest Beta

### Linux
```
sudo sh get.docker.com
mkdir ./SkiffUI
git clone https://github.com/Gameplex-Software/SkiffUI/blob/master/app/services.sh
cd ./skiffui/
docker build .
docker-compose up -d
```

### MacOS
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew cask install docker
mkdir ./SkiffUI
git clone https://github.com/Gameplex-Software/SkiffUI/blob/master/app/services.sh
cd ./skiffui/
docker build .
docker-compose up -d
```
