import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD
from .CONFIG import LISTE1
from .CONFIG import LISTE5

from .coupe_analysis import recup2



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
    """here we unificate the last list"""
    
    liste2 = []
    for i in liste1:
        if i == []:
            pass
        else:
            i = "".join(i)
            liste2.append(i)
            
    return liste2



def suppression_en_trop(liste2):
    """we clean the parentheses, hooks too much"""
    
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
    """here we sort our data by list list,
    indeed we have mixed up and down data"""
    
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
    """here we organize it
    in dictionnary"""
    
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
            if counter % 2 == 0:
                ou = 'haut'
            else:
                ou = 'bas'
            liste9.append((i[1][0][0], i[1][0][1], ou))
            
        else:
            try:
                if int(i[1][0][0]):
                    if counter % 2 == 0:
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




def dico_max(dico):
    
    nb = 0
    coul = ''
    
    for cle, valeur in dico.items():
        if valeur > nb:
            
            nb = 0
            nb += valeur
            coul = ''
            coul = cle

    return coul


def analyse_tendance_funct_1(liste, c):

    liste1 = []
    liste2 = []
    liste3 = []
    
    for i in liste:
        try:
            if liste[c][3] == 'marron':
                liste1.append(liste[c][0])
            elif liste[c][3] == 'blond':
                liste2.append(liste[c][0])
            elif liste[c][3] == 'chatin':
                liste3.append(liste[c][0])
            
            c+=2
            
        except:
            pass

    return liste1,\
           liste2,\
           liste3


def analyse_tendance_funct_2(liste):
    
    dico = {}
    
    for i in liste:
        dico[i] = 0

    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[cle] += 1

    return dico



def analyse_tendance(liste):
    """We define color from picture"""

    #define color of t-shirt
    funt1 = analyse_tendance_funct_1(liste, 0)

    liste_haut_marron = funt1[0]
    liste_haut_blond = funt1[1]
    liste_haut_chatain = funt1[2]

    dico_haut_marron = analyse_tendance_funct_2(liste_haut_marron)
    dico_haut_blond = analyse_tendance_funct_2(liste_haut_blond)
    dico_haut_chatin = analyse_tendance_funct_2(liste_haut_chatain)


    #define color of jean
    funt2 = analyse_tendance_funct_1(liste, 1)


    liste_bas_marron = funt2[0]
    liste_bas_blond = funt2[1]
    liste_bas_chatain = funt2[2]


    dico_bas_marron = analyse_tendance_funct_2(liste_bas_marron)
    dico_bas_blond = analyse_tendance_funct_2(liste_bas_blond)
    dico_bas_chatin = analyse_tendance_funct_2(liste_bas_chatain)


    #Take the most value
    haut_marron = dico_max(dico_haut_marron)
    haut_blond = dico_max(dico_haut_blond)
    haut_chatain = dico_max(dico_haut_chatin)

    bas_marron = dico_max(dico_bas_marron)
    bas_blond = dico_max(dico_bas_blond)
    bas_chatain = dico_max(dico_bas_chatin)

 
    marron = [haut_marron, bas_marron]
    blond = [haut_blond, bas_blond]
    chatain = [haut_chatain, bas_chatain]

    print(marron, blond, chatain)
    return marron, blond, chatain




def la_tendance():
    
    liste = dataaa()
    liste1 = i_into_i(liste)
    liste2 = unification(liste1)
    liste3 = suppression_en_trop(liste2)
    liste6 = re_elment_de_liste(liste3)
    liste7 = mise_en_dico(liste6)
    liste8 = determination_couleur(liste7)
    liste9 = les_tendances_couleurs(liste8)
    liste10 = analyse_tendance(liste9)

    return liste10



#la_tendance()











