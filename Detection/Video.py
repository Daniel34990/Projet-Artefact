import cv2
import cv2.aruco as aruco

# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# Créer les paramètres du détecteur ARUCO
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
cap = cv2.VideoCapture(0)

while True:
    # Lire le cadre de la caméra
    ret, frame = cap.read()
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    # Dessiner les marqueurs détectés sur l'image
    frame = aruco.drawDetectedMarkers(frame, corners, ids)

    # Afficher l'image résultante
    cv2.imshow('ARUCO Detection', frame)

    # Sortir de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
