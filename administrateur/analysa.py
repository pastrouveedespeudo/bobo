import os
import psycopg2

from analysis_psychopg2.mode_w_data import traitement_coul


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


def analysa():
    
    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    liste = os.listdir()

    liste1 = []
    
    c = 0
    for i in liste:
        try:
            liste1.append((str(liste[c]), str(liste[c+1]), int(str(c) + str(c))))
            c+=2

        except:
            pass

    for i in liste1:
        print(i)
        a = coiffure('bobo1', 'haut', i[0])
        b = coiffure('bobo1', 'bas', i[0])
        print('ok')

        c = traitement_coul(str(a))
        print(c)
        print('\n\n\n\n\n\n\n\n\n\n')
        d = traitement_coul(str(b))
        print(d)
        
        break



    

analysa()
