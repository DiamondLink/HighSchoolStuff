#encode : utf - 8
import os
import csv
from tkinter import filedialog, Tk

#a)
def lire_csv_dictionnaire(nomFichier):
    csvfile = open(nomFichier, "r")
    contenu = csv.DictReader(csvfile, delimiter=';')
    table = []
    for ligne in contenu:
        table.append(ligne)
    csvfile.close()
    return(table)

#b)
def lire_csv_list(nomFichier):
    liste = list()
    with open(nomFichier, "r") as fichier:
        for ligne in fichier:
            liste.append(ligne.rstrip("\n").split(";"))
    return liste

#c)
def ecrire_Dans_CSV_dictionnaire(nomFichierCSV, listeDict):
    with open(nomFichierCSV, 'w', newline="") as csv_file:
        enTete = [cle for cle in listeDict[0].keys()]
        contenant = csv.DictWriter(csv_file, fieldnames=enTete, delimiter=';')

        contenant.writeheader()
        for ligne in listeDict:
            if None in ligne.keys():
                del(ligne[None])
            contenant.writerow(ligne)

#d)
def ecrire_Dans_CSV_list(nomFichierCSV, listeList):
    with open(nomFichierCSV, 'w', newline="") as csv_file:
        for ligne in listeList:
            csv_file.write(";".join(ligne) + "\n")

#e)
def rechercheFichier(titre, fileTypes: list, rep=os.getcwd()):
    fic = ""
    root = Tk()
    root.withdraw()
    nomfichier = filedialog.askopenfilename(title=titre, initialdir=rep,
    initialfile=fic, filetypes=fileTypes)
    root.destroy()
    return(nomfichier)


#f)
def remplacer_string_par_int(nomFichier, colonnesAConvertir: list = [1, 2]):
    with open(nomFichier, "r") as fichier:
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

    with open(nomFichier, "w") as fichier:
        fichier.write(fichierConverti)

#g)
def supprimerDoublons(nomFichier):
    fichierSansDoublons = ""
    with open(nomFichier, "r") as fichier:
        for ligne in fichier:
            if not ligne in fichierSansDoublons:
                fichierSansDoublons += ligne

    with open(nomFichier, "w") as fichier:
        fichier.write(fichierSansDoublons)

#h)
def trierColonne(nomFichier, colonneATrier: int, croissant=True, inclureLaPremiereLigne=True):
    with open(nomFichier, "r") as fichier:
        listeDeLignes = fichier.readlines()
        if inclureLaPremiereLigne:
            premiereLigne = listeDeLignes[0]
            del(listeDeLignes[0])

        listeDeLigneSplite = list()

        for ligne in listeDeLignes:
            listeDeLigneSplite.append(
                ligne.rstrip("\n").split(";")[colonneATrier])

        for i in range(len(listeDeLigneSplite)):
            colonneTemporaire = ""
            for element in listeDeLigneSplite[i]:
                try:
                    element = int(element)
                    colonneTemporaire += str(element)
                except:
                    pass
            listeDeLigneSplite[i] = colonneTemporaire

        ordreDesLigne = sorted(
            range(len(listeDeLigneSplite)), key=lambda k: int(listeDeLigneSplite[k]))

        listeDeLignesTrie = list()
        for index in ordreDesLigne:
            listeDeLignesTrie.append(listeDeLignes[index])

        if not croissant:
            listeDeLignesTrie.reverse()

        if inclureLaPremiereLigne:
            listeDeLignesTrie = premiereLigne.split() + listeDeLignesTrie

    with open(nomFichier, "w") as fichier:
        for i in range(len(listeDeLignesTrie)):
            if listeDeLignesTrie[i][-1:] != "\n":
                listeDeLignesTrie[i] += "\n"
        fichier.write("".join(listeDeLignesTrie))

#i)
def supprimerColonne(nomFichier, colonneASupprimer: int):
    fichierAvecLaColonneEnMoins = ""
    with open(nomFichier,"r") as fichier:
        listeDeLignes = fichier.readlines()
        for ligne in listeDeLignes:
            ligne = ligne.rstrip("\n")
            ligne = ligne.split(";")
            del(ligne[colonneASupprimer])
            fichierAvecLaColonneEnMoins += ";".join(ligne) + "\n"
            
    with open(nomFichier,"w") as fichier:
        fichier.write(fichierAvecLaColonneEnMoins)

#j)
def ajoutDensite(nomFichier):
    remplacer_string_par_int(nomFichier,colonnesAConvertir=[1,2])
    listeDictionnaire = lire_csv_dictionnaire(nomFichier)
    for i in range(len(listeDictionnaire)):
        listeDictionnaire[i]["Densité"] = str(int(listeDictionnaire[i]["Population"]) // int(listeDictionnaire[i]["Superficie"]))
    
    ecrire_Dans_CSV_dictionnaire(nomFichier,listeDictionnaire)

#k)
def fusionDeDeuxTablesAyantuneCleeCommune(table1 : list,table2 : list,cleCommune):
    for dico1 in table1:
        for dico2 in table2:
            if dico1[cleCommune] == dico2[cleCommune]:
                for key in dico2.keys():
                    if key != cleCommune:
                        dico1[key] = dico2[key]

    return table1

#l)
def selecLigneDict(listeDict,cle,signe,critere):
    listDict2 = []
    for dico in listeDict:
        try:
            if signe == ">":
                if dico[cle] > critere:
                    listDict2.append(dico["Pays"])
            elif signe == "<":
                if dico[cle] < critere:
                    listDict2.append(dico["Pays"])
            elif signe == "!=":
                if dico[cle] != critere:
                    listDict2.append(dico["Pays"])
            elif signe == "=":
                if dico[cle] == critere:
                    listDict2.append(dico["Pays"])
        except:
            pass

    return listDict2
assert selecLigneDict([{"Pays" : "France", "population" : 65},{"Pays" : "Allemagne", "population" : 85},{"Pays" : "Italie","population" : 60}], "population","<",70) == ["France","Italie"]

#k)
if __name__ == "__main__": 
    listePays = lire_csv_dictionnaire("Monde_Nbre_Habitants_2019_Superficie.csv")
    listeMonaie = lire_csv_dictionnaire("Monde_Monnaie.csv")
    listeCapitale = lire_csv_dictionnaire("Monde_Capitale_Continent.csv")

    paysETmonaieFusionne = fusionDeDeuxTablesAyantuneCleeCommune(listePays, listeMonaie, "Pays")
    tablesFusionne = fusionDeDeuxTablesAyantuneCleeCommune(paysETmonaieFusionne, listeCapitale,"Pays")

    ecrire_Dans_CSV_dictionnaire("Monde_Nbre_Habitants_2019_Superficie.csv",tablesFusionne)