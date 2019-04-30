import os


def remove_KDE():
    '''
    Sert à supprimer kde'''
    print("Remove KDE...")
    os.system('sudo apt-get purge kubuntu-desktop -y')
    os.system('sudo apt-get purge sddm-theme-breeze -y')


def install_KDE():
    print("Install KDE...")
    os.system('sudo apt-get install sddm-theme-breeze -y')
    os.system('sudo apt-get install kubuntu-desktop -y')
