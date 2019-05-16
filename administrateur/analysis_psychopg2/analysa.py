import psycopg2

from config import DATABASE
from config import USER
from config import HOST
from config import PASSWORD

from mode_w_data import traitement_coul
from palettecouleur import *



LISTE_FINAL = []


def couleur_vetement(liste):
    coul = []
    dico = {}
    
    for cle, valeur in DICO_COULEUR.items():
        dico[valeur] = 0
        
    for i in liste:
        for cle, valeur in DICO_COULEUR.items():
            if i[0] == cle:
                coul.append(DICO_COULEUR[cle])
                dico[valeur] += int(i[1])
                break

    terminal = []
    for cle, valeur in dico.items():
        if valeur != 0:
            terminal.append((cle, valeur))

    return terminal


def nombre_couleur(liste):

    
    c = 0
    for i in liste:
        nb = int(i[1])
        c += nb 
    return c



def pourcentage(bl, gr, cl, image, endroit):
    print(bl, gr,cl)
    total = int(bl) + int(gr) + int(cl)
    blanc = (100 * bl) / total
    gris = (100 * gr) / total
    couleur = (100 * cl) / total

    print('sur', total, 'couleurs il y a:', blanc,'% de blanc')
    print('sur', total, 'couleurs il y a:', gris,'% de gris')
    print('sur', total, 'couleurs il y a:', couleur,'% de coul')




    if couleur > 50.0:
        LISTE_FINAL.append(('couleur', image, endroit))
        c =  'couleur'
    elif gris > 60.0:
        LISTE_FINAL.append(('gris', image, endroit))
        c = 'gris'
    elif blanc > 50.0:
        LISTE_FINAL.append(('blanc', image, endroit))
        c = 'blanc'
    else:
        LISTE_FINAL.append(('none', image, endroit))
        c = 'couleur'


    return LISTE_FINAL, c

    
def liste_final(liste):
    print(liste)


#def data():
conn = psycopg2.connect(database='bobo',
                        user='postgres',
                        host='127.0.0.1',
                        password='tiotiotio333')

cur = conn.cursor()

cur.execute("""select * from bobo1;""")

conn.commit()


rows = cur.fetchall()
liste = [i for i in rows]

#def visuel_liste(liste):
for i in liste:


    liste_white_haut = []
    liste_couleur_haut = []
    liste_gris_haut = []


    liste_white_bas = []
    liste_couleur_bas = []
    liste_gris_bas = []



    print('nom:', i[1])

    print(i[1])
    print('haut')
    
    a = traitement_coul(str(i[4]))

    a = a[:-1]
    for j in a:
        for k in j:
 
            gris = str(k[0]).find('gray')
            blanc = str(k[0]).find('white')
            
            if gris >= 0:
                try:
                    nb = k[0][-2:]
                    nb = int(nb)
                    
                    if nb <= 24:
                        liste_coul_haut.append(k)
                        
                    elif nb > 24 and nb < 95:
                        liste_gris_haut.append(k)
                        
                    elif nb >= 95:
                        liste_white_haut.append(k) 
                except:
                    pass
            

            elif blanc >= 0:
                if k[0] == 'white':
                    pass
                else:
                    liste_white_haut.append(k)
            else:
                liste_couleur_haut.append(k)

        liste_couleur_haut = sorted(liste_couleur_haut, key=lambda s : s[1])
        liste_white_haut = sorted(liste_white_haut, key=lambda s : s[1])
        liste_gris_haut = sorted(liste_gris_haut, key=lambda s : s[1])
        


        print('\n')
        print('\n')
        print('WHITE', liste_white_haut)
        print('il y a : blanc', nombre_couleur(liste_white_haut))
        print('\n')
        print('GRIS', liste_gris_haut)
        print('il y a : gris', nombre_couleur(liste_gris_haut))
        print('\n')
        print('COUL', liste_couleur_haut)
        print('il y a coul : ', nombre_couleur(liste_couleur_haut))
        print('\n')
        print('\n')
        
        pour1 = pourcentage(nombre_couleur(liste_white_haut),
                    nombre_couleur(liste_gris_haut),
                    nombre_couleur(liste_couleur_haut), i[1], 'haut')
        
        print('\n\n')
        print(str(pour1[1]).upper())
        if pour1[1] == 'couleur':
            print('\n')
            un = couleur_vetement(liste_couleur_haut)
            print(un)
            print('\n')
        else:
            print(pour1[1])



        
    print(i[1])
    print('bas')


    b = traitement_coul(str(i[5]))
    b = b[:-1]
    for j in b:
        for k in j:

            gris = str(k[0]).find('gray')
            blanc = str(k[0]).find('white')
            
            if gris >= 0:
                try:
                    nb = k[0][-2:]
                    nb = int(nb)
                    if nb <= 24:
                        liste_couleur_bas.append(k)
                    elif nb > 24 and nb < 95:
                        liste_gris_bas.append(k)
                    elif nb >= 95:
                        liste_white_bas.append(k) 
                except:
                    pass
         
                    
                
            elif blanc >= 0:
                if k[0] == 'white':
                    pass
                else:
                    liste_white_bas.append(k)
            else:
                liste_couleur_bas.append(k)

        liste_couleur_bas = sorted(liste_couleur_bas, key=lambda s : s[1])
        liste_white_bas = sorted(liste_white_bas, key=lambda s : s[1])
        liste_gris_bas = sorted(liste_gris_bas, key=lambda s : s[1])
        
        print('\n\n')
        
        print('WHITE', liste_white_bas)
        print('il y a : blanc', nombre_couleur(liste_white_bas))
        print('\n')
        print('GRIS', liste_gris_bas)
        print('il y a : gris', nombre_couleur(liste_gris_bas))
        print('\n')
        print('COUL', liste_couleur_bas)
        print('il y a : couleur', nombre_couleur(liste_couleur_bas))
        print('\n')

        pour = pourcentage(nombre_couleur(liste_white_bas),
                    nombre_couleur(liste_gris_bas),
                    nombre_couleur(liste_couleur_bas), i[1], 'bas')
 
        print('\n\n')
        print(str(pour[1]).upper())
        if pour[1] == 'couleur':
            print('\n')
            un = couleur_vetement(liste_couleur_bas)
            print(un)
            print('\n')
        else:
            print(pour[1])


print('\n\n\n')
liste_final(LISTE_FINAL)

 




































    
