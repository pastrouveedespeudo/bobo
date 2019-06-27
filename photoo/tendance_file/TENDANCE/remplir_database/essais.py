import sys
import os
import cv2

from colour import *
import numpy as np
from PIL import Image, ImageDraw, ImageChops
from matplotlib import pyplot as plt
import math

from palettecouleur_coiffure import couleur_cheuvelure
from coul import *
from palettecouleur import DICO_COULEUR

from database import insertion_table
import psycopg2
import shutil


from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE
from config import LISTE2



def pré_visualisation_donnée(table):
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cur = conn.cursor()
    
    cur.execute("""SELECT * from {}""".format(table))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste



def function_traitement():
    """Here we call database
    for see if we have news pictures."""

    os.chdir('/app/static/bobo')
    liste = os.listdir()
    
    element = pré_visualisation_donnée('bobo1')
    element2 = pré_visualisation_donnée('bobo1_coiffure')
    
    for i in element:
        LISTE2.append(i[1])
    for i in element2:
        LISTE2.append(i[1])

    set1 = set(LISTE2)
    set2 = set(liste)

    liste3 = []
    
    for a in set1 :
        if not(a in set2):
            print(a)
     
    for b in set2 :
        if not(b in set1):
            liste3.append(b)
    return liste3


def traitement():
    """Here we insert picture of body and
    haircuts into database with them colors"""
    
    liste3 = function_traitement()

    print(sorted(liste3),'000000000LISTE3')


    for i in sorted(liste3):    
        print(i)

        nom = i[-5:-4]

        if nom == 'a':
            
            mask_bas(i)
            
            resize('traitement_bas1.jpg', 'traitement_bas1.jpg')
            bas = couleur_habit('traitement_bas1.jpg')


            mask_haut(i)
            resize('traitement_haut.jpg', 'traitement_haut.jpg')
            
            haut = couleur_habit('traitement_haut.jpg')
            

            insertion_info(i, 'féminin', haut[1], bas[1],
                           haut[0], bas[0])


        elif nom == 'b':
        
            coiffure = couleur_cheveux(i)
            print(coiffure)
            ccoiffure(i, coiffure)


                                    

