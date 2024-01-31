from flask import Flask, render_template, request
from commandes import run, stop_tot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_position', methods=['POST'])
def update_position():
    position_x = request.form['x']
    position_y = request.form['y']
    max_value = 40  # Valeur maximale de la plage actuelle
    normalized_max_value = 1  # Valeur maximale de la nouvelle plage

    # Normalisation des coordonnées
    position_x_norm = (position_x / max_value) * normalized_max_value
    position_y_norm = (position_y / max_value) * normalized_max_value

    run(position_y_norm,position_x_norm)
    
    # Fais quelque chose avec la position du joystick
    # Peut-être appeler une fonction Python avec ces valeurs
    print(f"Position X: {position_x}, Position Y: {position_y}")
    return 'Position mise à jour'

@app.route('/stop_joystick', methods=['POST'])
def stop_joystick():
    stop_tot()
    # Appeler la fonction "stop" ou réaliser toute autre logique nécessaire lorsque l'utilisateur lâche le joystick
    print("Joystick relâché")
    # Ici, tu peux exécuter la fonction Python associée à l'arrêt du joystick
    return 'Joystick arrêté'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
