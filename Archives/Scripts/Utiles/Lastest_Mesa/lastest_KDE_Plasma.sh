#!/bin/sh
sudo add-apt-repository ppa:ubuntu-x-swat/updates -y
sudo apt-get dist-upgrade
glxinfo | grep "OpenGL version"

#sudo apt-get install ppa-purge && sudo ppa-purge ppa:ubuntu-x-swat/updates