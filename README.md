
Prerequirements

Existing Arch-Linux Image in Docker

docker pull archlinux/archlinux


Do run Docker as non-root user run:

sudo groupadd docker

sudo usermod -aG docker $USER

newgrp docker
