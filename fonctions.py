#coding : UTF-8

def recherche_element(tableau : list,element):
    """Rechercher d'un élément dans un tableau"""
    i = 0
    while t[i] < element and i <= n-1:
        i += 1
    if tableau[i] == element:
        return("{} a été trouvé".format(element))
    else:
        return("{} n'a pas été trouvé".format(element))
    
def recherche_dichotomie(tableau : list,element):
    """Rechercher d'un élément dans un tableau"""
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

def tri_fusion(tableau1 : list,tableau2 : list):
    n1 = len(tableau1)
    n2 = len(tableau2)

    x =0
    y = 0

    for i in range(0,n1 + n2):
        if x < n1 and y <n2:
            if tableau1[x] <= tableau2[y]:
                tableau3[i] = tableau1


