#!/bin/bash
NAME=dockerapps-gnome-sound-recorder

if [ "$1" = "-u" ]; then
	echo Uninstalling $NAME...
	rm /bin/$NAME
	rm /usr/share/applications/$NAME.desktop
	exit
fi

echo Installing $NAME...
cp ./src/$NAME /bin
cp ./src/$NAME.desktop /usr/share/applications

echo Use \"install.sh -u\" to uninstall $NAME
