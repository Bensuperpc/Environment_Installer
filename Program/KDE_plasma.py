#
#
# KDE_plasma.py - Commands for KDE env
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


class KDE_plasma:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"
    name = ""

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def remove_KDE():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("Remove KDE...")
            os.system('sudo apt-get purge kubuntu-desktop -y')
            os.system('sudo apt-get purge sddm-theme-breeze -y')
        else:
            print("Wrong OS Only for Linux !")

    def install_KDE():
        if platform.system() == 'Linux':
            print("Install KDE...")
            os.system('sudo apt-get install sddm-theme-breeze -y')
            os.system('sudo apt-get install kubuntu-desktop -y')
        else:
            print("Wrong OS Only for Linux !")

    def install_last_KDE():
        if platform.system() == 'Linux':
            print("Install KDE...")
            os.system('sudo add-apt-repository ppa:kubuntu-ppa/backports -y')
            os.system('sudo apt update && sudo apt dist-upgrade -y')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "KDE"


if __name__ == '__main__':
    objName = KDE_plasma()
    print(objName.class_version())
    # objName.install_KDE()
