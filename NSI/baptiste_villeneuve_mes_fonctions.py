import os
import csv
from tkinter import filedialog,Tk
os.chdir("C://Users//BAPTISTE//Downloads")

def lire_csv_dictionnaire(nomFichier):
    csvfile =open(nomFichier,"r")
    contenu=csv.DictReader(csvfile, delimiter=';')
    table=[]
    for ligne in contenu :
        table.append(ligne)
    csvfile.close()
    return(table)

def lire_csv_list(nomFichier):
    liste = list()
    with open(nomFichier,"r") as fichier:
        for ligne in fichier:
            liste.append(ligne.rstrip("\n").split(";"))
    return liste

def ecrire_Dans_CSV_dictionnaire(nomFichierCSV,listeDict): 
    with open(nomFichierCSV, 'w', newline="") as csv_file:
        enTete=[cle for cle in listeDict[0].keys()] 
        contenant = csv.DictWriter(csv_file, fieldnames=enTete, delimiter=';') 

        contenant.writeheader()
        for ligne in listeDict:
            contenant.writerow(ligne)

def ecrire_Dans_CSV_list(nomFichierCSV,listeList):
    with open(nomFichierCSV, 'w', newline="") as csv_file:
        for ligne in listeList:
            csv_file.write(";".join(ligne) + "\n")


def rechercheFichier(titre, fileTypes : list, rep=os.getcwd()):
    fic=""
    root=Tk()
    root.withdraw()
    nomfichier=filedialog.askopenfilename(title =titre,initialdir =rep,
    initialfile=fic, filetypes=fileTypes)
    root.destroy()
    return(nomfichier) 

def remplacer_string_par_int(nomFichier, colonnesAConvertir : list = [1,2]):
    with open (nomFichier,"r") as fichier:
        fichierConverti = None
        for ligne in fichier:
            ligne = ligne.rstrip("\n")
            if fichierConverti == None:
                fichierConverti = ligne + "\n"
            else:
                listeDeLignes = ligne.split(";")
                for colonne in listeDeLignes:
                    isChanged = False
                    for colonneIndex in colonnesAConvertir:
                        if listeDeLignes[colonneIndex] == colonne:
                            for element in colonne:
                                if element == " ":
                                    fichierConverti += element
                                    isChanged = True
                                else:
                                    try:
                                        element = int(element)
                                        fichierConverti += str(element)
                                        isChanged = True
                                    except:
                                        pass

                    if not isChanged:
                        fichierConverti += colonne
                    fichierConverti += ";"
                fichierConverti += "\n"
    
    with open(nomFichier,"w") as fichier:
        fichier.write(fichierConverti)

def supprimerDoublons(nomFichier):
    fichierSansDoublons = ""
    with open(nomFichier,"r") as fichier:
        for ligne in fichier:
            if not ligne in fichierSansDoublons:
                fichierSansDoublons += ligne

    with open(nomFichier,"w") as fichier:
        fichier.write(fichierSansDoublons)

def trierColonne(nomFichier,colonneATrier : int, croissant = True, inclureLaPremiereLigne = True):
    with open(nomFichier,"r") as fichier:
        listeDeLignes = fichier.readlines()
        if inclureLaPremiereLigne:
            premiereLigne = listeDeLignes[0]
            del(listeDeLignes[0])

        listeDeLigneSplite = list()

        for ligne in listeDeLignes:
            listeDeLigneSplite.append(ligne.rstrip("\n").split(";")[colonneATrier])
        
        for i in range(len(listeDeLigneSplite)):
            colonneTemporaire = ""
            for element in listeDeLigneSplite[i]:
                try:
                    element = int(element)
                    colonneTemporaire += str(element)
                except:
                    pass
            listeDeLigneSplite[i] = colonneTemporaire

        ordreDesLigne = sorted(range(len(listeDeLigneSplite)), key=lambda k: int(listeDeLigneSplite[k]))

        listeDeLignesTrie = list()
        for index in ordreDesLigne:
            listeDeLignesTrie.append(listeDeLignes[index])

        if not croissant:
            listeDeLignesTrie.reverse()
        
        if inclureLaPremiereLigne:
            listeDeLignesTrie = premiereLigne.split() + listeDeLignesTrie
    
    with open(nomFichier,"w") as fichier:
        for i in range(len(listeDeLignesTrie)):
            if listeDeLignesTrie[i][-1:] != "\n":
                listeDeLignesTrie[i] += "\n"
        fichier.write("".join(listeDeLignesTrie))

trierColonne("tableau.csv",colonneATrier=1)




