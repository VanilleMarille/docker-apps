FROM  archlinux/archlinux:base
RUN pacman -Syu
RUN pacman -S --noconfirm gnome-sound-recorder

RUN useradd -ms /bin/bash user
RUN chown -R user /home/user

EXPOSE 8887
CMD gnome-sound-recorder
