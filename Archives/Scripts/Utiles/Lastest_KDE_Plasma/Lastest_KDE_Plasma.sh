#!/bin/sh
sudo add-apt-repository ppa:kubuntu-ppa/backports
sudo apt update && sudo apt dist-upgrade
sudo reboot now