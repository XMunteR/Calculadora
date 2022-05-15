import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
""" ecuacion = input("Enter a function: ")
inferior = int(input("Enter the start point: "))
superior = int(input("Enter the end point: "))
numeroIteraciones = int(input("Enter the number of rectangles: ")) """

#ecu(ecuacion, inferior, superior,numeroIteraciones)

def ecu(ecuacion, inferior, superior,numeroIteraciones):
    global midpoint_riemann_sum,left_riemann_sum,right_riemann_sum
    """ ecuacion = input("Enter a function: ")
    inferior = int(input("Enter the start point: "))
    superior = int(input("Enter the end point: "))
    numeroIteraciones = int(input("Enter the number of rectangles: ")) """

    f=lambda x : eval(ecuacion)
    a=inferior #izquierdo 
    b=superior #Derecho
    N=numeroIteraciones

    """ f = lambda x : x**2
    a = 0; b = 5; N = 10 """
    n = N # Use n*N+1 points to plot the function smoothly


    x = np.linspace(a,b,N+1)
    y = f(x)

    X = np.linspace(a,b,n*N+1)
    Y = f(X)

    dx = (b-a)/N
    x_left = np.linspace(a,b-dx,N)
    x_midpoint = np.linspace(dx/2,b - dx/2,N)
    x_right = np.linspace(dx,b,N)

    print("Partition with",N,"subintervals.")
    left_riemann_sum = np.sum(f(x_left) * dx)
    print("Left Riemann Sum:",left_riemann_sum)

    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
    print("Midpoint Riemann Sum:",midpoint_riemann_sum)

    right_riemann_sum = np.sum(f(x_right) * dx)
    print("Right Riemann Sum:",right_riemann_sum)

    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.plot(X,Y,'b')
    x_left = x[:-1] # Left endpoints
    y_left = y[:-1]
    plt.plot(x_left,y_left,'b.',markersize=10)
    plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title('Left Riemann Sum, N = {}'.format(N))

    plt.subplot(1,3,2)
    plt.plot(X,Y,'b')
    x_mid = (x[:-1] + x[1:])/2 # Midpoints
    y_mid = f(x_mid)
    plt.plot(x_mid,y_mid,'b.',markersize=10)
    plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
    plt.title('Midpoint Riemann Sum, N = {}'.format(N))

    plt.subplot(1,3,3)
    plt.plot(X,Y,'b')
    x_right = x[1:] # Left endpoints
    y_right = y[1:]
    plt.plot(x_right,y_right,'b.',markersize=10)
    plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title('Right Riemann Sum, N = {}'.format(N))

    plt.show()

#ecu(ecuacion, inferior, superior,numeroIteraciones)