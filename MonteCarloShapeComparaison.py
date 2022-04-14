import matplotlib
import matplotlib.patches as patches
import random as r

import matplotlib.pyplot as plt
import matplotlib.path as mplPath

# limits of integration
a = 0
b = 100  #borne de la figure
N = 1000 #nbr de points à placer de manière random

def defineShape():

    #rectangle
    depart = (30,30)
    a = 40
    b = 50
    airRec = a*b
    path_data = [
        (mplPath.Path.MOVETO, depart),
        (mplPath.Path.LINETO, (depart[0],depart[1]+a)),
        (mplPath.Path.LINETO, (depart[0]+b,depart[1]+a)),
        (mplPath.Path.LINETO, (depart[0] + b, depart[1])),
        (mplPath.Path.LINETO, (30,30))
    ]
    codes, verts = zip(*path_data)
    path = mplPath.Path(verts, codes)

    return path, airRec

def monteCarlos(a, b, N, path):
    c = 0 #nbr de points dans la forme

    #création aléatoire de points
    points = [[r.uniform(a, b), r.uniform(a, b) ]  for _ in range(N)]

    for i in range(N) :
        if path.contains_point((points[i][0],points[i][1])) :
            c+=1

    airAera = (c/N)*pow((b-a), 2)

    return points, airAera

def displayFigure(path, points, N):
    patch = patches.PathPatch(path, facecolor='r', alpha=0.5)

    # Affiche le patch et les points que l'on jette
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.add_patch(patch)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    for i in range(N) :
        ax.scatter(points[i][0], points[i][1], s = 2 + 1000/N)

    plt.show()

print("\nAlgorithme de Monte-Carlo (comparaison avec air exacte)")
path, airRec = defineShape()
valeursN = [500, 1000, 100000]
for N in valeursN:
    [points, airAera] = monteCarlos(a, b, N, path)
    print("-----  N =", N, "-----")
    print("Air avec Monte Carlos :", airAera)
    print("Air exacte :", airRec)
    print("Erreur de", abs((airAera-airRec))/airRec*100, "%")
    if(N==500) :
        displayFigure(path, points, N)


#the current algorithm has some limitations: The result is undefined for points exactly at the boundary (i.e. at the path shifted by radius/2).