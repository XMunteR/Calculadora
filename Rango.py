from unittest import result
import numpy as np
import sympy as sp

def matricesRango2x2(num1,num2,num4,num5):
    global result1
    Matriz2x2=([[num1,num2],
                [num4,num5]])

    print(Matriz2x2)
    result1=np.linalg.matrix_rank(Matriz2x2) 
    return result1

def matricesRango3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9):
    global result2
    Matriz3x3=([[num1,num2,num3],
            [num4,num5,num6],
            [num7,num8,num9]])
    
    
    print(Matriz3x3)
    result2=np.linalg.matrix_rank(Matriz3x3) 

    return result2
