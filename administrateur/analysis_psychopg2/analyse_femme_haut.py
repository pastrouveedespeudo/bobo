import psycopg2

from config import DATABASE
from config import USER
from config import HOST
from config import PASSWORD

from mode_w_data import traitement_coul




LISTE_FINAL = []


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



    if couleur > 25.0:
        LISTE_FINAL.append(('couleur', image, endroit))

    elif couleur > blanc and couleur > gris:
        LISTE_FINAL.append(('couleur', image, endroit))

    elif gris > blanc + 35 and couleur < 10:
        LISTE_FINAL.append(('gris', image, endroit))

    elif blanc > gris + 50 and couleur < 25.0:
        LISTE_FINAL.append(('blanc', image, endroit))

    else:
        LISTE_FINAL.append(('none', image, endroit))



    return LISTE_FINAL
    
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


##        print('\n')
##        print('WHITE', liste_white_haut)
##        print('il y a : blanc', nombre_couleur(liste_white_haut))
##        print('GRIS', liste_gris_haut)
##        print('il y a : gris', nombre_couleur(liste_gris_haut))
##        print('COUL', liste_couleur_haut)
##        print('il y a coul : ', nombre_couleur(liste_couleur_haut))
        
        
        pourcentage(nombre_couleur(liste_white_haut),
                    nombre_couleur(liste_gris_haut),
                    nombre_couleur(liste_couleur_haut), i[1], 'haut')
        
        print('\n\n')




        
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
      
        print('\n\n\n\n\n\n\n\n\n\n')
        
##        print('WHITE', liste_white_bas)
##        print('il y a : blanc', nombre_couleur(liste_white_bas))
##        print('\n\n')
##        print('GRIS', liste_gris_bas)
##        print('il y a : gris', nombre_couleur(liste_gris_bas))
##        print('\n\n')
##        print('COUL', liste_couleur_bas)
##        print('il y a : couleur', nombre_couleur(liste_couleur_bas))
##        print('\n\n')

        pourcentage(nombre_couleur(liste_white_bas),
                    nombre_couleur(liste_gris_bas),
                    nombre_couleur(liste_couleur_bas), i[1], 'bas')
 






    liste_final(LISTE_FINAL)

 






































    
