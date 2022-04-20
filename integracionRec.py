pi = 3.14159265358979
#intervalo izquierdo y derecho
ci = 0.0
cf = 150.0
###
intv = 5
paso = (cf - ci)/intv
suma = 0.0
x = ci
#def de f(x)
def funx(x):
        from math import sqrt, cos, sin
        return sqrt(1+(3*cos(x))**2)
#####
#Bucle
while 1e-5 < abs(cf-x):
        y = funx(x)
        print ("%5.10f" %x," |","%5.10f" %y)
        x = x + paso
        #Cond. de int. por trapecios
        if x == ci or x == cf +- 1e-5:
                suma = suma+y
        else:
                suma = suma+2*y
#Fin bucle
resultado = suma*paso/2
print ("El resultado de la integral es %5.10f" %resultado)