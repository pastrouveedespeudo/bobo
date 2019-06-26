import psycopg2
from database import *


from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD
from CONFIG import LISTE1
from CONFIG import LISTE5

from coupe_analysis import recup2


def dataaa():
    """Here we call database and select
    data recorded"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cur = conn.cursor()

    cur.execute("""select * from analyse_donnee1;""")

    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste


def i_into_i(liste):
    """Here we clean list from dataaa()"""
    

    counter = 0
    counter1 = 0
    
    for i in liste[0][0]:
        
 
        if liste[0][0][counter1] == ')' and\
           liste[0][0][counter1 + 1] == ',' and\
           liste[0][0][counter1 + 2] == ' ' and\
           liste[0][0][counter1 + 3] == '(' and\
           liste[0][0][counter1 + 4] == '[':
            counter += 1
        
        elif i == '[':
            pass

        else:
            LISTE1[counter].append(i)

        counter1 += 1
            
     


    return LISTE1


def unification(liste1):
    """here we """
    liste2 = []
    
    for i in liste1:
        if i == []:
            pass
        
        else:
            i = "".join(i)
            liste2.append(i)


    return liste2



def suppression_en_trop(liste2):

    liste3 = []
    
    for i in liste2:
        liste3.append(i.split())

    liste4 = []
    for i in liste3:
        
        for j in i:
            mot = ''
            
            for k in j:
                if k == '(' or\
                   k == '"' or\
                   k == ',' or\
                   k == ')' or\
                   k ==']':
                    pass
                
                else:
                    mot += k
                    
            liste4.append(mot)

    return liste4 



def re_elment_de_liste(liste4):

    counter = 0
    for i in liste4:
        
        if i == 'bas' or\
           i == 'haut':
            
            LISTE5[counter].append(i)
            counter += 1
            
        elif i == '':
            pass
        
        else:
            LISTE5[counter].append(i)

    liste6 = []
    for i in LISTE5:
        
        if i == []:
            pass

        else:
            liste6.append(i)

    return liste6


def mise_en_dico(liste6):

    liste7 = []
    dico = {}

    counter = 0
    for i in liste6:
        
        counter1 = 0
        
        for j in i:
            
            try:
                dico[liste6[counter][counter1]] = liste6[counter][counter1 + 1]
                counter1 += 2
                
            except:
                pass

            
        liste7.append(dico)
        dico = {}
        counter += 1

    return liste7




def determination_couleur(liste7):
    """Here we associate the the biggest
    score to the picture"""

    liste8 = []
    for i in liste7:

        couleur = ''
        nombre = 0
        nom = []
        
        for cle, valeur in i.items():

            try:
                if int(valeur) > nombre:
                    nombre = 0
                    nombre += int(valeur)
                    couleur = ''
                    couleur = cle
                    
            except:
                if cle == 'blanc' and\
                   valeur == 0:
                    
                    couleur = 'blanc'
                    nom.append(valeur)
                    
                elif cle == 'gris' and\
                     valeur == 0:
                    
                    couleur = 'gris'
                    nom.append(valeur)
                    
            if cle[-4:] == '.jpg':
                nom.append((cle, valeur))
                
            elif valeur[-4:] == '.jpg':
                nom.append((cle, valeur))
                

        liste8.append((couleur, nom))
        
    return liste8 


def les_tendances_couleurs(liste8):
    """We reunicate all data, t-shirt,
    jean and haircut"""

    
    #We call class visu from coupe_analysis.py
    #It return hair color of picture
    data_coupe = recup2()
    

    coupa = [(i[1], i[2]) for i in data_coupe] 
    coupa2 = [i[1] for i in sorted(coupa)]

    counter = 0
    liste9 = []
    for i in liste8:

        if i[0] == '':
            if counter%2 == 0:
                ou = 'haut'
            else:
                ou = 'bas'
            liste9.append((i[1][0][0], i[1][0][1], ou))
            
        else:
            try:
                if int(i[1][0][0]):
                    if counter%2 == 0:
                        ou = 'haut'
                    else:
                        ou = 'bas'
                    
                    liste9.append((i[0], i[1][0][1], ou))
            except:
                liste9.append((i[0], i[1][0][0], i[1][0][1]))
            

        counter += 1

    counter1 = 0
    for i in coupa2:
        liste9[counter1] = liste9[counter1] + (i,)
        liste9[counter1 + 1] = liste9[counter1 + 1] + (i,)
        counter1 += 2
        
    return liste9









liste = dataaa()
liste1 = i_into_i(liste)
liste2 = unification(liste1)
liste3 = suppression_en_trop(liste2)
liste6 = re_elment_de_liste(liste3)

liste7 = mise_en_dico(liste6)
liste8 = determination_couleur(liste7)
liste9 = les_tendances_couleurs(liste8)
analyse_tendance(liste9)

















