import cv2
import cv2.aruco as aruco
from math import *
from datetime import datetime
import os
# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

def debug_image():
    # Créer les paramètres du détecteur ARUCO
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, parameters)
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)
    

    ret, frame = cap.read()

    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    # Dessiner les marqueurs détectés sur l'image
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
        
    nom_fichier = datetime.now().strftime("%Y%m%d%H") + '.png'

    cv2.imwrite(nom_fichier, frame)
    cv2.imshow('ARUCO Detection', frame)

    # Libérer les ressources
    cap.release()



