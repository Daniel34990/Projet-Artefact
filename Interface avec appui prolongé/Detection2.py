from commandes import forward,time, right, left
from detect import pair, impair, distance


def Parcoursauto():
    left(0.7,3.7)


def Parcoursauto1():
    duree_execution = 1
    v=False
    a=0
    forward(-0.4,-0.4,0.9)
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if impair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)
    v=False
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if impair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)
    v=False
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if impair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)

    v=False
    time.sleep(2)
    forward(0.4,0.4,0.7)
    time.sleep(1)
    forward(0.52,-0.5,4)

    
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if pair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)
    v=False
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if pair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)
    v=False
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if pair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*0.8)
    v=False
    while not v:
        temps_debut = time.time()
        while (time.time() - temps_debut) < duree_execution:
            if pair():
                v=True
                a=distance()
                break
        if v==False:
            forward(0.4,0.4,0.1)
    forward(0.52,-0.5,a/100*1.2)
    v=False