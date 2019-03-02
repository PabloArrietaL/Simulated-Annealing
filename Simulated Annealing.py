import template as t
import numpy as np
from math import exp
import random as r

def ObjetiveFunction(pos,matriz):
    z = 0
    for i in range(len(pos)-1):
        z += matriz[pos[i]][pos[i+1]]
    return z

def DisruptMatrix(x):
    x1 = r.randint(1,len(x)-2)
    x2 = r.randint(1,len(x)-2)
    while(x2==x1):
        x2 = r.randint(1,len(x)-2)
    aux = x[x1]
    x[x1] = x[x2]
    x[x2] = aux
    return x

if __name__ == "__main__":
    coor = t.distancesFromCoords()
    x = []
    pos = r.randint(0,len(coor)-1)
    x.append(pos)
    for i in range(len(coor)):
        if(i!=pos):
            x.append(i)
    x.append(pos)
    T = 1000
    alpha = 0.99
    while(T>0.1):
        z = ObjetiveFunction(x,coor)
        new_x = DisruptMatrix(x[:])
        new_z = ObjetiveFunction(new_x,coor)
        if(new_z<z):
            x = new_x
            T *= alpha

        else:
            n = r.random()
            p = exp((-(new_z - z)/T))
            if(n < p):
                x = new_x
                T *= alpha
        print(T)
        print("\n")

    print("Route:",x)
    print("Final distance:",new_z)