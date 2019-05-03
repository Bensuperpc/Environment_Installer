#
#
# KDE.py - Commands for KDE env
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


class install_gcc:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def install_gcc():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("install gcc...")
            os.system('sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y')
            os.system('sudo apt-get update')
            os.system('sudo apt-get install gcc-9 g++-9 -y')
            os.system('sudo apt install build-essential -y')
            os.system(
                'sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-9')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "install_gcc"


if __name__ == '__main__':
    objName = install_gcc()
    print(objName.class_version())
    # objName.install_KDE()
