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

def queens():
    tab = []
    for i in range(8):
        tab.append([0])
        for j in range(7):
            tab[i].append(0)

    for i in range(8):
        if not queensIter(tab):
            return False

    return printSolution(tab)

def queensIter(tab):

    a = random.randint(0, 7)
    o = random.randint(0, 7)
    while verification(tab, a, o):
        a = random.randint(0, 7)
        o = random.randint(0, 7)

    if verifDiag(tab, a, o):
        gonext = False
    else:
        tab[a][o] = 1
        gonext = True
    return gonext

def printSolution(tab):
    solution = ""
    for i in range(8):
        for j in range(8):
            if tab[i][j] == 1:
                solution = solution + '(' + str(i) + ' ' + str(j) + ')'
    return solution

def verification(tab, a, o):
    for i in range(a):
        if tab[i][o] == 1:
            return True
    for i in range(a, 8):
        if tab[i][o] == 1:
            return True
    for i in range(o):
        if tab[a][i] == 1:
            return True
    for i in range(o, 8):
        if tab[a][i] == 1:
            return True
    return False

def verifDiag(tab, a, o):
    l = a
    c = o
    while l != 0 and c != 0:
        l = l - 1
        c = c - 1
        if tab[l][c] == 1:
            return True
    l = a
    c = o
    while l != 7 and c != 0:
        l = l + 1
        c = c - 1
        if tab[l][c] == 1:
            return True
    l = a
    c = o
    while l != 0 and c != 7:
        l = l - 1
        c = c + 1
        if tab[l][c] == 1:
            return True
    l = a
    c = o
    while l != 7 and c != 7:
        l = l + 1
        c = c + 1
        if tab[l][c] == 1:
            return True