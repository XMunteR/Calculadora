import matplotlib
from matplotlib import pyplot as plt
import sympy as sp
import matplotlib as plt

x,y = sp.symbols('x y')

def funcion(ecuacion):
    global funcion
    funcion = sp.sympify(ecuacion)
    sp.plot(funcion, (x, -20, 20), title = 'Grafica', aspect_ratio = 'auto')

