#coding : UTF-8

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
    """Rechercher d'un élément dans un tableau par dichotomie"""
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

assert recherche_element([1,7,19,28],21) == "21 n'a pas été trouvé"
assert recherche_element([3,12,90,113],113) == "113 a été trouvé"

def tri_par_selection(tableau : list):
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

def tri_insertion(tableau):
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

def tri_fusion(tableau1 : list,tableau2 : list):
    n1 = len(tableau1)
    n2 = len(tableau2)

    tableau3 = ["salut"] * (n1 + n2)

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

assert tri_fusion([3,9,12,90],[5,9,56,101]) == [3,5,9,9,12,56,90,101]