xhost +

MYPATH=$(pwd)

docker run -it --rm \
    --device /dev/snd \
    -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
    -e DISPLAY=$DISPLAY \
    --net=host \
    -v $MYPATH/selenium.d/:/opt/selenium.d \
    -v $HOME/.dockerapps/firefox-python-selenium:/root \
    -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
    -v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
    firefox-python-selenium
