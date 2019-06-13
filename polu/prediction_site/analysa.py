

import psycopg2
from math import *

def moyenne(tableau):
    return sum(tableau, 0.0) / len(tableau)


def variance(tableau):
    m=moyenne(tableau)
    return moyenne([(x-m)**2 for x in tableau])



def all():
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    aaa = 'lyon'

    cursor.execute("""select *  from conditions2 where nom_ville = '{}' order by nombre_particule ;""".format(aaa))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]
   
    return liste[0]





def all1():
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    aaa = 'lyon'

    cursor.execute("""select *  from conditions2 where nom_ville = '{}' order by nombre_particule ;""".format(aaa))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    for i in liste:
        print(i[2:-2])
        print('\n')
    

   

    








all1()
















