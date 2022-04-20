import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# INGRESO
x,y = sp.symbols('x, y')
def ecuacion(ecuacion,izquierdo,derecho,particiones):
    global funcion, a, b, tramos
    a = izquierdo
    b = derecho
    tramos = particiones
    funcion = sp.sympify(ecuacion)
    sp.plot(funcion, (x, -10, 10), title = 'Trapecio', aspect_ratio='auto')
    return (integTrap(a, b, tramos))

def f(x):
    b = funcion.free_symbols
    var = b.pop()
    valor = funcion.evalf(subs = {var:x})
    return valor

# PROCEDIMIENTO
def integTrap(a, b, tramos):
    global area, error
    h = (b-a)/tramos
    xi = a
    suma = f(xi)
    for i in range(0,tramos-1,1):
        xi = xi + h
        suma = suma + 2*f(xi)
    suma = suma + f(b)
    area = h*(suma/2)
    vt = np.exp(np.pi) / 2 + 1 / 2
    error = abs((vt - suma) / vt) * 100
    print("Error %: ", error)

    #error = "aqui va el error"
    # SALIDA
    print('tramos: ', tramos)
    print('Integral: ', area)

    return "#"