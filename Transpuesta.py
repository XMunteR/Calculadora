from unittest import result
import numpy as np
import sympy as sp

def matricesTranspuesta2x2(num1,num2,num4,num5):
    global result1
    Matriz2x2=([[num1,num4],
                [num2,num5]])

    result1 =str(Matriz2x2)
    
    return result1

def matricesTranspuesta3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9):
    global result2
    matriz3x3=([[num1,num4,num7],
                [num2,num5,num8],
                [num3,num6,num9]])

    result2 = str(matriz3x3)
    return result2