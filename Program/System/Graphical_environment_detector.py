#
#
# Graphical_environment_detector.py - get current name of graphical env
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

# https://stackoverflow.com/questions/14768162/get-the-return-value-from-a-function-in-a-class-in-python

import os
import platform
import sys


class GED:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"
    name = ""

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel

    def detect_desktop_environment(self):
        desktop_environment = ''

        if os.environ.get('KDE_FULL_SESSION') == 'true':
            desktop_environment = 'kde'
        elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            desktop_environment = 'gnome'
        else:
            if platform.system() == 'Windows':
                desktop_environment = 'Windows'
            else:
                desktop_environment = 'unknown desktop environment'
        # System.getenv("XDG_CURRENT_DESKTOP")
        return desktop_environment

    def __init__(self):
        self.name = ""


if __name__ == '__main__':
    objName = GED()
    print(objName.class_version())
    print(sys.argv[0])
    objName.detect_desktop_environment()
    # objName.install_KDE()
