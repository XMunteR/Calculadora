from distutils.log import error
from math import*
from sympy import*
from numpy import*
import numpy as np
import sympy as sp
from random import *

f = ""
x = symbols('x')
print
print ("Super calculo de integrales simples con metodo del trapecio c:")
print
f = input("Ingrese su funcion en terminos de x:\n") #Coje el string donde se escribe la funcino
print
funcion = sympify(f) #convierte el string en una expresion literal f(x)
a = int (input("Ingrese su parametro inicial:\n"))
b = int (input("Ingrese su parametro final:\n"))
m = int (input("Ingrese el numero de particiones\n"))

derivada1 = sp.diff(funcion)
derivada2 = sp.diff(derivada1)

def trapecios(funcion,a,b,m):
    h = (b-a)/float(m)
    s = 0
    n = 0
    a_evaluado = 0
    b_evaluado = 0

    for i in range(1,m):
        n = a + (i*h)
        n_evaluado = funcion.evalf(subs = {"x" : n}) #evalua n en la funcion descrita
        s = s + n_evaluado

    a_evaluado = funcion.evalf(subs = {"x" : a}) #evalua a en la funcion descrita, lo mismo con b en la siguiente linea
    b_evaluado = funcion.evalf(subs = {"x" : b})
    resul = h/2 * (a_evaluado + 2*s + b_evaluado)

    
    return resul

Error = 0
h=(b-a)/m
n = np.random.uniform(a,b+1)
z = float(a+(n*a-b))
Error = -(((h)**3/12)*(derivada2*(z)))

print (trapecios(funcion,a,b,m))

print ("error: ", Error)










