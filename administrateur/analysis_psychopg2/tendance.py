import psycopg2
from .database import *
from .coupe_analysis import *

def dataaa():
    conn = psycopg2.connect(database='bobo',
                        user='postgres',
                        host='127.0.0.1',
                        password='tiotiotio333')

    cur = conn.cursor()

    cur.execute("""select * from analyse_donnee1;""")

    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste


def i_into_i(liste):

    liste1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]

    c=0
    d = 0
    for i in liste[0][0]:
        try:
            if liste[0][0][d] == ')' and\
               liste[0][0][d+1] == ',' and liste[0][0][d+2] == ' '\
               and liste[0][0][d+3] == '('\
               and liste[0][0][d+4] == '[':
                c+=1
            
            elif i == '[':
                pass

            else:
                liste1[c].append(i)

            d+=1
            
        except:
            pass
        
    return liste1
    
def unification(liste1):
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
                if k == '(' or k == '"' or k == ',' or k == ')'\
                   or k ==']':
                    pass
                else:
                    mot += k
            liste4.append(mot)

    return liste4    
    
def re_elment_de_liste(liste4):

    liste5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
    c = 0
    for i in liste4:
        if i == 'bas' or i == 'haut':
            liste5[c].append(i)
            c+=1
        elif i == '':
            pass
        else:
            liste5[c].append(i)


    liste6 = []
    for i in liste5:
        if i == []:
            pass
        else:
            liste6.append(i)

    return liste6


def mise_en_dico(liste6):

    liste7 = []
    dico = {}
##    print(liste6)
##    print('\n')
    c = 0
    for i in liste6:
        d = 0
        for j in i:
            try:
                dico[liste6[c][d]] = liste6[c][d + 1]
                d+=2
            except:
                pass
        liste7.append(dico)
        dico = {}
        c+=1

    
    return liste7


def determination_couleur(liste7):
    
    liste8 = []
    for i in liste7:
        #print(i)
        couleur = ''
        nombre = 0
        nom = []
        for cle, valeur in i.items():
            #print(cle, valeur)
            try:
                if int(valeur) > nombre:
                    nombre = 0
                    nombre += int(valeur)
                    couleur = ''
                    couleur = cle
                    
            except:
                if cle == 'blanc' and valeur == 0:
                    couleur = 'blanc'
                    nom.append(valeur)
                    
                elif cle == 'gris' and valeur == 0:
                    couleur = 'gris'
                    nom.append(valeur)
                    
            if cle[-4:] == '.jpg':
                nom.append((cle, valeur))
            elif valeur[-4:] == '.jpg':
                nom.append((cle, valeur))
                

            
        #print('DONC : ', couleur, nombre, nom)
        liste8.append((couleur, nom))
        
        #print('\n')

    #print(liste8)
    return liste8 

def les_tendances_couleurs(liste8):
    print('\n')

    data_coupe = recup2()
    coupa = []
    for i in data_coupe:
        coupa.append((i[1], i[2]))

    coupa2 = []
    for i in sorted(coupa):
        coupa2.append(i[1])



    c = 0
    liste9 = []
    for i in liste8:
        #print(i)
        if i[0] == '':
            if c%2 == 0:
                ou = 'haut'
            else:
                ou = 'bas'
            #print(i[1][0][0], i[1][0][1], ou)
            liste9.append((i[1][0][0], i[1][0][1], ou))
        else:
            try:
                if int(i[1][0][0]):
                    if c%2 == 0:
                        ou = 'haut'
                    else:
                        ou = 'bas'
                    #print(i[0], i[1][0][1], ou)
                    liste9.append((i[0], i[1][0][1], ou))
            except:
                #print(i[0], i[1][0][0], i[1][0][1])
                liste9.append((i[0], i[1][0][0], i[1][0][1]))
            

        c+=1

    a = 0
    for i in coupa2:
        liste9[a] = liste9[a] + (i,)
        liste9[a+1] = liste9[a+1] + (i,)
        a+=2
        
    print(liste9)
        

    return liste9


def analyse_tendance(liste9):

    c = 0
    liste_haut_marron = []
    liste_haut_blond = []
    liste_haut_chatain = []
    
    for i in liste:
        try:
            print(liste[c][0], liste[c][1], liste[c][3])
            
            if liste[c][3] == 'marron':
                liste_haut_marron.append(liste[c][0])
            elif liste[c][3] == 'blond':
                liste_haut_blond.append(liste[c][0])
            elif liste[c][3] == 'chatin':
                liste_haut_chatain.append(liste[c][0])
            
            c+=2
            
        except:
            pass


    print(liste_haut_marron,
          liste_haut_blond,
          liste_haut_chatain)


    dico_haut_marron = {}
    dico_haut_blond = {}
    dico_haut_chatin = {}
    
    for i in liste_haut_marron:
        dico_haut_marron[i] = 0
        
    for i in liste_haut_blond:
        dico_haut_blond[i] = 0
        
    for i in liste_haut_chatain:
        dico_haut_chatin[i] = 0


    for i in liste_haut_marron:
        for cle, valeur in dico_haut_marron.items():
            if i == cle:
                dico_haut_marron[cle] += 1

    for i in liste_haut_blond:
        for cle, valeur in dico_haut_blond.items():
            if i == cle:
                dico_haut_blond[cle] += 1

    for i in liste_haut_chatain:
        for cle, valeur in dico_haut_chatin.items():
            if i == cle:
                dico_haut_chatin[cle] += 1

                


    liste_bas_marron = []
    liste_bas_blond = []
    liste_bas_chatain = []

    d = 1
    for i in liste:
        try:
            print(liste[d][0], liste[d][1], liste[d][3])

            if liste[d][3] == 'marron':
                liste_bas_marron.append(liste[d][0])
            elif liste[d][3] == 'blond':
                liste_bas_blond.append(liste[d][0])
            elif liste[d][3] == 'chatin':
                liste_bas_chatain.append(liste[d][0])

            d+=2
        except:
            pass
    
       
    print(liste_bas_marron,
          liste_bas_blond,
          liste_bas_chatain)

    dico_bas_marron = {}
    dico_bas_blond = {}
    dico_bas_chatin = {}
    
    for i in liste_bas_marron:
        dico_bas_marron[i] = 0
        
    for i in liste_bas_blond:
        dico_bas_blond[i] = 0
        
    for i in liste_bas_chatain:
        dico_bas_chatin[i] = 0


    for i in liste_bas_marron:
        for cle, valeur in dico_bas_marron.items():
            if i == cle:
                dico_bas_marron[cle] += 1

    for i in liste_bas_blond:
        for cle, valeur in dico_bas_blond.items():
            if i == cle:
                dico_bas_blond[cle] += 1

    for i in liste_bas_chatain:
        for cle, valeur in dico_bas_chatin.items():
            if i == cle:
                dico_bas_chatin[cle] += 1



    print('\n\n')
    print(dico_haut_marron, dico_haut_blond, dico_haut_chatin)
    print(dico_bas_marron, dico_bas_blond, dico_bas_chatin)

    haut = [dico_haut_marron, dico_haut_blond, dico_haut_chatin]
    bas = [dico_bas_marron, dico_bas_blond, dico_bas_chatin]
    
    return haut, bas


def dico_max(dico):
    nb = 0
    coul = ''
    for cle, valeur in dico.items():
        if valeur > nb:
            nb = 0
            nb += valeur
            coul = ''
            coul = cle
            
    return coul, nb

    
def analyse_tendance(liste):

    c = 0
    liste_haut_marron = []
    liste_haut_blond = []
    liste_haut_chatain = []
    
    for i in liste:
        try:
            print(liste[c][0], liste[c][1], liste[c][3])
            
            if liste[c][3] == 'marron':
                liste_haut_marron.append(liste[c][0])
            elif liste[c][3] == 'blond':
                liste_haut_blond.append(liste[c][0])
            elif liste[c][3] == 'chatin':
                liste_haut_chatain.append(liste[c][0])
            
            c+=2
            
        except:
            pass


    print(liste_haut_marron,
          liste_haut_blond,
          liste_haut_chatain)


    dico_haut_marron = {}
    dico_haut_blond = {}
    dico_haut_chatin = {}
    
    for i in liste_haut_marron:
        dico_haut_marron[i] = 0
        
    for i in liste_haut_blond:
        dico_haut_blond[i] = 0
        
    for i in liste_haut_chatain:
        dico_haut_chatin[i] = 0


    for i in liste_haut_marron:
        for cle, valeur in dico_haut_marron.items():
            if i == cle:
                dico_haut_marron[cle] += 1

    for i in liste_haut_blond:
        for cle, valeur in dico_haut_blond.items():
            if i == cle:
                dico_haut_blond[cle] += 1

    for i in liste_haut_chatain:
        for cle, valeur in dico_haut_chatin.items():
            if i == cle:
                dico_haut_chatin[cle] += 1

                


    liste_bas_marron = []
    liste_bas_blond = []
    liste_bas_chatain = []

    d = 1
    for i in liste:
        try:
            print(liste[d][0], liste[d][1], liste[d][3])

            if liste[d][3] == 'marron':
                liste_bas_marron.append(liste[d][0])
            elif liste[d][3] == 'blond':
                liste_bas_blond.append(liste[d][0])
            elif liste[d][3] == 'chatin':
                liste_bas_chatain.append(liste[d][0])

            d+=2
        except:
            pass
    
       
    print(liste_bas_marron,
          liste_bas_blond,
          liste_bas_chatain)

    dico_bas_marron = {}
    dico_bas_blond = {}
    dico_bas_chatin = {}
    
    for i in liste_bas_marron:
        dico_bas_marron[i] = 0
        
    for i in liste_bas_blond:
        dico_bas_blond[i] = 0
        
    for i in liste_bas_chatain:
        dico_bas_chatin[i] = 0


    for i in liste_bas_marron:
        for cle, valeur in dico_bas_marron.items():
            if i == cle:
                dico_bas_marron[cle] += 1

    for i in liste_bas_blond:
        for cle, valeur in dico_bas_blond.items():
            if i == cle:
                dico_bas_blond[cle] += 1

    for i in liste_bas_chatain:
        for cle, valeur in dico_bas_chatin.items():
            if i == cle:
                dico_bas_chatin[cle] += 1



    print('\n\n')
    print(dico_haut_marron, dico_haut_blond, dico_haut_chatin)
    print(dico_bas_marron, dico_bas_blond, dico_bas_chatin)
    print('\n\n')
    print('\n\n')


    haut_marron = dico_max(dico_haut_marron)
    haut_blond = dico_max(dico_haut_blond)
    haut_chatain = dico_max(dico_haut_chatin)

    bas_marron = dico_max(dico_bas_marron)
    bas_blond = dico_max(dico_bas_blond)
    bas_chatain = dico_max(dico_bas_chatin)

    
    print(haut_marron, haut_blond, haut_chatain)
    print(bas_marron, bas_blond, bas_chatain)


    marron = [haut_marron, bas_marron]
    blond = [haut_blond, bas_blond]
    chatain = [haut_chatain, bas_chatain]

    print(marron, blond, chatain)
    return marron, blond, chatain






    











##liste = data()
##liste1 = i_into_i(liste)
##liste2 = unification(liste1)
##liste3 = suppression_en_trop(liste2)
##liste6 = re_elment_de_liste(liste3)
##liste7 = mise_en_dico(liste6)
##liste8 = determination_couleur(liste7)
##liste9 = les_tendances_couleurs(liste8)
##analyse_tendance(liste9)






