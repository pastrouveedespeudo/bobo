import psycopg2
import time


from analyse import *
from analysebis import *



def donnée():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    liste1 = ['angrais', 'incendie', 'pression',
              'vent', 'météo', 'climat', 'saison',
              'region_industrielle',
              'population_active', 'traffique',
              'heure', 'weekend', 'bouchon',
              'activité', 'diesel', 'eruption',
              'jour_nuit', 'polenne', 'voisin',
              'pos_france']

    liste2 = ['conditions']


##    for condi in liste1:
##        
##        cursor.execute("""select *  from {};""".format(condi))
##
##
##        conn.commit()
##
##
##
##      
##        rows = cursor.fetchall()
##        liste = [i for i in rows]
##
##
##        for i in liste:
##            print(condi)
##            print(i[-1], i[-2])
##
##        print('\n\n')



    liste_ville = ['lyon']
    #liste_ville = ['lyon', 'paris', 'marseille']

    LISTE_DEJA = []
    
    for i in liste_ville:

        cursor.execute("""select *  from conditions2 where nom_ville = '{}';""".format(i))


        conn.commit()

        rows = cursor.fetchall()
        liste = [i for i in rows]
        #faut voir si toutes les conditions mini se mettent si oui en faire la moyenne et a chaque fois la renouveller
        
        début_boucle = True

##        minimum = condition_min(liste, LISTE_DEJA)
##        liste1, liste2, liste3, liste4 = différence(liste, minimum, LISTE_DEJA)
##        a = différences(liste1, liste2, liste3, liste4, LISTE_DEJA)

##                
##        oContinuer = True
##        
##        while oContinuer:
##            time.sleep(0.3)
##            if début_boucle != False:
##                minimum = condition_min(liste, LISTE_DEJA)
##                liste1, liste2, liste3, liste4 = différence(liste, minimum, LISTE_DEJA)
##                a = différences(liste1, liste2, liste3, liste4, LISTE_DEJA)
##                
##                #print(LISTE_DEJA)
##                #print(a)
##                print('\n')
##
##                début_boucle = début()
##                
##            else:
##
##                liste1, liste2, liste3, liste4 = différence(liste, a, LISTE_DEJA)
##                a = différences(liste1, liste2, liste3, liste4, LISTE_DEJA)
##                
##                #print(LISTE_DEJA)
##                #print(a)
##                print('\n')

                

            
            
        print('\n')
        print('\n')
        print('\n')


donnée()













