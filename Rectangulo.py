import sympy as sp

x,y = sp.symbols('x y')
def rectangulo(ecuacion, inferior, superior, numeroIteraciones):
    global suma, suma2, funcion
    suma= 0
    suma2= 0


    str_ecuacion = ecuacion
    funcion = sp.sympify(str_ecuacion)
    sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)', aspect_ratio = 'auto')
    a = float(inferior)
    b = float(superior)
    NumeroDeIteracciones = int(numeroIteraciones)
    Dx = (b-a)/NumeroDeIteracciones

    for i in range (NumeroDeIteracciones):
        c= a+Dx/2 
        Altura = f(c)
        area = Dx* Altura
        suma = suma + area
        a= a + Dx
    for i in range (NumeroDeIteracciones):
        c2= b+Dx/2 
        Altura2 = f(c2)
        area2 = Dx* Altura2
        suma2 = suma2 + area2
        b= b + Dx





def f(x):
	b = funcion.free_symbols
	var = b.pop()
	valor = funcion.evalf(subs = {var:x})
	return valor



    
