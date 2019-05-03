#
#
# Android_Studio.py - Get system info
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

# http://tvaira.free.fr/projets/activites/qt-android-installation.html
# https://doc.qt.io/qt-5/android-getting-started.html
# https://stackoverflow.com/questions/1078524/how-to-specify-the-location-with-wget
# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python

import platform
import os  # We need this module
import sys
# import lsb_release


class Android_Studio:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def Android_Studio():
        if platform.system() == 'Linux':
            # Install needed packages
            os.system(
                'sudo apt-get install libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 -y')
            os.system('sudo apt-get install libsdl1.2debian:i386 -y')

            # Download
            os.system(
                'wget https://dl.google.com/dl/android/studio/ide-zips/3.4.0.18/android-studio-ide-183.5452501-linux.tar.gz -P')
            os.system(
                'wget https://dl.google.com/android/repository/android-ndk-r20-beta2-linux-x86_64.zip -P')

            # wget <file.ext> -O /path/to/folder/file.ext
            # https://dl.google.com/android/repository/android-ndk-r20-beta2-linux-x86_64.zip
            # https://dl.google.com/android/repository/android-ndk-r19c-linux-x86_64.zip
            # https://dl.google.com/dl/android/studio/ide-zips/3.4.0.18/android-studio-ide-183.5452501-linux.tar.gz
            # sudo apt-get install openjdk-8-jre

        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "Android_Studio"


if __name__ == '__main__':
    objName = Android_Studio()
    print("Lib Version : " + objName.class_version())
    # count the arguments
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

    # objName.install_KDE()
