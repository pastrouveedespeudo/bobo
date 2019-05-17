import psycopg2
from database import *


def data():
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
    print(liste6)
    print('\n')
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
        print(i)
        couleur = ''
        nombre = 0
        nom = []
        for cle, valeur in i.items():
            print(cle, valeur)
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
                

            
        print('DONC : ', couleur, nombre, nom)
        liste8.append((couleur, nom))
        
        print('\n')

    print(liste8)
    return liste8 

def les_tendances_couleurs(liste8):
    print('\n')

    c = 0
    liste9 = []
    for i in liste8:
        #print(i)
        if i[0] == '':
            if c%2 == 0:
                ou = 'haut'
            else:
                ou = 'bas'
            print(i[1][0][0], i[1][0][1], ou)
            liste9.append((i[1][0][0], i[1][0][1], ou))
        else:
            try:
                if int(i[1][0][0]):
                    if c%2 == 0:
                        ou = 'haut'
                    else:
                        ou = 'bas'
                    print(i[0], i[1][0][1], ou)
                    liste9.append((i[0], i[1][0][1], ou))
            except:
                print(i[0], i[1][0][0], i[1][0][1])
                liste9.append((i[0], i[1][0][0], i[1][0][1]))
            

        c+=1

    

    print(liste9)

    return liste9





















liste = data()
liste1 = i_into_i(liste)
liste2 = unification(liste1)
liste3 = suppression_en_trop(liste2)
liste6 = re_elment_de_liste(liste3)
liste7 = mise_en_dico(liste6)
liste8 = determination_couleur(liste7)
les_tendances_couleurs(liste8)



