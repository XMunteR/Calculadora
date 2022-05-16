from audioop import mul
from unittest import result
import numpy as np
import sympy as sp

def matricesMult2x2(num1,num2,num4,num5,mult):
    global result2
    Matriz2x2=([[num1 * mult,num2 * mult],
                [num4 * mult,num5 *mult]])

    print(Matriz2x2)
    result2=(Matriz2x2)
    return result2

def matricesMult3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9,mult):
    global result1
    Matriz3x3=([[num1 *mult,num2 *mult,num3 *mult],
                [num4 *mult,num5 *mult,num6 *mult],
                [num7 *mult,num8 *mult,num9 *mult]])
    
    
    print(Matriz3x3)
    result1=(Matriz3x3)

    return result1
