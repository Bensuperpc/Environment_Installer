#
#
# system_info.py - Get system info
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


class system_info:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def system_info():
        if platform.system() == 'Linux':
            print(platform.system(), end=' ')  # Linux/Darwin/Windows
            print(platform.release(), end=' ')  # 2.6.22-15-generic€
            print(platform.architecture(), end=' ')
            print(platform.dist(), end=' ')
            print(sys.version, end=' ')
            print(sys.version_info, end=' ')
            print("the script has the name %s" % (sys.argv[0]))
            print(os.name, end=' ')  # nt/ls

            if sys.hexversion >= 0x3000000:
                # Python 3 code in this block
                print('Python 3.x hexversion %s is in use.' %
                      hex(sys.hexversion))
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "KDE"


if __name__ == '__main__':
    objName = system_info()
    print("Lib Version : " + objName.class_version())
    # count the arguments
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

    # objName.install_KDE()
