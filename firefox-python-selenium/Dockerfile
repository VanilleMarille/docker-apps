FROM  archlinux/archlinux:base
RUN pacman -Syu
RUN pacman -S --noconfirm firefox
RUN pacman -S --noconfirm python geckodriver python-selenium


EXPOSE 8887
CMD /home/user/selenium.d/start.py
