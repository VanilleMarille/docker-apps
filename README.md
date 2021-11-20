
Prerequirements

Existing Arch-Linux Image in Docker

See https://wiki.archlinux.org/title/docker#Arch_Linux

Don't use "docker pull archlinux"


Do run Docker as non-root user run:

sudo groupadd docker

sudo usermod -aG docker $USER

newgrp docker
