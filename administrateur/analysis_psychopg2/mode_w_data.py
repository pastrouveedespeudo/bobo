from database import visualisation_table
from conteneur import CONTENEUR


def traitement_coul(a):
    
    liste = []

    #on met la liste dans une liste car c du str
    for i in a:
        if i == ',':
            liste.append("','")
        elif i == '"':
            pass
        elif i == '}' or i == '{':
            pass
        else:
            liste.append(i)

    #on la nettoyé

    liste = "".join(liste)
    liste = "'" + liste + "'"
    #on ajoute ' au debut et a la fin


    print(liste)


    c = 0

    for i in liste:

        if i == ",":
            c+=1
        elif i == '"' or i == "'":
            pass
        else:
            CONTENEUR[c].append("".join(i))

    liste2 = []


    for i in CONTENEUR:
        if i == []:
            pass
        else:
            i = "".join(i)
            liste2.append(i)

    dico = {}
    

    liste3 = set(liste2)

    for i in liste3:
        dico[i] = 0

    print(dico)

    for i in liste2:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i]+=1

    liste4 = []
    for cle, valeur in dico.items():
        if valeur == 0:
            pass
        else:
            liste4.append((cle, valeur))

    print(liste4)

    



class visu:

    def visu(self):
        vision = visualisation_table.visualisation_donnée(self)

        for i in vision:

            traitement_coul(vision[0][4])
            traitement_coul(vision[0][5])
            break



visu = visu()
visu.visu()
