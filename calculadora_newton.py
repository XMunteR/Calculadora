import sympy as sp

x,y = sp.symbols('x y')
x0 = 0
tolerancia = 0

def newtonR(str_ecuacion, puntoInicio, toler):
    global funcion, x0, tolerancia
    x0 = puntoInicio
    tolerancia = toler
    funcion = sp.sympify(str_ecuacion)
    sp.plot(funcion, (x, -10, 10), title = 'Newton', aspect_ratio = 'auto')
    return raizR(x0,tolerancia)

""" def grafica():
    sp.plot(funcion,(x, -10, 10), title='Ten en cuenta la(s) raíz(es)', aspect_ratio='auto') """

def f(x):
    b = funcion.free_symbols
    var = b.pop()
    valor = funcion.evalf(subs = {var:x})
    return valor

def Df(x):
    b = funcion.free_symbols
    var = b.pop()
    df = sp.diff(funcion,var)
    valor = df.evalf(subs = {var:x})
    return valor

def raizR(x0,tolerancia):
    global raiz, error,contador
    contador = 0
    result3 = ()
    result2 = []

    result1  = "#     Raiz"

    while (abs(f(x0)) > tolerancia and contador < 1000):

        x1 = x0 - f(x0) / Df(x0)
        x0 = x1


        result2.append(x0)
        contador = contador + 1

    if(contador == 1000):
        print("\nSe ha alcanzado el numero máximo de iteraciones")
        print("Es posible que no hayan raices")
        print("Intenta con otro punto inicial")
    else:
        raiz  = str(x0)
        error = str(abs(f(x0)))
        result3 = (result2[0:3])
        

    return result1,error,contador,result3
