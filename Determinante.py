from unittest import result
import numpy as np
import sympy as sp

def matricesDeterminante(num1,num2,num3,num4,num5,num6,num7,num8,num9):

    global result
    print("Sistema 3x3")
    Matriz=([[num1,num2,num3],
            [num4,num5,num6],
            [num7,num8,num9]])
    print(Matriz)
    result=np.linalg.det(Matriz)    
    return result




''' n_array = np.array([[5, 2, 1, 4, 6], 
                    [9, 4, 2, 5, 2], 
                    [11, 5, 7, 3, 9], 
                    [5, 6, 6, 7, 2], 
                    [7, 5, 9, 3, 3]]) 
  
print("Numpy Matrix is:") 
print(n_array) 
  
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 5X5 square matrix:") 
print(int(det)) 
 '''