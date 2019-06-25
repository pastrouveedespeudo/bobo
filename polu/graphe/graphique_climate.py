import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
from .function_graph import moyenne
import os
import shutil
from .function_graph import new

def visuuu_climat(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""SELECT climat, nombre_particule FROM climat
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitementtt_climat(donnée):


    inf_zero = [10]
    zero_dix = [10]
    onze_vingt = [10]
    vingtun_trente = [10]
    trente_un_quarante = [10]
    supp_quarante  = [10]
   
    for i in donnée:
    
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        
        elif i[0] == '>0':
            inf_zero.append(int(i[1]))
            
        elif i[0] == '0_10':
            zero_dix.append(int(i[1]))
            
        elif i[0] == '11_20':
            onze_vingt.append(int(i[1]))
            
        elif i[0] == '21_30':
            vingtun_trente.append(int(i[1]))
            
        elif i[0] == '31_40':
            trente_un_quarante.append(int(i[1]))

        elif i[0] == '>40':
            supp_quarante.append(int(i[1]))

        print(i)

    data = len(inf_zero) + len(zero_dix) + len(onze_vingt) + len(vingtun_trente) + len(trente_un_quarante) + len(supp_quarante)
    print(data)
    
    donnée_inf_zero = moyenne(inf_zero)
    donnée_zero_dix = moyenne(zero_dix)
    donnée_onze_vingt = moyenne(onze_vingt)
    donnée_vingtun_trente = moyenne(vingtun_trente)
    donnée_trente_un_quarante = moyenne(trente_un_quarante)
    donnée_supp_quarante = moyenne(supp_quarante)
  

    
    return donnée_inf_zero[0], donnée_zero_dix[0],donnée_onze_vingt[0],\
           donnée_vingtun_trente[0],\
           donnée_trente_un_quarante[0], donnée_supp_quarante[0],\
           donnée_inf_zero[1], donnée_zero_dix[1],\
           donnée_onze_vingt[1], donnée_vingtun_trente[1],\
           donnée_trente_un_quarante[1], donnée_supp_quarante[1], data








def diagramme_climattt(donnée_inf_zero, donnée_zero_dix,
                      donnée_onze_vingt,
                      donnée_vingtun_trente, donnée_trente_un_quarante,
                      donnée_supp_quarante,
                      er_inf_zero, er_zero_dix, er_onze_vingt,
                      er_vingtun_trente, er_assez_trente_un_quarante,
                      er_supp_quarante, save):


    plt.bar(range(6), [donnée_inf_zero, donnée_zero_dix,
                        donnée_onze_vingt,
                        donnée_vingtun_trente, donnée_trente_un_quarante,
                        donnée_supp_quarante],
                        width = 0.1, color = 'black',
                       yerr = [er_inf_zero, er_zero_dix, er_onze_vingt,
                              er_vingtun_trente, er_assez_trente_un_quarante,
                              er_supp_quarante],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(6), ['> 0', '0 à 10', '11 à 20',
                          '21 à 30', '31 à 40 ', '> 40'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon la température en degrès")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau






          







































