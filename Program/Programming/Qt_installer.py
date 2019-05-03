#
#
# Qt_installer.py - Commands for KDE env
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


class Qt_installer:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"
    name = ""

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def Qt_installer():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("Remove KDE...")
            os.system('sudo apt-get install libfontconfig1 -y')
            os.system('sudo apt-get install mesa-common-dev -y')
            os.system('sudo apt-get install libglu1-mesa-dev -y')
            os.system('sudo apt-get install cmake -y')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "Qt_installer"


if __name__ == '__main__':
    objName = Qt_installer()
    print(objName.class_version())
    # objName.install_KDE()
