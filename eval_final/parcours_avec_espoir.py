from commandes import *
from detect import detection, detect_aruco_center
import time

t = {"3pi/4":0.675,"pi/2":0.45,"pi/4":0.225}
t["pi/3"]=0.3
C=[1,0,3,4,2,5]
L=["-3pi/4","pi","3pi/4","pi/4","0","-pi/4"]
D=["3pi/4","pi/2","pi/4"]


def recherche_balise(j):
    i = C.index(j)
    if i<=2:
        left(0.4,t[D[(2-i%3)]])
    else:
        right(0.4,t[D[2-i%3]])
    forward(0.75,0.7,3.7)
    backward(0.75,0.7,3.7)
    if i<=2:
        right(0.4,t[D[(2-i%3)]])
    else:
        left(0.4,t[D[2-i%3]])


j_cur=0
for _ in range(4):
    recherche_balise(j_cur)
    j_cur=(j_cur+2)%6