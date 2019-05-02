#
# main.py - main file for Environment Installer
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


# import needed modules
import os
import sys
# from Scripts.bcolors import bcolors
from system_info import system_info
from main_installer import install_env
system_info()

# bc = bcolors()
print(sys.argv)
# bc.test()

# pip install colorama

# x = int( sys.argv[1] )
# y = int( sys.argv[2] )


# if (sys.version_info > (3, 0)):
if sys.hexversion >= 0x3000000:
    try:
        # Launch main installer
        install_env()
        # os.system("main_installer.py")
        print("Script done ! ^^")

        sys.exit()
    except AttributeError:
        print("Error, Script failed")
    # os.system("pause")
else:
    print("Error, please use python 3.X instead of python 2.X")
