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

    print(liste2)



    dico = {}



class visu:

    def visu(self):
        vision = visualisation_table.visualisation_donnée(self)

        for i in vision:

            traitement_coul(vision[0][4])
            traitement_coul(vision[0][5])
            break



visu = visu()
visu.visu()
