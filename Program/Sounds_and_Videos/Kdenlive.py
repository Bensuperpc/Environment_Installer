#
#
# Kdenlive.py - Kdenlive installer
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


import platform
import os  # We need this module
import sys
# import lsb_release


class Kdenlive:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def Kdenlive_installer():
        if platform.system() == 'Linux':
            os.system('sudo apt-get install kdenlive -y')
            os.system('sudo apt-get install frei0r-plugin -y')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "KDE"


if __name__ == '__main__':
    objName = Kdenlive()
    print("Lib Version : " + objName.class_version())
    # count the arguments
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

    # objName.install_KDE()
