FROM  archlinux/archlinux:base
RUN pacman -Syu
RUN pacman -S --noconfirm base-devel
RUN pacman -S --noconfirm pulseaudio 
RUN pacman -S --noconfirm xorg-xauth
RUN pacman -S --noconfirm git

RUN useradd -ms /bin/bash user
RUN su - user -c "git clone https://aur.archlinux.org/librewolf.git"
RUN source /home/user/librewolf/PKGBUILD && pacman -Syu --noconfirm --needed --asdeps "${makedepends[@]}" "${depends[@]}"
RUN su - user -c "cd /home/user/librewolf; makepkg -s --noconfirm"
RUN pacman -U --noconfirm /home/user/librewolf/librewolf*.pkg.tar.zst 

RUN pacman -S --noconfirm xorg-xhost
RUN chown -R user /home/user

USER user
EXPOSE 8887
CMD librewolf
