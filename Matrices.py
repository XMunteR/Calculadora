import numpy as np
import sympy as sp

''' def matrices():

    return '''

n_array = np.array([[5, 2, 1, 4, 6], 
                    [9, 4, 2, 5, 2], 
                    [11, 5, 7, 3, 9], 
                    [5, 6, 6, 7, 2], 
                    [7, 5, 9, 3, 3]]) 
  
print("Numpy Matrix is:") 
print(n_array) 
  
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 5X5 square matrix:") 
print(int(det)) 
