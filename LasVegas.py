import random
import time


def quickSortLV(tab):
    pTab = []
    gTab = []
    size = len(tab)
    if size < 2:
        return tab
    indice = random.randint(0, size - 1)
    for i in range(size):
        if i != indice:
            if tab[i] <= tab[indice]:
                pTab.append(tab[i])
            else:
                gTab.append(tab[i])
    return quickSortLV(pTab) + [tab[indice]] + quickSortLV(gTab)

list = []
taille = 100000
for i in range(taille):
    list.append(random.randint(0, 1000))

for i in range(10):
    start = time.time()
    list = quickSortLV(list)
    temps = time.time() - start
    print("Temps d'exécution :", temps)