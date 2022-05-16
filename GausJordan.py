import numpy as np
import sys
def GaussJordan2x3(num1,num2,num4,num5,ind1,ind2):
    global result2x2
    n = 2
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = ind1

    a[1][0] = num4
    a[1][1] = num5
    a[1][2] = ind2

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Error...Division por cero')

        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n):
     x[i] = a[i][n]/a[i][i]

    #Para imprimir colocar
    arreglo=[]
    for i in range(n):
     result = ('X%d = %0.5f' %(i,x[i]))
     arreglo.append(str(result))
     
    result2x2 = arreglo[0:2]
    return result2x2