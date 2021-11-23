# Docker-Apps
Run Apps in Arch-Linux based Containers.

## Prerequirements

Existing Arch-Linux Image in Docker

* docker pull archlinux/archlinux

Server access control program for Xorg
* xhost


## How to use

### dockerbuild.sh
Run **dockerbuild.sh** to create new Docker Container
This will also create an **.dockerapps** config Folder into your **$HOME** directory.
This folder is used to make the containered app persistent.
Not every app is using this folder. 
  * Example: **gnome-sound-recorder** - is not using this folder
  * Example: **firefox** is using this folder

### start.sh
Run **start.sh** to run the containered application.
The server access control program **xhost** is used to connect to the container.
  * You may need to install **xhost**.
  * If you use Arch Linux install **xorg-xhost** package

### install.sh
Run **install.sh** to copy an **.desktop** file and a modified version of **start.sh** to you System.
This will made it possible to start the Application from you **GUI-Menu**
After installing you can also start the Container from terminal with **dockerapps-programmname**


## Notes

Librewolf is an example how to create an app with an **AUR PKGBUILD** file.
