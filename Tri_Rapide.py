import random as r

def separation(liste, pivot, i):
    """Entrée : une liste, un pivot et la place du pivot dans la liste
    Sortie : une liste listePetit contenant les éléments de liste strictement plus petits que le pivot et une liste listeGrand contentant, à l'exception du pivot, les éléments plus grands que le pivot"""
    listePetit = []
    listeGrand = []
    for k in range(len(liste)):
        """Cela permet d'exclure le pivot"""
        if k != i:
            if liste[k] >= pivot:
                listeGrand.append(liste[k])
            else:
                listePetit.append(liste[k])
    return listePetit, listeGrand


def quicksort(liste):
    """Entrée : une liste
       Sortie : une liste avec les mêmes éléments triés par l'algorithme de tri rapide randomisé"""
    n = len(liste)
    if n == 1 or n==0:
        """Une liste à 1 élément est toujours triée"""
        return liste
    else:
        """Choix du pivot AU HASARD dans la liste"""
        i = r.randint(0, n - 1)
        pivot = liste[i]

        """On sépare en 2 listes de taille strictement plus petite que n car le pivot n'appartient à aucune des deux listes"""
        liste1, liste2 = separation(liste, pivot, i)

        """Le résultat est la concaténation des deux sous-listes auparavant triés, avec le pivot entre elles"""
        return quicksort(liste1) + [pivot] + quicksort(liste2)