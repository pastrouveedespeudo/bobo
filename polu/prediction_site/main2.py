import psycopg2
import datetime


from angrais import *
from climat import *
from diesel import *
from eruption import *
from incendie import *
from jour_nuit import *
from météo import *
from particule import *
from polenne import *
from socio import *
from trafique import *

from database2 import *



def heure_jour():
    
    date = datetime.datetime.now()
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute

    jour = str(jour)+'_'+str(mois)+'_'+str(année)
    heure = str(heure)+'_'+str(minute)
    
    return jour, heure


heure_jour = heure_jour()


liste = ['lyon', 'paris','marseille']
#liste = ['marseille']
#liste = ['lyon']
#liste = ['paris']
for i in liste:

    print('TOUR: ', i)
    m = particule2(i)
    #print('taux de particule de', m, 'a', i)


    a = periode_angrais()
    #print('période engrais ?', a)
    insertion_angrais(i, a, heure_jour[0], heure_jour[1], m)

    c = saison()
    #print('saison : ', c)
    insertion_saison(i,c, heure_jour[0], heure_jour[1], m)

    d = recup_balise()
    #print('augmentation du prix barille de diesel, du d+ et du dollar : ', d)
    insertion_diesel(i, d, heure_jour[0], heure_jour[1], m)


    e = eruption()
    #print('erruption cet semaine ? le :', e)
    insertion_eruption(i,  e, heure_jour[0], heure_jour[1], m)

    g = nuit_jour()
    #print('nous sommes en periode de :', g)
    insertion_nuit_jour(i, g, heure_jour[0], heure_jour[1], m)

    r = trafique_circulation()
    #print('aujourd\'hui est il un départ routier ?', r)
    insertion_trafique_circulation(i, r, heure_jour[0], heure_jour[1], m)

    s = heure_de_pointe()
    #print('est ce une heure de pointe ?', s)
    insertion_heure_de_pointe(i,  s, heure_jour[0], heure_jour[1], m)

    t = habitude()
    #print('quel periode de la semaine ?', t)
    insertion_habitude(i, t, heure_jour[0], heure_jour[1], m)

    u = bouchons(i)
    #print('a', i, 'il y a un','',  u, 'bouchon')
    insertion_bouchon(i, u, heure_jour[0], heure_jour[1], m)

    v = activité_execptionnelle(i)
    #print('a', i ,'il y a manif ou pas ?', v)
    insertion_activité_execptionnelle( i, v, heure_jour[0], heure_jour[1], m)

    q = habitant(i)
    #print('population active de', i, 'de :', q)
    insertion_habitant(i, q, heure_jour[0], heure_jour[1], m)

    n = industrie(i)
    #print(i,'est dans une zone industrielle polluante ?', n)
    insertion_industrie(i, n, heure_jour[0], heure_jour[1], m)

    o = polenne(i)
    #print('le taux de polenne a ', i, 'est : ', o)
    insertion_polenne(i, o, heure_jour[0], heure_jour[1], m)

    l = france(i)
    #print(i, 'est', l, 'en france')
    insertion_france(i, l, heure_jour[0], heure_jour[1], m)

    h = recuperation_donnée_météo(i)
    #print('il fait', h, 'à', i)
    insertion_météo(i, h, heure_jour[0], heure_jour[1], m)

    j = vent(i)
    #print('le vent est :', j, 'a', i)
    insertion_vent(i, j, heure_jour[0], heure_jour[1], m)


    k = pression(i)
    #print('la pression est', k,'a', i)
    insertion_pression(i, k, heure_jour[0], heure_jour[1], m)

    b = recuperation_donnée_température(i)
    #print('la température est dans une plage de: ', b)
    insertion_température(i, b, heure_jour[0], heure_jour[1], m)

    f = incendie(i)
    #print('incendie a', i ,'ojd ?', f)
    insertion_incendie(i, f, heure_jour[0], heure_jour[1], m)


    #print('\n')





    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    
    sql = ("""INSERT INTO conditions2
            (nom_ville, pression, vent,
            météo, climat, saison,
              REGION_INDUSTRIEL_POLLUEE,
              POPULATION_ACTIVE_HABITANT,
              TRAFIQUE, HEURE, WEEKEND,
              BOUCHON, ACTIVITE_EXEPTIONNELLE
              , angrais, diesel,
              eruption,incendie,
              jour_nuit, polenne,
              pos, heure_donnée, date,
              nombre_particule)
              VALUES (%s,%s,%s,
              %s,%s,%s,%s,
              %s,%s,
              %s,%s,%s,%s,
              %s,%s,%s,%s,
              %s,%s,
              %s,%s, %s, %s);
            """)


    values = (i, k, j, h, b, c,
              n, q,
              r, s, t, u, v
              , a, d, e, f, g,
              o, l, heure_jour[1], heure_jour[0], m)

    cursor.execute(sql, values)    
    conn.commit()

        

 
    









