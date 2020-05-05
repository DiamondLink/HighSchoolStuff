from baptiste_villeneuve_mes_fonctions import lire_csv_list
import matplotlib.pyplot as plt

def getList(fichier : str):
    liste = lire_csv_list(fichier)
    del liste[0]
    return liste

def getTypeAndDatas(fichier):
    arrayList = getList(fichier)
    i = 0
    for element in arrayList:
        del element[-1]
        i2 = 0
        for data in element:
            try:
                arrayList[i][i2] = int(data)
            except:
                pass
            i2 += 1
        i += 1
    return arrayList

def getStatGraph(listEntry, labels : list, types = False, type1 = [None,None], type2 = [None,None], color = "b"):
    for data in listEntry:
        if types:
            if data[0] == type1[0]:
                plt.scatter(data[1], data[2], marker = "o", c = type1[1])
            elif data[0] == type2[0]:
                plt.scatter(data[1], data[2], marker = "o", c = type2[1])
        else:
            plt.scatter(data[0], data[1], marker = "o", c = color)

    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    if types:
        plt.legend([plt.scatter(listEntry[0][1], listEntry[0][2], marker = "o", c = type1[1]), plt.scatter(listEntry[0][1], listEntry[0][2], marker = "o", c = type2[1])], [type1[0], type2[0]], loc = 'best')

    plt.grid()
    
    return plt

if __name__ == "__main__":
    #POKEMON
    graph = getStatGraph(getTypeAndDatas("11-10 Pokemons_2_types.csv"), labels = ["Points de vie","Points d'attaque"], types = True, type1=["Eau","b"], type2=["Psy", "m"])
    graph.savefig('11-10 Pokemons_2_types.pdf ', format = 'pdf')
    graph.show()

    #IRIS
    graph = getStatGraph(getTypeAndDatas("11-11 iris.csv"), labels = ["petal lengh", "petal width"])
    graph.savefig('11-11 iris.pdf ', format = 'pdf')
    graph.show()

