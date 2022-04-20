import sympy as sp

x,y = sp.symbols('x y')

def funcion(ecuacion):
    global funcion
    funcion = sp.sympify(ecuacion)
    sp.plot(funcion, (x, -20, 20), title = 'Grafica', aspect_ratio = 'auto')