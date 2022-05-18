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
            result2x2('Error...Division por cero')

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

def GaussJordan3x4(num1,num2,num3,num4,num5,num6,num7,num8,num9,ind1,ind2,ind3):
    global result3x3
    n = 3
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = num3
    a[0][3] = ind1

    a[1][0] = num4
    a[1][1] = num5
    a[1][2] = num6
    a[1][3] = ind2

    a[2][0] = num7
    a[2][1] = num8
    a[2][2] = num9
    a[2][3] = ind3

    for i in range(n):
        if a[i][i] == 0.0:
            result3x3=('Error...Division por cero')

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
     
    result3x3 = arreglo[0:2]
    return result3x3

def GaussJordan4x5(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13
                    ,num14,num15,num16,ind1,ind2,ind3,ind4):
    global result4x4
    n = 4
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = num3
    a[0][3] = num4
    a[0][4] = ind1

    a[1][0] = num5
    a[1][1] = num6
    a[1][2] = num7
    a[1][3] = num8
    a[1][4] = ind2

    a[2][0] = num9
    a[2][1] = num10
    a[2][2] = num11
    a[2][3] = num12
    a[2][4] = ind3

    a[3][0] = num13
    a[3][1] = num14
    a[3][2] = num15
    a[3][3] = num16
    a[3][4] = ind4

    for i in range(n):
        if a[i][i] == 0.0:
            result4x4=('Error...Division por cero')

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
     
    result4x4 = arreglo[0:2]
    return result4x4