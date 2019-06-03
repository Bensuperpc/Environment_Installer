#
#
# flatpak.py - flatpak installer
#
# Created by Benoît(Bensuperpc@gmail.com) 30, April of 2019
# Updated by X for python 3.X
#
# Released into the Public domain with MIT licence
# https://opensource.org/licenses/MIT
#
# Written with Sublime text 3 and python 3.7.3
# Script compatibility : Linux (Ubuntu ad debian based)
#
# ==============================================================================


import os
import platform


class flatpak:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"
    name = ""

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def flatpak():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("Remove KDE...")
            os.system('sudo add-apt-repository ppa:alexlarsson/flatpak -y')
            os.system('sudo apt-get update')
            os.system('sudo apt install flatpak -y')
            os.system(
                'sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
            os.system('sudo apt install plasma-discover-flatpak-backend')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "flatpak"


if __name__ == '__main__':
    objName = flatpak()
    print(objName.class_version())
    # objName.install_KDE()
