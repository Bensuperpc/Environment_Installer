#
#
# install_clang.py - Install clang compiler
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


class install_clang:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def install_clang():
        '''
        Sert à supprimer kde'''
        if platform.system() == 'Linux':
            print("install clang...")
            os.system('sudo apt-get update')
            os.system(
                'sudo apt-add-repository "deb http://apt.llvm.org/disco/ llvm-toolchain-disco-8.0 main"')
            os.system(
                'sudo apt-add-repository "deb http://apt.llvm.org/disco/ llvm-toolchain-disco-7.0 main"')
            os.system('sudo apt-get update')
            os.system('sudo apt-get install -y clang-7.0')
            os.system('sudo apt-get install -y clang-8.0')

            os.system('sudo apt install build-essential -y')

            os.system(
                'sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-8.0 1000')
            os.system(
                'sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 1000')
            os.system("update-alternatives --config clang")
            os.system("update-alternatives --config clang++")
        else:
            print("Wrong OS Only for Linux !")

    def __init__(self):
        self.name = "install_clang"


if __name__ == '__main__':
    objName = install_clang()
    print(objName.class_version())
    # objName.install_KDE()
