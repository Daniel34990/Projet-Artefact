import cv2
import cv2.aruco as aruco
from math import *
# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Créer les paramètres du détecteur ARUCO
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)


def impair():
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)

    # Lire le cadre de la caméra
    ret, frame = cap.read()
    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    if len(corners) > 0:
        
        for markerCorner in corners:
            if ids%2==0:
                
                return True
        
    
    return False

impair()
