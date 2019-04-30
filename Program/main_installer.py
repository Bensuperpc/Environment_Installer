import ctypes
import os
import platform
from Repair_KDE import install_KDE, remove_KDE

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

if platform.system() == 'Linux':
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    # print('Run in Admin :', end='')
    print(is_admin)
elif platform.system() == 'Windows':
    choice = "0"
    while choice != "q":
        print("Main menu: Choose 1 of 5 choices")
        print("Choose 1 for update system")
        print("Choose 2 for repair broken packages")
        print("Choose 3 for repair KDE")
        print("Choose 4 Grub config")
        print("Choose 5 for install Dev environment")
        print("tape 'q' for leave this menu")
        choice = input("Please make a choice and press Enter: ")

        if choice == "1":  # Menu #1
            # os.system("update_system.py")
            install_KDE()
            remove_KDE()
        elif choice == "2":  # Menu #1:
            os.system('sudo apt --fix-broken install -y')
        elif choice == "3":  # Menu #1:
            os.system("Repair_KDE.py")
        elif choice == "4":  # Menu #1:4
            os.system('sudo add-apt-repository ppa:kubuntu-ppa/backports -y')
            os.system('sudo apt update && sudo apt dist-upgrade -y')
        elif choice == "5":  # Menu #1:5
            print("Second Menu: Choose 1 of 5 choices")
            print("Choose 1 for install Desktop software(QT,Kdenlive...)")
            print("Choose 2 for install Desktop software lite")
            print("Choose 3 for install WordPress Server software")
            print("Choose 4 for install software on Desktop(QT,Kdenlive...)")
            print("Choose 5 for install software on Desktop(QT,Kdenlive...)")
            print("tape 'q' for leave this menu")

            choice1 = input("Please make a choice: ")
            if choice1 == "1":
                os.system('sudo apt install build-essential -y')
            elif choice1 == "2":
                print("Do Something 4")
            elif choice1 == "3":
                print("Do Something 4")
            elif choice1 == "4":
                print("Do Something 4")

        elif choice == "q":  # Menu #1
            print("Leave this menu...")
        else:
            print("Sorry, i don't understand your choice :/")
else:
    print('UnKnow OS')
