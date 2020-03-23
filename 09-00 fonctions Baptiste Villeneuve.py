# coding: utf-8
import random
import time

def recherche_element(tableau : list,element):
    """Recherche d'un élément dans un tableau"""
    n = len(tableau)
    i = 0
    while tableau[i] < element and i <= n-1:
        i += 1
    if tableau[i] == element:
        return("{} a été trouvé".format(element))
    else:
        return("{} n'a pas été trouvé".format(element))
    
assert recherche_element([1,7,19,28],19) == "19 a été trouvé"
assert recherche_element([3,12,90,113],56) == "56 n'a pas été trouvé"




    
def recherche_dichotomie(tableau : list,element):
    """Algorithme de recherche pour trouver la position d'un élément dans un tableau trié.
    Le principe est le suivant : comparer l'élément avec la valeur de la case au milieu du tableau ;
    si les valeurs sont égales, la tâche est accomplie, sinon on recommence dans la moitié du tableau pertinente."""
    n = len(tableau)
    g = 0
    d = n-1
    milieu = int((g + d)/2)
    while tableau[milieu] != element and g <= d:
        if tableau[milieu] < element:
            g = milieu+1
        else:
            d = milieu - 1
        
        milieu = int((g + d)/2)

    if tableau[milieu] == element:
        return("{} est dans le tableau".format(element))
    else:
        return("{} n'est pas dans le tableau".format(element))

assert recherche_dichotomie([1,7,19,28],21) == "21 n'est pas dans le tableau"
assert recherche_dichotomie([3,12,90,113],113) == "113 est dans le tableau"

def tri_par_selection(tableau : list):
    """Algorithme permettant de trié un tableau. Le tri par sélection est un algorithme par comparaison.
    Il s'exécute en temps quadratique"""
    n = len(tableau)
    for i in range(0,n-1):
        minimum = i
        for j in range(i + 1,n):
            if tableau[j] < tableau[minimum]:
                minimum = j
        if minimum != i:
            tableau[i],tableau[minimum] = tableau[minimum],tableau[i]

    return tableau

assert tri_par_selection([21,912,13,1,67,53]) == [1,13,21,53,67,912]

def tri_a_bulle(tableau : list):
    """Algoritme de tri (à bulle) consistant à comparer répétitivement les éléments consécutifs d'un tableau,
    et à les permuter lorsqu'ils sont mal triés"""
    n = len(tableau)
    echange = True
    while echange == True:
        echange = False
        for i in range(1,n):
            if tableau[i] < tableau[i-1]:
                tableau[i],tableau[i-1] = tableau[i-1],tableau[i]
                echange = True
    
    return tableau

assert tri_a_bulle([9,21,15,90,65,15]) == [9,15,15,21,65,90]

def tri_insertion(tableau : list):
    """Algorithme du tri par insertion. On fait comme si les éléments à trier étaient donnés un par un, le premier élément constituant, à lui tout seul, une liste triée de longueur 1.
    On range ensuite le second élément pour constituer une liste triée de longueur 2, puis on range le troisième élément pour avoir une liste triée de longueur 3 et ainsi de suite.
    Le principe du tri par insertion est donc d'insérer à la nième itération le nième élément à la bonne place."""
    n = len(tableau)
    for i in range(1,n):
        x = tableau[i]
        j = i
        while j >= 1 and tableau[j-1] > x:
            tableau[j] = tableau[j-1]
            j -= 1
        
        tableau[j] = x
    
    return(tableau)


assert tri_insertion([5,2,3,1,8,4,10,7]) == [1,2,3,4,5,7,8,10]

def fusion(tableau1 : list,tableau2 : list):
    """Fonction renvoyant un tableau trié à partir de 2 listes déjà triées
    
    À partir de deux listes triées, on peut facilement construire une liste triée comportant les éléments issus de ces deux listes (leur *fusion*).
    Le principe de l'algorithme de tri fusion repose sur cette observation : le plus petit élément de la liste à construire est soit le plus petit élément de la première liste, soit le plus petit élément de la deuxième liste. 
    Ainsi, on peut construire la liste élément par élément en retirant tantôt le premier élément de la première liste, tantôt le premier élément de la deuxième liste """
    n1 = len(tableau1)
    n2 = len(tableau2)

    tableau3 = [None] * (n1 + n2)

    x =0
    y = 0

    for i in range(0,n1 + n2):
        if x < n1 and y <n2:
            if tableau1[x] <= tableau2[y]:
                tableau3[i] = tableau1[x]
                x += 1
            else:
                tableau3[i] = tableau2[y]
                y += 1
        elif x >= n1:
            tableau3[i] = tableau2[y]
            y += 1
        else:
            tableau3[i] = tableau1[x]
            x +=1

    return tableau3

def tri_par_fusion(tableau : list):
    """Algorithme de tri par fusion, qui utilise la fusion : le tableau est divisé et les nouveau tableau sont triées entre eux"""
    if len(tableau)<2:
        return tableau[:]
    else:
        milieu=len(tableau)//2
        liste1=tri_par_fusion(tableau[:milieu])
        liste2=tri_par_fusion(tableau[milieu:])
    return fusion(liste1,liste2)

assert fusion([3,9,12,90],[5,9,56,101]) == [3,5,9,9,12,56,90,101]
assert tri_par_fusion([89,13,13,6,78,2,43]) == [2,6,13,13,43,78,89]

#PERMUTATION
def permutation(tableau : list):
    """Fonction permettant de permuter les éléments d'un tableau ave une part d'aléatoire"""
    n = len(tableau)
    for i in range(n):
        randInt = random.randint(0,n-1)
        tableau[i], tableau[randInt] = tableau[randInt], tableau[i]
def estTrié(a): 
    """Renvoie True si le tableau est trié, sinon, renvoie False"""
    n = len(a) 
    for i in range(0, n-1): 
        if (a[i] > a[i+1] ): 
            return False
    return True
def tri_permutation(tableau : list): 
    """Algorithme de tri par permutation consistant à "mélanger" aléatoirement un tableau jusqu'à ce qu'il soit trié"""
    n = len(tableau) 
    while (estTrié(tableau)== False): 
        permutation(tableau)
    return tableau

assert tri_permutation([9,31,1,78,12,7,34]) == [1,7,9,12,31,34,78]

def remplissage_tableau(n : int):
    """Algorithme renvoyant un tableau contenant n éléments aléatoire compris entre 1 et n"""
    tableau = list()
    for i in range(n):
        tableau.append(random.randint(1,n))
    
    return tableau

def temp_dexecution_pour_une_fonction(fonction, *args, **kwargs):
    """Fonction renvoyant le temp d'execution d'une fonction"""
    tempAuDemarrage = time.time()
    fonction(*args, **kwargs)
    return(time.time() - tempAuDemarrage)

if __name__ == "__main__":
    longueurTableau = int(input("Longueur du tableau : "))

    fonctions = [tri_par_selection,tri_a_bulle,tri_insertion,tri_par_fusion] #TRI PAR PERMUTATION EST TROP LONG

    for fonction in fonctions:
        tableau = remplissage_tableau(longueurTableau)
        print("L'algorithme {} a un temp d'execution de {} s avec un tableau de longueur {}".format(fonction.__name__,temp_dexecution_pour_une_fonction(fonction,tableau),longueurTableau))