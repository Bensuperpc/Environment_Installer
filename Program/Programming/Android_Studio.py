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
# https://wiki.qt.io/Android
# https://stackoverflow.com/questions/1078524/how-to-specify-the-location-with-wget
# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
# https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python
# https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings

import platform
import os  # We need this module
import sys
from pathlib import Path
# import lsb_release


class Android_Studio:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    home = str(Path.home())

    ndkVersion = "r19c"
    sdkBuildToolsVersion = "28.0.3"
    sdkApiLevel = "android-28"
    toolsVersion = "r26.1.1"

    repository = "https://dl.google.com/android/repository"
    toolsFile = "sdk-tools-linux-4333796.zip"
    toolsFolder = "android-sdk-tools"
    ndkFile = "android-ndk-" + ndkVersion + "-linux-x86_64.zip"
    ndkFolder = "android-ndk-" + ndkVersion

    JAVA_HOME = "/usr/lib/jvm/java-8-openjdk-amd64"

    def Android_Studio(self):
        if platform.system() == 'Linux':
            # Install needed packages
            print("Install needed packages...")
            os.system("sudo apt-get install build-essential -y")

            os.system("sudo apt-get install default-jre -y")
            os.system("sudo apt-get install openjdk-8-jdk-headless -y")
            # os.system("sudo apt-get install openjdk-8-jre -y") # Noot needed
            os.system("sudo apt-get install android-sdk -y")
            os.system("sudo apt-get install android-sdk-platform-23 -y")
            os.system("sudo apt-get install libc6-i386 -y")

            os.system("sudo apt-get install libstdc++6:i386 -y")
            os.system("sudo apt-get install libncurses5:i386 -y")
            os.system("sudo apt-get install zlib1g:i386 -y")
            os.system("sudo apt-get install libgcc1:i386 -y")
            os.system("sudo apt-get install libsdl1.2debian:i386 -y")
            print("Install needed packages: OK")
            os.chdir(self.home)
            # Remove old files
            print("Remove :" + self.toolsFolder)
            os.system("rm -rf " + self.toolsFolder)

            # Remove old files
            print("Remove :" + self.home + self.ndkFolder)
            os.system("rm -rf " + self.home + self.ndkFolder)

            print("Downloading SDK tools from :" + self.repository)
            os.system("wget -q " + self.repository + "/" +
                      self.toolsFile + " " + self.home)
            print("Unzip :" + self.sdkFile)
            os.system("unzip -qq $sdkFile")

            print("Downloading NDK from " + self.repository)
            os.system("wget -q " + self.repository + "/" +
                      self.toolsFile + " " + self.home)
            # Unzip files
            print("Unzip :" + self.ndkFile)
            os.system("unzip -qq $ndkFile")

            # Remove unneeded files
            os.system("rm -rf " + self.toolsFile)
            # Remove unneeded files
            os.system("rm -rf " + self.ndkFile)

            os.system("export ")
            os.system("export PATH=$PATH:" + self.JAVA_HOME + "/bin")

            # Remove unneeded files
            print("Installing SDK packages...")
            os.chdir(self.home + self.toolsFolder + "/tools/bin")
            # Optional workaround for issue with certain JDK/JRE versions
            # cp $toolsFolder/tools/bin/sdkmanager $toolsFolder/tools/bin/sdkmanager.backup
            # sed -i 's/^DEFAULT_JVM_OPTS.*/DEFAULT_JVM_OPTS='"'\"-Dcom.android.sdklib.toolsdir=\$APP_HOME\" -XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'"'/' \
            #        $toolsFolder/tools/bin/sdkmanager
            os.system(
                'echo "y" | ./sdkmanager "platforms;$sdkApiLevel" "platform-tools" "build-tools;$sdkBuildToolsVersion" >> sdkmanager.log')
            os.system(
                'echo "y" | ./sdkmanager --install "emulator" >> sdkmanager.log')
            os.system(
                'echo "y" | ./sdkmanager --install "system-images;android-21;google_apis;x86" >> sdkmanager.log')
            os.system(
                'echo "no" | ./avdmanager create avd -n x86emulator -k "system-images;android-21;google_apis;x86" -c 2048M -f >> sdkmanager.log')

            os.system("Here's the list of packages and avd devices:")
            os.system("./sdkmanager --list")
            os.system("./avdmanager list avd")

        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "Android_Studio"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel


if __name__ == '__main__':
    objName = Android_Studio()
    print("Lib Version : " + objName.class_version())
    objName.Android_Studio()
    # count the arguments
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

    # objName.install_KDE()
