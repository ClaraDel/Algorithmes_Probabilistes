import random
from Tri_Rapide import *
from MonteCarlos import *

def main():


if __name__ == '__main__':
    main()

def launchQuickSort() :
    tailleList = 10
    valMax = 20
    liste = [random.randrange(1, valMax) for _ in range(tailleList)]
    print("liste initiale = ",liste)
    listeTriée = quicksort(liste)
    print("liste triée = ", listeTriée)