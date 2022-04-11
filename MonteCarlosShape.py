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
    path_data = [
        (mplPath.Path.MOVETO, (10, 20)),
        (mplPath.Path.CURVE4, (20, 80)),
        (mplPath.Path.CURVE4, (40, 80)),
        (mplPath.Path.CURVE4, (80, 90)),
        (mplPath.Path.CURVE4, (85, 35)),
        (mplPath.Path.CURVE4, (40, 25)),
        (mplPath.Path.CURVE4, (8, 14))
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
        ax.scatter(points[i][0], points[i][1])

    plt.show()


path = defineShape()
[points, airAera] = monteCarlos(a, b, N, path)
print("pour N =", N, ", la figure a une aire de", airAera)
displayFigure(path, points, N)


# Steps
# Create a list of points to make the polygon.
#
# Create a new path with the given vertices and codes, using mplPath.Path().
#
# Check if point (200, 100) exists in the polygon or not, using contains_point() method. Return whether the (closed) path contains the given point. => True
#
# Check if point (1200, 1000) exists in the polygon or not, using contains_point() method. Return whether the (closed) path contains the given point. => False