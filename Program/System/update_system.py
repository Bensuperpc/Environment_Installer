#
#
# update_system.py - Update system
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


class update_system:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def update_system():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("Update system...")
            os.system('sudo apt-get update')
            os.system('sudo apt-get dist-upgrade -y')
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "update_system"


if __name__ == '__main__':
    objName = update_system()
    print(objName.class_version())
    # objName.update_system()
