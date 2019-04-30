#!/bin/bash
if ! [ $(id -u) = 0 ]; then #si le programme n'est pas exécuté en mode Super Utilisateur
echo " \033[31m#####################################################################\033[0m"
echo "  \033[31m|   Ce Script est à éxécuter en mode Super Utilateur:             |\033[0m"
echo "  \033[31m|   il faut éxécuter cette commande:                              |\033[0m"
echo "  \033[31m|   ' \033[37msudo sh ~/${0}\033[0m \033[31m'|\033[0m"
echo "  \033[31m|   Puis tapez votre Mot de passe Administrateur                  |\033[0m"
echo " \033[31m#####################################################################\033[0m"
sleep 6s
   exit 1
   else
fct_menu ()
    {
    echo "  ==================================================" 
    echo "  Choisir une Option Pour Cron et la tocuhe 'Entre'"
    echo
    echo "  1 : Installation clean PC/Serveur"
    echo "  2 : Mettre à jour les paquets"
    echo "  3 : Réparer les paquets cassés"
    echo "  4 : Installation de KDE"
    echo "  5 : Déinstaller paquets/pilotes de Nvidia"
    echo "  6 : 6"
    echo
    echo "  Q ou q: Quitter le Script"
    echo
    echo "  Choix : "
    echo "  =================================================="

    read optionmenu
        case $optionmenu in
        1)

	fct_menu ()
		{
		echo "  ==================================================" 
		echo "  Choisir une Option et la tocuhe 'Entre'"
		echo
		echo "  1 : Installation clean PC/Serveur"
		echo "  2 : Mettre à jour les paquets"
		echo "  3 : Réparer les paquets cassés"
		echo "  4 : Installation de KDE"
		echo "  5 : Déinstaller paquets/pilotes de Nvidia"
		echo "  6 : 6"
		echo
		echo "  Q ou q: Quitter le Script"
		echo
		echo "  Choix : "
		echo "  =================================================="

		read optionmenu
			case $optionmenu in
			1)
				echo "  =========================="
				echo "  PC Install clean"
				echo "  =========================="
				sudo apt-get update
				sudo apt-get dist-upgrade
				#Install de l'environement de programmation
				sudo apt-get install build-essential -y
				#-----GCC-----
				sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
				sudo apt-get update
				sudo apt-get install gcc-8 g++-8 -y
				#-----Kdevelop-----
				sudo apt-get install kdevelop -y
				#Install des logiciels Mulimedia
				sudo apt-get install kdenlive -y
				sudo apt-get install frei0r-plugin -y
				sudo apt-get install vlc -y
				#Install des logiciels photos
				sudo apt-add-repository ppa:otto-kesselgulasch/gimp -y
				sudo apt-get update
				sudo apt-get install gimp -y
				sudo apt-add-repository ppa:inkscape.dev/stable -y
				sudo apt-get update
				sudo apt-get install inkscape -y
				
				#-----Librairies de Qt-----
				sudo apt-get install libfontconfig1 -y
				sudo apt-get install mesa-common-dev -y
				sudo apt-get install libglu1-mesa-dev -y
				sudo apt-get install cmake -y
				#-----Logiciels Utiles-----
				sudo apt-get install exfat-utils -y
				sudo apt-add-repository ppa:cubic-wizard/release -y
				sudo apt-get update
				sudo apt install cubic -y
				#-----flatpak-----
				sudo add-apt-repository ppa:alexlarsson/flatpak -y
				sudo apt-get update
				sudo apt install flatpak -y
				sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
				sudo apt install plasma-discover-flatpak-backend
				sudo add-apt-repository ppa:kubuntu-ppa/backports -y
				sudo apt update && sudo apt dist-upgrade
				sudo sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
				#wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
				#sudo apt-get update
				#sudo apt-get install google-chrome-stable
				
				
				fct_menu;;
			2)
				echo "  =========================="
				echo "  Mise à jour des paquets"
				echo "  =========================="
				sudo apt-get update && sudo apt-get dist-upgrade;
				sudo apt-get autoremove;
				fct_menu;;
			3)
				echo "  =========================="
				echo "  Réparation des paquets cassés"
				echo "  =========================="
				sudo apt --fix-broken install ; 
				fct_menu;;
			4)
				echo "  =========================="
				echo "  Réparation de KDE"
				echo "  =========================="
				echo "suppression de KDE dans 6 Sec"
				echo "Ctrl+C pour annuler"
				sleep 6s
				#suppression de KDE
				#sudo apt-get purge kubuntu-desktop -y
				#sudo apt-get purge sddm-theme-breeze -y
				
				#Installation de KDE
				#sudo apt-get install sddm-theme-breeze -y
				#sudo apt-get install kubuntu-desktop -y
				echo "Reboot dans 6 Sec"
				echo "Ctrl+C pour annuler"
				sleep 6s
				#sudo reboot now
				fct_menu;;
			5)
				echo "  =========================="
				echo "  lancement de la 5"
				echo "  =========================="
				
				fct_menu;;
			6)
				echo
				echo "lancement de la 6"
				echo
				mplayer -playlist 6 ; 
				fct_menu;;
			Q) 
				exit;;
			q) 
				exit;;
			*)
				echo
				echo "erreur de frappe"
				echo
				fct_menu;;
				esac
		}

            fct_menu;;
        2)
            echo "  =========================="
            echo "  Mise à jour des paquets"
            echo "  =========================="
            sudo apt-get update && sudo apt-get dist-upgrade;
            sudo apt-get autoremove;
            fct_menu;;
        3)
            echo "  =========================="
            echo "  Réparation des paquets cassés"
            echo "  =========================="
            sudo apt --fix-broken install ; 
            fct_menu;;
        4)
            echo "  =========================="
            echo "  Réparation de KDE"
            echo "  =========================="
            echo "suppression de KDE dans 6 Sec"
            echo "Ctrl+C pour annuler"
            sleep 6s
            #suppression de KDE
            #sudo apt-get purge kubuntu-desktop -y
            #sudo apt-get purge sddm-theme-breeze -y
            
            #Installation de KDE
            #sudo apt-get install sddm-theme-breeze -y
            #sudo apt-get install kubuntu-desktop -y
			
            echo "Reboot dans 6 Sec"
            echo "Ctrl+C pour annuler"
            sleep 6s
            #sudo reboot now
            fct_menu;;
        5)
            echo "  =========================="
            echo "  lancement de la 5"
            echo "  =========================="
            
            fct_menu;;
        6)
            echo
            echo "lancement de la 6"
            echo
            mplayer -playlist 6 ; 
            fct_menu;;
        Q) 
            exit;;
        q) 
            exit;;
        *)
            echo
            echo "erreur de frappe"
            echo
            fct_menu;;
            esac
    }
fct_menu;#Retour au menu
fi
#sudo add-apt-repository ppa:kubuntu-ppa/backports
#sudo apt update && sudo apt dist-upgrade



#https://forum.ubuntu-fr.org/viewtopic.php?id=2029590
