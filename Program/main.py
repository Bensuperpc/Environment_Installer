#
# main.py - main file for Environment Installer
#
# Created by Benoît(Bensuperpc@gmail.com) 30, April of 2019
# Updated by Benoît(Bensuperpc@gmail.com) for arduino 1.8.6 and newer (Not tested with previous versions)
# Released into the Public domain with MIT licence : https://opensource.org/licenses/MIT
#
# Use Sublime text 3 and python 3.7.3
# Script compatibility : Windows, Linux, Mac
#
# ==============================================================================


# import needed modules
import os
import sys
from Scripts.bcolors import bcolors
from system_info import system_info
system_info()

bc = bcolors()
print(sys.argv)

# pip install colorama

#x = int( sys.argv[1] )
#y = int( sys.argv[2] )


try:
        # Launch main installer
    os.system("main_installer.py")
    print("Script done ! ^^")
except AttributeError:
    print("Error, Script failed")
os.system("pause")
