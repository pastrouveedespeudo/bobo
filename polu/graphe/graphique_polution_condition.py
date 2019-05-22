import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import moyenne

def visu(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT particule FROM ville
                    where nom_ville=%s
                    order by particule DESC""", (ville,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return max(liste), min(liste)

def visu2(max):

    maxi = max[0]

    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM ville
                    where particule = %s""",  (maxi,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu3(min):

    mini = min[0]

    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM ville
                    where particule = %s""",  (mini,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


##a = visu('marseille')
##b = visu2(a[0])
##c = visu2(a[1])
##c = set(c)
##b = set(b)
##for i in c:
##    print(i)
##
##print('\n')
##
##for i in b:
##    print(i)

















##donnée = traitement_ville(a)
##
##diagramme(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
##          donnée[5])
