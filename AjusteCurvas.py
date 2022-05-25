from numpy import *
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from pylab import mpl

y = []
x = []


def DeArray(Ax,Ay):
    global x, y
    

    x.append(Ax)
    
    y.append(Ay)

def AjustarCurva (grado):
    global resultado,p
    # Datos experimentales

    # Ajuste a una recta (polinomio de grado 1)
    p = polyfit(x, y, grado)

    print("p")
    print(p)

    # Ajuste a una recta, con salida completa
    resultado = polyfit(x, y, 1)
    print("resultado")
    print(resultado)
    """ Imprime tupla
    (array([ 2.7 ,  9.94]),                 # Parámetros del ajuste
    array([ 0.472]),                       # Suma de residuos
    2,                                     # Rango de la matriz del sistema
    array([ 2.52697826,  0.69955764]),     # Valores singulares
    1.1102230246251565e-15)                # rcond
    """

    # Evaluo el polinomio en x=5.4
    print ("polyval(p, 5.4)")
    print (polyval(p, 5.4))

def graficar():
    parameter = liner_fitting(x,y)
    draw_data = calculate(x,parameter[0],parameter[1])
    draw(x,draw_data,y) 



def liner_fitting(data_x,data_y):
      size = len(data_x);
      i=0
      sum_xy=0
      sum_y=0
      sum_x=0
      sum_sqare_x=0
      average_x=0;
      average_y=0;
      while i<size:
          sum_xy+=data_x[i]*data_y[i];
          sum_y+=data_y[i]
          sum_x+=data_x[i]
          sum_sqare_x+=data_x[i]*data_x[i]
          i+=1
      average_x=sum_x/size
      average_y=sum_y/size
      return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
      return_b=average_y-average_x*return_k
      return [return_k,return_b]
 
 
#Después de completar el cálculo del valor de función correspondiente en la curva
def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay

def draw(data_x,data_y_new,data_y_old):
         plt.plot (data_x, data_y_new, label = "curva de ajuste", color = "black")
         plt.scatter (data_x, data_y_old, label = "datos discretos")
         #mpl.rcParams['font.sans-serif'] = ['SimHei']
         mpl.rcParams['axes.unicode_minus'] = False
         plt.title ("Datos de ajuste lineal de una variable")
         plt.legend(loc="upper left")
         plt.show()
 
 