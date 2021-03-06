import matplotlib
import matplotlib.patches as patches
import random as r

import matplotlib.pyplot as plt
import matplotlib.path as mplPath

# limits of integration
a = 0
b = 100  #borne de la figure
N = 500 #nbr de points à placer de manière random

def defineShape():
    depart = (r.uniform(17, 30), r.uniform(10, 35))
    pt1 = (r.uniform(0, 20), r.uniform(depart[1], 70))
    pt2 = (r.uniform(5, 25), r.uniform(pt1[1], 90))
    pt3 = (r.uniform(pt2[0], 50), r.uniform(80, 100))
    pt4 = (r.uniform(40, 60), r.uniform(70, 85))
    pt5 = (r.uniform(70, 100), r.uniform(0, 15))
    path_data = [
        (mplPath.Path.MOVETO, depart),
        (mplPath.Path.CURVE3, pt1),
        (mplPath.Path.CURVE3, pt2),
        (mplPath.Path.CURVE3, pt3),
        (mplPath.Path.CURVE3, pt4),
        (mplPath.Path.CURVE3, (75, 90)),
        (mplPath.Path.CURVE3, (80, 60)),
        (mplPath.Path.CURVE3, pt5),
        (mplPath.Path.LINETO, depart)
    ]
    codes, verts = zip(*path_data)
    path = mplPath.Path(verts, codes)

    return path

def monteCarlos(a, b, N, path):
    c = 0 #nbr de points dans la forme

    #création aléatoire de points
    points = [[r.uniform(a, b), r.uniform(a, b) ]  for _ in range(N)]

    for i in range(N) :
        if path.contains_point((points[i][0],points[i][1])) :
            c+=1

    print("nbr points in shape =", c, "sur ", N, "points totaux")

    airAera = (c/N)*pow((b-a), 2)

    return points, airAera

def displayFigure(path, points, N):
    patch = patches.PathPatch(path, facecolor='b', alpha=0.5)

    # Affiche le patch et les points que l'on jette
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.add_patch(patch)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    for i in range(N) :
        ax.scatter(points[i][0], points[i][1], s = 2 + 1000/N)

    plt.show()

print("\nAlgorithme de Monte-Carlo")
path = defineShape()
[points, airAera] = monteCarlos(a, b, N, path)
print("pour N =", N, ", la figure a une aire de", airAera)
displayFigure(path, points, N)


#the current algorithm has some limitations: The result is undefined for points exactly at the boundary (i.e. at the path shifted by radius/2).