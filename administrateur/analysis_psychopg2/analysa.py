import os
import psycopg2
from operator import itemgetter


from mode_w_data import traitement_coul


def coiffure(table, attribut, image):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333') 

    cur = conn.cursor()
    

    
    cur.execute("""select {} from {}
                WHERE image = '{}';""".format(attribut, table, image))

    
    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste

def coiffure2(table, attribut):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333') 

    cur = conn.cursor()
    

    
    cur.execute("""select {} from {};""".format(table, attribut))

    
    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste



def analysa():
    
    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    liste = os.listdir()

    liste1 = []


    d = coiffure2('*', 'bobo1')


    coif = [i[2] for i in d]
 

    laliste1 = []

    for i in liste:
        if i == 'analyse_femme_haut.py' or  i == 'bobo.txt' or\
           i == 'config.py' or i == 'constante.py' or i == 'conteneur.py' or\
           i == 'coul.py' or i == 'coupe_analysis.py' or i=='constante.py' or\
           i == 'database.py' or i == 'mode_analyse.py' or i == 'mode_w_data.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i == 'traitement_bas1.jpg' or i == 'traitement_haut.jpg' or i == '__pycache__' or i=='bobo'\
           or i =='ess.py' or i =='analysa.py':
            pass
        else:
            laliste1.append(i)

    c = 0
    for i in laliste1:
        try:
            liste1.append((str(laliste1[c]), str(laliste1[c+1]), int(str(c) + str(c))))
            c+=2

        except:
            pass

    pré_liste_haut = []
    pré_liste_bas = []
    pré_liste = []

    compteur = 0
    for i in liste1:

        a = coiffure('bobo1', 'haut', i[0])
        b = coiffure('bobo1', 'bas', i[0])
        
    
        c = traitement_coul(str(a))

    
        try:
            for j in c:
                for k in j:
                    pré_liste_haut.append(k)
                    
        except:
            pass

        finally:
            pré_liste_haut = sorted(pré_liste_haut, key=lambda s : s[1])
          



        d = traitement_coul(str(b))
        
        try:
            for j in d:
                for k in j:
                    pré_liste_bas.append(k)
                    
        except:
            pass

        finally:
            pré_liste_bas = sorted(pré_liste_bas, key=lambda s : s[1])
           
            
            pré_liste.append([pré_liste_haut, pré_liste_bas, coif[compteur] ,i[0]])
          
            
        pré_liste_haut = []
        pré_liste_bas = []
        compteur += 1


        

    return pré_liste
    #haut, bas, brun, 1a.jpg


def analyse_couleur(liste):


    c = 0
    for i in liste:
            
        liste_white_haut = []
        liste_couleur_haut = []
        liste_gris_haut = []


        liste_white_bas = []
        liste_couleur_bas = []
        liste_gris_bas = []

        
        print('debut analyse de:', i[3])
        print('\n')
        print('\n')
         
        print('le haut:')
        
        print('\n')
        print(i[0])
        print('\n')
        
        for j in i[0]:
 
            gris = str(j[0]).find('gray')
            blanc = str(j[0]).find('white')
 
            if gris >= 0:
                try:
                    nb = j[0][-2:]
                    nb = int(nb)
                    
                    if nb <= 24:
                        liste_coul_haut.append(j)
                        
                    elif nb > 24 and nb < 95:
                        liste_gris_haut.append(j)
                        
                    elif nb >= 95:
                        liste_white_haut.append(j) 
                except:
                    pass
                
   
            elif blanc >= 0:
                liste_white_bas.append(j)
            else:
                liste_couleur_bas.append(j)

                
        print('\n')
        print('\n\n\n\n\n\n\n\n\n\n')
        print('WHITE', liste_white_haut)
        print('\n\n')
        print('GRIS', liste_gris_haut)
        print('\n\n')
        print('COUL', liste_couleur_haut)
        
        print('\n\n')
        print('\n')
        print('\n')

        print('le bas:')
        print('\n')
        print('\n')
        
        print(i[1])
        
        for j in i[1]:

            gris = str(j[0]).find('gray')
            blanc = str(j[0]).find('white')
            
            if gris >= 0:
                try:
                    nb = j[0][-2:]
                    nb = int(nb)
                    if nb <= 24:
                        liste_couleur_bas.append(j)
                    elif nb > 24 and nb < 95:
                        liste_gris_bas.append(j)
                    elif nb >= 95:
                        liste_white_bas.append(j) 
                except:
                    pass
         
                    
                
            elif blanc >= 0:
                liste_white_bas.append(j)
            else:
                liste_couleur_bas.append(j)
      
        print('\n\n\n\n\n\n\n\n\n\n')
        
        print('WHITE', liste_white_bas)
        print('\n\n')
        print('GRIS', liste_gris_bas)
        print('\n\n')
        print('COUL', liste_couleur_bas)
        print('\n\n')


 


        break



def nombre_couleur(liste):

    

    for i in liste:
        pass



    



liste = analysa()
liste1 = analyse_couleur(liste)





















