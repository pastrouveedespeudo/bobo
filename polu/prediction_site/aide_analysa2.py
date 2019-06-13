import psycopg2
from statistics import *


def vision(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    
    cursor = conn.cursor()




    
    cursor.execute("""select angrais, saison, diesel, eruption, jour_nuit,
                   TRAFIQUE, HEURE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE,
                   POPULATION_ACTIVE_HABITANT, REGION_INDUSTRIEL_POLLUEE,
                   polenne, pos, météo, vent, pression, climat, incendie,
                   nombre_particule
                   from conditions2 where nom_ville=%s""", (ville,))


    conn.commit()


    rows = cursor.fetchall()
    liste = [i for i in rows]


    return liste




























