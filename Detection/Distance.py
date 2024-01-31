import cv2
import cv2.aruco as aruco
from math import *
# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Créer les paramètres du détecteur ARUCO
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)
# Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"La résolution de la vidéo est {width} x {height} pixels.")

while True:
    # Lire le cadre de la caméra
    ret, frame = cap.read()

    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    # Dessiner les marqueurs détectés sur l'image
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    
    if len(corners) > 0:
        for markerCorner in corners:
            # Extrait les cordonnées des coins
            c = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = c
            #Convertit les (x,y) en int
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            #Détermine la longueur des traits verticaux en pixels
            longueur_gauche=bottomLeft[1]-topLeft[1]
            longueur_droite=bottomRight[1]-topRight[1]
            longueur=(longueur_droite+longueur_gauche)/2
            #Calcule la distance avec 682 pixels pour 15 cm de distance (règle de trois)
            distance=15*682/(longueur+0.0001)
            #Affiche les paramètres du marqueurs
            cv2.putText(frame, str(topLeft[0])+','+str(topLeft[1])  , (topLeft[0]-20, topLeft[1]-40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, str(longueur)  , (int(((topLeft[0]+topRight[0]))/2), topLeft[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, str(distance)  , (bottomLeft[0]-20, bottomLeft[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # Afficher l'image résultante
    cv2.imshow('ARUCO Detection', frame)

    # Sortir de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
