from distutils.log import error
from numbers import Integral
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x,y = sp.symbols('x, y')

def ecuacion(ecuacion,izquierdo,derecho,particiones):
    global funcion, a, b, tramos
    a = izquierdo
    b = derecho
    tramos = particiones
    funcion = sp.sympify(ecuacion)
    sp.plot(funcion, (x, -10, 10), title = 'Metodo Simpson 3/8', aspect_ratio='auto')
    return (raizsimp(a, b, tramos))

def f(x):
    b = funcion.free_symbols
    var = b.pop()
    valor = funcion.evalf(subs = {var:x})
    return valor

""" def simpson38(f, a, b):
    m1 = (2* a + b) / 3
    m2 = (a + 2 * b) / 3
    integral = (b - a) / 8 * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
    return integral """


""" a = 0
b = np.pi
n = 40 """
def raizsimp(a, b, tramos):
    global suma, errorporcent


    h = (b - a) / tramos
    suma = 0

    for i in range (tramos):
        b = a + h
        m1 = (2* a + b) / 3
        m2 = (a + 2 * b) / 3
        integral = (b - a) / 8 * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
        area = integral
        suma = suma + area
        a = b
    #suma=area
    print(suma)
    vt = np.exp(np.pi) / 2 + 1 / 2
    errorporcent = abs((vt - suma) / vt) * 100
    print("Error %: ", errorporcent)

    return "#"

