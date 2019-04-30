#!/bin/sh
echo "Disable Nouveau Driver with blacklist" 
sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nouveau.conf"
sudo update-initramfs -u

echo "Disable Nouveau Driver in Grub" 
sudo mv /etc/default/grub /etc/default/grub.back
sudo sed -i 's/^\(GRUB_CMDLINE_LINUX_DEFAULT=.*\)"$#\1 nouveau.modeset=0"#' /etc/default/grub
sudo update-grub

read -p "Voulez-vous redemarer pour activer les modifications ?" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    sudo reboot now
fi
