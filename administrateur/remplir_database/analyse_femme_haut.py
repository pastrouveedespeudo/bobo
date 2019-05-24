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



def resize(img, save):

   image = Image.open(img)

   image = image.resize((100,100))
                        
   image.save(save)

   
def mask_bas(i):

    print('mask bas de :', i)

    img = Image.open(i)

    masque = Image.new('RGB', img.size, color=(255,255,255))

    a = img.size[0] / 100 *30
    b = img.size[1] / 100* 70
    c = 0
    d = img.size[1]

    coords = (a,b, c,d)

    masque_draw = ImageDraw.Draw(masque)
    masque_draw.rectangle(coords, fill=(0,0,0))
    diff = ImageChops.lighter(img, masque)

    img = img.rotate(180)
    img.crop((0, 0, b/2, a)).save('traitement_bas1.jpg')

    print('fin')

def mask_haut(i):

    img = Image.open(i)

    print('mask haut de :', i)

    masque = Image.new('RGB', img.size, color=(255,255,255))

    a = img.size[1]
    b = img.size[0] / 100 * 100
   
    c = 0
    d = 0

    coords = (a,b, c,d)

    
    masque_draw = ImageDraw.Draw(masque)
    masque_draw.rectangle(coords, fill=(0,0,0))
    diff = ImageChops.lighter(img, masque)


    img.crop((0, 0, b, a/2)).save('traitement_haut.jpg')
    


def couleur_habit(im):


    print(im, ' : en cours')

    image = cv2.imread(im)
    print('ok')
    largeur = image.shape[1]
    hauteur = image.shape[0]

    taille = largeur * hauteur
    print('ok1')
    couleur_liste = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            
            colordb = get_colordb('bobo.txt')
            if not colordb:
                print('No parseable color database found')
                sys.exit(1)
            nearest = colordb.nearest(image[x,y][2],
                                      image[x,y][1],
                                      image[x,y][0])

            couleur_liste.append(nearest)
            

    print('ok2')
    return taille, couleur_liste



def couleur_cheveux(image):

    dico = {}
    dico_couleur = {'marron':0,
                    'noir':0,
                    'blond':0}

    im = Image.open(image)
    for value in im.getdata(): 
         if value in dico.keys():
             dico[value] += 1
         else:
             dico[value] = 1


    liste = []
    
    for cle, valeur in dico.items():
        liste.append((cle, valeur))
            
    liste2 = []
    for i in liste:
        if i[0][0] >= 240 and\
           i[0][1] >= 240 and\
           i[0][2] >= 240:
            pass
        else:
            liste2.append(i)

    for i in liste2:
        coul = couleur_cheuvelure(i[0][0], i[0][1], i[0][2])
        if coul == None:
            pass
        else:

            if coul == 'blond':
                dico_couleur['blond'] += 1
                
            elif coul == 'marron':
                dico_couleur['marron'] += 1

            elif coul == 'noir':
                dico_couleur['noir'] += 1

                

 
    if dico_couleur['blond'] > dico_couleur['marron'] + 1000 and\
       dico_couleur['blond'] > dico_couleur['noir']:
        print('couleur de cheveux blond')
        return 'blond'
        
        
    elif dico_couleur['marron'] > dico_couleur['blond'] + 1000 and\
       dico_couleur['marron'] > dico_couleur['noir']:
        print('couleur de cheveux marron')
        return 'marron'
    
    elif dico_couleur['noir'] > dico_couleur['blond'] and\
       dico_couleur['noir'] > dico_couleur['noir']:
        print('couleur de cheveux noir')
        return 'noir'
    
    elif dico_couleur['marron'] >= dico_couleur['blond'] + 400 and\
       dico_couleur['marron'] > dico_couleur['noir']:
        print('couleur de cheveux chatin')
        return 'chatin'
        
    elif dico_couleur['blond'] >= dico_couleur['marron'] + 400 and\
       dico_couleur['blond'] > dico_couleur['noir']:
        print('couleur de cheveux chatin')
        return 'chatin'



def insertion_info(nom, sexe, haut, bas, taille_haut, taille_bas):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    cur = conn.cursor()

    
    
    cur.execute("""insert into bobo1
             (image, sexe, haut, bas, taille_haut, taille_bas)
             values(%s, %s, %s, %s, %s, %s);""",
             (nom, sexe, haut, bas, taille_haut,
             taille_bas))

    
    
    conn.commit()


def ccoiffure(image, coiffure):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cur = conn.cursor()
    

    cur.execute("""insert into bobo1_coiffure
                (image, coiffure)
                values(%s, %s);""", (image, coiffure))


    conn.commit()


def pré_visualisation_donnée(table):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cur = conn.cursor()
    
    cur.execute("""SELECT * from {}""".format(table))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste


    
def traitement():
    

    try:
        os.chdir('/app/static/bobo')
    except:
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        
    liste = os.listdir()
    print(liste)
    liste2 = ['analysa.py', 'analyse_femme_haut.py', 'bobo.txt',
              'config.py', 'constante.py', 'conteneur.py', 'coul.py',
              'coupe_analysis.py', 'database.py', 'ess.py', 'mode_analyse.py',
              'mode_w_data.py', 'palettecouleur.py', 'palettecouleur_coiffure.py',
              'traitement_bas1.jpg', 'traitement_haut.jpg', '__pycache__', 'tendance.py']

    element = pré_visualisation_donnée('bobo1')
    element2 = pré_visualisation_donnée('bobo1_coiffure')
    
    for i in element:
        liste2.append(i[1])
    for i in element2:
        liste2.append(i[1])

    set1 = set(liste2)
    set2 = set(liste)

    liste3 = []
    
    for a in set1 :
        if not(a in set2):
            print(a)
     
    for b in set2 :
        if not(b in set1):
            liste3.append(b)

    
    print(sorted(liste3),'000000000LISTE3')


    for i in sorted(liste3):    
        print(i)
        if i == '__pycache__' or i == 'analyse_femme_haut.py' or\
           i == 'constante.py' or i == 'coul.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i=='bobo.txt' or i== 'traitement_haut.jpg' or i == "traitement_bas1.jpg" or\
           i == 'config.py' or i == 'constante.py' or i =='coul.py' or i == 'database.py' or\
           i == 'palettecouleur.py' or i =='palettecouleur_coiffure.py' or i=='tendance.py':
            pass
        
        else:

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


                                         




        



traitement()












































