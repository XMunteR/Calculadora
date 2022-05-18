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

def GaussJordan5x6(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13
                    ,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,num24
                    ,num25,ind1,ind2,ind3,ind4,ind5):
    global result5x5
    n = 5
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = num3
    a[0][3] = num4
    a[0][4] = num5
    a[0][5] = ind1

    a[1][0] = num6
    a[1][1] = num7
    a[1][2] = num8
    a[1][3] = num9
    a[1][4] = num10
    a[1][5] = ind2

    a[2][0] = num11
    a[2][1] = num12
    a[2][2] = num13
    a[2][3] = num14
    a[2][4] = num15
    a[2][5] = ind3

    a[3][0] = num16
    a[3][1] = num17
    a[3][2] = num18
    a[3][3] = num19
    a[3][4] = num20
    a[3][5] = ind4

    a[4][0] = num21
    a[4][1] = num22
    a[4][2] = num23
    a[4][3] = num24
    a[4][4] = num25
    a[4][5] = ind5

    for i in range(n):
        if a[i][i] == 0.0:
            result5x5=('Error...Division por cero')

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
     
    result5x5 = arreglo[0:2]
    return result5x5

def GaussJordan6x7(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13
                    ,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,num24
                    ,num25,num26,num27,num28,num29,num30,num31,num32,num33,num34
                    ,num35,num36,ind1,ind2,ind3,ind4,ind5,ind6):
    global result6x6
    n = 6
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = num3
    a[0][3] = num4
    a[0][4] = num5
    a[0][5] = num6
    a[0][6] = ind1

    a[1][0] = num7
    a[1][1] = num8
    a[1][2] = num9
    a[1][3] = num10
    a[1][4] = num11
    a[1][5] = num12
    a[1][6] = ind2

    a[2][0] = num13
    a[2][1] = num14
    a[2][2] = num15
    a[2][3] = num16
    a[2][4] = num17
    a[2][5] = num18
    a[2][6] = ind3

    a[3][0] = num19
    a[3][1] = num20
    a[3][2] = num21
    a[3][3] = num22
    a[3][4] = num23
    a[3][5] = num24
    a[3][6] = ind4

    a[4][0] = num25
    a[4][1] = num26
    a[4][2] = num27
    a[4][3] = num28
    a[4][4] = num29
    a[4][5] = num30
    a[4][6] = ind5

    a[5][0] = num31
    a[5][1] = num32
    a[5][2] = num33
    a[5][3] = num34
    a[5][4] = num35
    a[5][5] = num36
    a[5][6] = ind6

    for i in range(n):
        if a[i][i] == 0.0:
            result6x6=('Error...Division por cero')

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
     
    result6x6 = arreglo[0:2]
    return result6x6

def GaussJordan7x8(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13
                    ,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,num24
                    ,num25,num26,num27,num28,num29,num30,num31,num32,num33,num34
                    ,num35,num36,num37,num38,num39,num40,num41,num42,num43,num44,num45
                    ,num46,num47,num48,num49,ind1,ind2,ind3,ind4,ind5,ind6,ind7):
    global result7x7
    n = 7
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    #Ingresar numeros de la matriz
    a[0][0] = num1
    a[0][1] = num2
    a[0][2] = num3
    a[0][3] = num4
    a[0][4] = num5
    a[0][5] = num6
    a[0][6] = num7
    a[0][7] = ind1

    a[1][0] = num8
    a[1][1] = num9
    a[1][2] = num10
    a[1][3] = num11
    a[1][4] = num12
    a[1][5] = num13
    a[1][6] = num14
    a[1][7] = ind2

    a[2][0] = num15
    a[2][1] = num16
    a[2][2] = num17
    a[2][3] = num18
    a[2][4] = num19
    a[2][5] = num20
    a[2][6] = num21
    a[2][7] = ind3

    a[3][0] = num22
    a[3][1] = num23
    a[3][2] = num24
    a[3][3] = num25
    a[3][4] = num26
    a[3][5] = num27
    a[3][6] = num28
    a[3][7] = ind4

    a[4][0] = num29
    a[4][1] = num30
    a[4][2] = num31
    a[4][3] = num32
    a[4][4] = num33
    a[4][5] = num34
    a[4][6] = num35
    a[4][7] = ind5

    a[5][0] = num36
    a[5][1] = num37
    a[5][2] = num38
    a[5][3] = num39
    a[5][4] = num40
    a[5][5] = num41
    a[5][6] = num42
    a[5][7] = ind6

    a[6][0] = num43
    a[6][1] = num44
    a[6][2] = num45
    a[6][3] = num46
    a[6][4] = num47
    a[6][5] = num48
    a[6][6] = num49
    a[6][7] = ind7

    for i in range(n):
        if a[i][i] == 0.0:
            result7x7=('Error...Division por cero')

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
     
    result7x7 = arreglo[0:2]
    return result7x7