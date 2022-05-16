from unittest import result
import numpy as np
import sympy as sp

def matricesElevado2x2(num1,num2,num4,num5,elev):
    global result2
    Matriz2x2=([[num1 ,num2 ],
                [num4 ,num5 ]])

    print(Matriz2x2)
    result2=np.linalg.matrix_power(Matriz2x2,elev)
    return result2

def matricesElevado3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9,elev):
    global result1
    Matriz3x3=([[num1 ,num2 ,num3 ],
                [num4 ,num5 ,num6 ],
                [num7 ,num8 ,num9 ]])
    
    
    print (Matriz3x3)
    result1= np.linalg.matrix_power(Matriz3x3,elev)
    

    return result1
