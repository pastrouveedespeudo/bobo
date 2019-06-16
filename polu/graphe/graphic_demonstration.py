import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .function_graph import moyenne
from .function_graph import new

def visu_demonstration(city):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""SELECT ACTIVITE_EXEPTIONNELLE, nombre_particule FROM activité
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatement_demonstration(data_demonstration):
    demonstration = []
    no_demonstration = []
    
    for i in data_demonstration:
        print(i)
        if i[1] == 'None' or i[1] == None\
           or i[0] == 'None' or i[0] == None:
            pass
        elif i[0] == 'manifestation':
            demonstration.append(int(i[1]))
        elif i[0] == 'non_manifestation':
            no_demonstration.append(int(i[1]))



    data = len(demonstration) + len(no_demonstration)
    print(data)


    data_demon = moyenne(demonstration)
    data_no_demon = moyenne(no_demonstration)


    return data_demon[0], data_no_demon[0],\
            data_demon[1], data_no_demon[1], data


def diagram_demonstration(data_demons, data_no_demons,
              error_demons, error_no_demons, save):


    
    plt.bar(range(2), [data_demons, data_no_demons],
                        width = 0.1, color = 'red',
                       yerr = [error_demons, error_no_demons],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['manifestation', 'non manifestation'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les manifestation")
    
    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')
    return nouveau


























































