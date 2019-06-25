import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new


def visu_traffic(city):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""SELECT TRAFIQUE, nombre_particule FROM traffique
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_traffic(data_traffic):
    
    deaparture = []
    regular_day = []

 
    for i in data_traffic:
    
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'regulier jour':
            regular_day.append(int(i[1]))
        elif i[0] == 'depart_routier':
            deaparture.append(int(i[1]))

        print(i)
        
    data = len(deaparture) + len(regular_day)
    print(data)

    data_regular_day = moyenne(regular_day)
    data_deaparture = moyenne(deaparture)

    return data_regular_day[0], data_deaparture[0],\
            data_regular_day[1], data_deaparture[1], data

def diagram_traffic(data_regular_day, data_deaparture,
              er_regular_day, er_deaparture, save):


    
    plt.bar(range(2), [data_regular_day, data_deaparture],
                        width = 0.1, color = 'black',
                       yerr = [er_regular_day, er_deaparture],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['régulier jour', 'départ routier'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les départ routiers")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau
























































