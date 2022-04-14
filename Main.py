import random
import time

import LasVegas
import MonteCarlo
import MonteCarloShape

def main():

    # Monte-Carlo
    MonteCarlo.monteCarlosPi()

    print("\n------------------------------------------------------------------- \nAlgorithme de Las Vegas")
    # Las Vegas

    print("\nExemple du tri rapide :")
    list = []
    taille = 10000
    for i in range(taille):
        list.append(random.randint(0, 1000))

    for i in range(10):
        start = time.time()
        list = LasVegas.quickSortLV(list)
        temps = time.time() - start
        print("Temps d'exécution :", temps * 1000, "ms")

    print("\nExemple du problème des 8 reines :")
    count = 0
    print("Solutions trouvées :")
    for i in range(1000):
        result = LasVegas.queens()
        if not result:
            count = count + 1
        else:
            print(result)
    print(str(count) + ' itérations sans solutions')

    return 0

main()