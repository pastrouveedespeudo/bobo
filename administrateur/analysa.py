import os
import psycopg2
from operator import itemgetter


from static.bobo.mode_w_data import traitement_coul


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


    d = coiffure2('*', 'bobo1_coiffure')


    coif = [i[2] for i in d]
    print(coif)

    laliste1 = []

    for i in liste:
        if i == 'analyse_femme_haut.py' or  i == 'bobo.txt' or\
           i == 'config.py' or i == 'constante.py' or i == 'conteneur.py' or\
           i == 'coul.py' or i == 'coupe_analysis.py' or i=='constante.py' or\
           i == 'database.py' or i == 'mode_analyse.py' or i == 'mode_w_data.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i == 'traitement_bas1.jpg' or i == 'traitement_haut.jpg' or i == '__pycache__' or i=='bobo'\
           or i =='ess.py':
            pass
        else:
            laliste1.append(i)
    print(laliste1,'487498749879')
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

##    for i in pré_liste:
##        print(i)
##        print('\n\n')
        
    #print(pré_liste)
    return pré_liste
    #haut, bas, brun, 1a.jpg


    






















