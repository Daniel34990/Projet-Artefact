from commandes1 import forward, backward, left, right, stop_tot
from flask import Flask, render_template, send_file
from Detection2 import Parcoursauto
from Test2 import debug_image
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<direction>')
def move(direction):
    # Fonctions spécifiques à chaque direction
    if direction == 'up':
        forward(0.52,0.5)
        # Fonction pour déplacer vers le haut
        print("Déplacement vers le haut")
        # Ajoutez ici votre code pour le déplacement vers le haut

    elif direction == 'down':
        backward(0.52,0.5)
        # Fonction pour déplacer vers le bas
        print("Déplacement vers le bas")
        # Ajoutez ici votre code pour le déplacement vers le bas

    elif direction == 'left':
        left(0.5)
        # Fonction pour déplacer vers la gauche
        print("Déplacement vers la gauche")
        # Ajoutez ici votre code pour le déplacement vers la gauche

    elif direction == 'right':
        right(0.5)
        # Fonction pour déplacer vers la droite
        print("Déplacement vers la droite")
        # Ajoutez ici votre code pour le déplacement vers la droite
    return 'OK'

@app.route('/stop/<direction>')
def stop(direction):
    stop_tot()
    return 'OK'

@app.route('/parcours_auto')
def parcours_automatique():
    Parcoursauto()
    return 'OK'

@app.route('/genere_image')
def genere_image():
    debug_image()
    return 'OK'

@app.route('/arret_robot')
def arret_robot():
    stop_tot()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
