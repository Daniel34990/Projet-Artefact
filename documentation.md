**Séance 1:**

Constitution des groupes et début de réflexion sur le design du robot. Réalisation de quelques schémas qui ont donné lieu à une première idée de prototypage.


**Séance 2:**

1. Installation de l'OS du Raspberry : 64 bit, Lite

Paramètres :
- Nom Machine : raspberrypi.local
- username SSH : 2d
- pwd : artefact2d

Wireless : Access mobile (Abdennour's iPhone)

Se connecter au RPI via le terminal: ssh 2d@raspberrypi.local

2. Obtention de l'adresse MAC
Commande : ifconfig (l'adresse MAC est précédé par "ether")

Adresses MAC :
- ethernet : d8:3a:dd:29:fe:18
- WLAN : d8:3a:dd:29:fe:19

3. Configuration réseau du RPI

On télécharge le certificat tp-2021.pem et on la dispose dans le dossier /boot du rpi.

Éditeur nano pour la connexion:

cd /etc/wpa.supplicant
sudo nano wpa.supplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

update_config=1

country=FR

network={
    ssid="Campus-Telecom"
    scan_ssid=1
    key_mgmt=WPA-EAP
    ca_cert="/boot/tp-2021.pem"
    eap=TTLS
    identity="robotpi-08.enst.fr"
    password="ENCsJIZ8aeQ9mw"
    phase2="auth=PAP"
}

Commande d'extinction : sudo shutdown -h now


**Séance 3:**

On commence la séance par fixer les objectifs de celle-ci, après lecture du descriptif. 

Les objectifs sont: finir le design du robot, finir l'authentification sur le réseau "campus-télécom" et commencer à travailler sur les tâches qu'on s'est attribué au sein du groupe, toutes les autres étapes étant complétées.


**Séance 4:**

Dessin d'un plan SVG avec Inkscape.

Connexion à campus Télécom.

Synchronisation de l'heure du RPI avec ntp.

Eteindre le RPI: shutdown -h  

Mise à jour des paquets : sudo apt-get upduate
and sudo apt-get dist-upgrade -y

Recherche de documentation pour la mise en route des moteurs: détermination des logiciels à installer et à utiliser, packages de code Python à installer et commencement de l'écriture des premières lignes de code.


**Séance 5:**

Finalisation du design ainsi que du plan SVG à l'aide du logiciel Inskcape. Tout est prêt pour la découpe laser du mercredi 18/10.

Progression dans l'écriture du code destiné à la motorisation du robot.

Commencement de la recherche de documentation pour la mise en place d'une interface pour pouvoir communiquer avec le robot.

Les tâches sont reparties au sein du groupe et chacun progresse dans la partie du projet qu'il lui a été assigné.

Mise en place de la détection video de balises ARUCO via un code en C++.
Pour cela, il faut d'abord installer opencv sur son système:
-via brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
puis: brew install opencv
-via Python: sudo apt-get install python-opencv

**Séance 6:**

Découpe laser du plan SVG et montage du robot. On réussit le montage du premier coup, toutes les mesures ayant été réussies.

Transcription du code C++ de la detection vidéo vers Python. 


**Séance 7:**

Installation des paquets detection ARUCO sur le RaspberryPi:
pip install opencv-python 

**Séance 8:**

Reprogrammation du RPI
Ecriture du script de démarrage.

**Séance 9:**

Installation des paquets sur le RPI:
sudo chmod +x scriptInstallation.sh
./scriptInstallation
Branchement des moteurs.
-Activation du protocole I2C:
sudo raspi config 
enable I2C
sudo chmod 777 -R Motor_Driver_HAT_Code (récuperer le code test des moteurs)

**Séance 10:**

Séance de roulage manuel et automatique pour s'assurer le bon fonctionnement des codes moteurs et de la détection image des balises. Tout est prêt pour la semaine ARTEFACT.

**Semaine ARTEFACT:**

Installation de Tmux pour éviter la perte du robot en cas de perte de la connexion WiFi si connexion via SSH.
Liens explorés: 
- https://github.com/tmux/tmux/wiki
- https://doc.ubuntu-fr.org/tmux

Contrôle manuel réussi 27/11 à 10h (@ tout le groupe)
