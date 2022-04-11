import random as r
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate

def monteCarlosPi():
    # limits of integration
    a = 0
    b = 1  # gets the value of pi
    N = 10000 #nbr de points à placer de manière random
    c = 0 #nbr de points sous la courbe

    points = [[r.uniform(a, b), r.uniform(a, b) ]  for _ in range(N)]
    #print(points)

    for i in range(N) :
        rayon = pow(pow(points[i][0], 2) + pow(points[i][1], 2), 0.5)
        if rayon < 1 :
            c+=1
            #print("point n.", i, "sous la courbe")

    pi = (c/N)*4
    print("pi est environ ", pi)
    # dx = 0.005
    # x  = np.arange(-10, 10, dx)
    # y  = 0.25*np.exp((-x ** 2)/8)
    #
    # y=y/ (np.sum(dx * y))
    #
    # plt.plot(x,y,label="pdf")
    # plt.xlabel("X")
    # plt.ylabel("Probability Values")
    # plt.title("Monte Carlos")
    # plt.legend()
    # plt.show()

