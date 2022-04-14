import random
from Tri_Rapide import *
from MonteCarlos import *

def main():

    _list_of_vertices
    MC(_list_of_vertices, iters, visualise = True, s_type = "rand")

if __name__ == '__main__':
    main()

def launchQuickSort() :
    tailleList = 10
    valMax = 20
    liste = [random.randrange(1, valMax) for _ in range(tailleList)]
    print("liste initiale = ",liste)
    listeTriée = quicksort(liste)
    print("liste triée = ", listeTriée)