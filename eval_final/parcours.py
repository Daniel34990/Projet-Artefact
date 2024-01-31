from commandes import *
from detect import detection, detect_aruco_center, distance
import time

j1 = 4
j2 = 6
j3 = 5
I=[j1,j2,j3]

t = {"3pi/4":0.675,"pi/2":0.45,"pi/4":0.225}
t["pi/3"]=0.3
C=[1,2,3,4,0,5]
L=["-3pi/4","pi","3pi/4","pi/4","0","-pi/4"]
D=["3pi/4","pi/2","pi/4"]

def balayage(ti,j):
    left(0.4,ti)
    i=0
    pas=ti/3
    flag=False
    while i < 15:
        temp_debut=time.time()
        while (time.time() - temp_debut)<0.8:
            if detection(j) and (detect_aruco_center(j)-320<50):
                flag=True
                break
        if flag:
            return True
        i+=1
        right(0.4,pas)
    if i>=6:
        left(0.4,ti)
    return False


###########################@

def balayage2(ti,j):
    left(0.4,ti)
    i=0
    pas=0.1
    flag=False
    while i < 20:
        temp_debut=time.time()
        while (time.time() - temp_debut)<0.8:
            if detection(j) and (detect_aruco_center()-320<250):
                flag=True
                break
        if flag:
            return True
        i+=1
        right(0.4,pas)
    if i>=20:
        left(0.4,ti)
    return False

####################################

def reconnaissance(j):
    while True:
        trouve=False
        i=0
        while ((not trouve) and i<100):
            trouve = detection(j)
            left(0.4,0.07)
            i+=1
        if trouve:
            return True
        else: return False

def recherche_balise(j): # Lorsque le robot est a peu près face à la balise
    while True:
        ti=0.07
        trouve=False
        while (not trouve) and (ti<=0.9):
            trouve=balayage(ti,j)
            ti=2*ti
        if not trouve:
            break
        a = distance()
        if a <= 50:
            break
        l = a/100*0.7
        forward(0.75,0.7,l)
    


def parcours():
    forward(0.75,0.7,3.2)
    for i in I:
        if reconnaissance(i):
            recherche_balise(i)
        else:
            continue
        backward(0.75,0.7,3.7)

parcours()
        