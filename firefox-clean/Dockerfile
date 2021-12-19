FROM  archlinux/archlinux:base
RUN pacman -Syu
RUN pacman -S --noconfirm firefox

RUN useradd -ms /bin/bash user
RUN chown -R user /home/user
USER user

EXPOSE 8887
CMD firefox
