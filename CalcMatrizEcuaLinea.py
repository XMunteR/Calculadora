import sympy as sp
from sympy import Matrix, det
from sympy import *
import numpy as np




def matrices(numeroBoton,num1, num2, num3, num4, num5, num6, num7, num8, num9, matrix):
    global A, B, C, D, E, F, G
    if numeroBoton == "A":
        if(matrix == "2x2"):
            A = np.matrix([[num1,num2],[num4,num5]])
            return A
        elif(matrix == "3x2"):
            A = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return A
        elif(matrix == "3x3"):
            A = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return A
        elif(matrix == "2x3"):
            A = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return A
    elif numeroBoton == "B":
        if(matrix == "2x2"):
            B = np.matrix([[num1,num2],[num4,num5]])
            return B
        elif(matrix == "3x2"):
            B = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return B
        elif(matrix == "3x3"):
            B = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return B
        elif(matrix == "2x3"):
            B = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return B
    elif numeroBoton == "C":
        if(matrix == "2x2"):
            C = np.matrix([[num1,num2],[num4,num5]])
            return C
        elif(matrix == "3x2"):
            C = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return C
        elif(matrix == "3x3"):
            C = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return C
        elif(matrix == "2x3"):
            C = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return C
    elif numeroBoton == "D":
        if(matrix == "2x2"):
            D = np.matrix([[num1,num2],[num4,num5]])
            return D
        elif(matrix == "3x2"):
            D = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return D
        elif(matrix == "3x3"):
            D = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return D
        elif(matrix == "2x3"):
            D = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return D
    elif numeroBoton == "E":
        if(matrix == "2x2"):
            E = np.matrix([[num1,num2],[num4,num5]])
            return E
        elif(matrix == "3x2"):
            E = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return E
        elif(matrix == "3x3"):
            E = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return E
        elif(matrix == "2x3"):
            E = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return E
    elif numeroBoton == "F":
        if(matrix == "2x2"):
            F = np.matrix([[num1,num2],[num4,num5]])
            return F
        elif(matrix == "3x2"):
            F = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return F
        elif(matrix == "3x3"):
            F = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return F
        elif(matrix == "2x3"):
            F = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return F
    elif numeroBoton == "G":
        if(matrix == "2x2"):
            G = np.matrix([[num1,num2],[num4,num5]])
            return G
        elif(matrix == "3x2"):
            G = np.matrix([[num1,num2],[num4,num5],[num7,num8]])
            return G
        elif(matrix == "3x3"):
            G = np.matrix([[num1,num2,num3],[num4,num5,num6], [num7,num8,num9]])
            return G
        elif(matrix == "2x3"):
            G = np.matrix([[num1,num2,num3], [num4,num5,num6]])
            return G
        


