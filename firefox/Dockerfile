FROM  archlinux/archlinux:base
RUN pacman -Syu
RUN pacman -S --noconfirm pulseaudio 
RUN pacman -S --noconfirm xorg-xauth
RUN pacman -S --noconfirm firefox

RUN useradd -ms /bin/bash user

USER user
EXPOSE 8887
CMD firefox 
