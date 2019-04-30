

import os


def update_system():
    print("Update system...")
    os.system('sudo apt-get update')
    os.system('sudo apt-get dist-upgrade -y')
