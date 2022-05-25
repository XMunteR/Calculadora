import numpy as np
import matplotlib.pyplot as plt
import random as rd
from numpy.random import uniform as unif
import sympy 


def f(x):
    return x

def MFuncion(a,b,n):
    global resultado 
    points = n
    internal = a
    external = b
    
    while(points<=1000000):
        x = rd.random()
        y = rd.random() 
        if(y<=f(x)):
            internal = internal + 1
        if(y>f(x)):
            external = external + 1
        points = points + 1
    resultado = internal/(internal+external)
    return resultado
