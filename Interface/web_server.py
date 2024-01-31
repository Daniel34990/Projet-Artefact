# Importation du module Flask
from flask import Flask, render_template
from commandes import forward, left, right, backward

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Définition de la route principale ('/') qui renvoie la page HTML avec les boutons
@app.route('/')
def index():
    return render_template('index.html')

# Définition de fonctions à exécuter pour chaque bouton
def fonction_haut():
    left(0.4,0.5)
    print("Bouton Haut pressé")
    # Ajoutez ici le code spécifique pour le bouton Haut

def fonction_bas():
    right(0.4,0.5)
    print("Bouton Bas pressé")
    # Ajoutez ici le code spécifique pour le bouton Bas

def fonction_gauche():
    forward(0.4,0.4,0.5)
    print("Bouton Gauche pressé")
    # Ajoutez ici le code spécifique pour le bouton Gauche

def fonction_droite():
    backward(0.4,0.4,0.5)
    print("Bouton Droite pressé")
    # Ajoutez ici le code spécifique pour le bouton Droite

# Définition de routes pour les fonctions des boutons
@app.route('/haut')
def bouton_haut():
    fonction_haut()
    return 'OK'

@app.route('/bas')
def bouton_bas():
    fonction_bas()
    return 'OK'

@app.route('/gauche')
def bouton_gauche():
    fonction_gauche()
    return 'OK'

@app.route('/droite')
def bouton_droite():
    fonction_droite()
    return 'OK'

# Vérification si le script est exécuté directement
if __name__ == '__main__':
    # Lancement de l'application Flask en mode débogage
    app.run(host='0.0.0.0',port=5000)
