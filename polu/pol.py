
import os
import cv2
import json
import requests
from colour import Color
from PIL import Image, ImageDraw, ImageChops

PATH_DOSSIER = r"C:\Users\jeanbaptiste\bobo\bobo\polution\26 frvrier 2019\apprentissage"

    
CIEL = {'bleu':0,
        'gris':0,
        'blanc':0,
        'bleu_pollution':0,
}

METEO = {'beau_temps':0,
         'nuageux':0,
         'pluie':0,
}


class couleur_ciel:



    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb
    

        
    def mask(self, image):
        self.image = image
        
        img = Image.open(self.image)

        
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[0] 
        b = img.size[1] / 100 * 50

        c = 0
        d = 0

        coords = (a,b, c,d)

        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        diff.save("ciel.jpg")
        return "ciel.jpg"



    def ciel_terre(self, image):
        self.image = image

        liste = []
        valeur_mask = []

        self.im = Image.open(self.image)
                      
        dico = {}
        for value in self.im.getdata():
            if value in dico.keys():
                 dico[value] += 1
            else:
                 dico[value] = 1
    

        liste_dico = []
        for i in dico.values():
            liste_dico.append(i)
            
        liste_dico= sorted(liste_dico, reverse = True)



    
        liste_couleur = []
        
        for i in liste_dico:
          
            couleur = [c for c,v in dico.items() if v==i]
            liste_couleur.append(couleur[0])

        return liste_couleur



    def analyse_ciel_couleur(self, liste):
        self.liste = liste
        
        bleu = 0
        blanc = 0
        bleu_pollution = 0

        for i in self.liste:

            if  i[0] <= i[1] < i[2] and\
                 i[1]>= i[2] - 30:
                 bleu_pollution += 1
                
            elif i[0] <= i[1] < i[2]:
                bleu += 1
                

            elif i[0] == i[1] == i[2] > 200:
                blanc += 1
            #else
            pass
            #ici faut définir les couleurs

        #print(bleu, blanc, bleu_pollution)
        total = len(liste)
    
    
        if bleu * 100 / total > 2:#faut voir ici 
            CIEL['bleu'] += 1
        if  bleu_pollution * 100 / total > 2:
            CIEL['bleu_pollution'] += 1
        if blanc * 100 / total > 2:
            CIEL['blanc'] += 1

        #gris
            
        print(CIEL)



        
class météo:


    def recuperation_lieu(self, image):
        self.image = image

        liste_lieu = []

        lieu = str(image)
        for i in lieu:
            if i == " ":
                break
            else:
                liste_lieu.append(i)
                
        liste_lieu = "".join(liste_lieu)
        return liste_lieu
    

    def recuperation_donnée(self, lieu):
        self.lieu = lieu
        clé = '5a72ceae1feda40543d5844b2e04a205'
        
        localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(self.lieu,clé)

        r = requests.get(localisation)

        data=r.json()
        print(data)

        méteo = data['weather'][0]['main']

        if méteo == "Rain":
            METEO['pluie'] +=1
        elif méteo == "Clouds":
            METEO['nuageux'] +=1
        elif méteo == "Clear":
            METEO['beau_temps'] +=1

    

class climat:

    CLIMAT = {'> 0':0,
              '0_10':0,
              '11_20':0,
              '21_30':0,
              '31_40':0,
            }

    def recuperation_donnée(self, lieu):
        self.lieu = lieu
        
        clé = '5a72ceae1feda40543d5844b2e04a205'
        
        localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(self.lieu,clé)

        r = requests.get(localisation)

        data=r.json()

        température = data['main']['temp']
        température = température - 273.15
        
        print(str(round(température)) + ' Celsius')

        if température < 0:
            CLIMAT['> 0']+=1
        elif température >= 0 and <= 10:
            CLIMAT['0_10']+=1
        elif température >= 11 and <= 20:
            CLIMAT['11_20']+=1
        elif température >= 21 and <= 30:
            CLIMAT['21_30']+=1
        elif température >= 31 and <= 40:
            CLIMAT['31_40']+=1




class trafique:
    
    TRAFIQUE = {'vacance_scolaire':0,
                'non_vacance':0,
                'heure_pointe':0,
                'non_heure_pointe':0,
                }

class concentration_industrielle:

    CONCENTRATRION = {'forte':0,
                      'moyenne':0,
                      'faible':0,
                    }


class analyse:

    def analyse(self):
        pass


class fourtout:
    
    pm = {'inf50':0,
          'inf90':0,
          'inf110':0,
          'inf130':0,
        }






if __name__ == "__main__":

    yo = couleur_ciel()

    meteo = météo()

    température = climat()

    liste_dossier = os.listdir(PATH_DOSSIER)

    for i in liste_dossier:
        if i == "pol.py" or i == "essais.py" or i == "ciel.png"\
           or i == "ciel.jpg":
            pass
        else:
            #mask = yo.mask(i)
            #print(i)
            #couleur_du_ciel = yo.ciel_terre(mask)
            #yo.analyse_ciel_couleur(couleur_du_ciel)

            position = meteo.recuperation_lieu(i)
            #meteo.recuperation_donnée(position)

            température.recuperation_donnée(position)

            #print(CIEL)
            #print(METEO)
    
            
        CIEL = {'bleu':0,
                'gris':0,
                'blanc':0,
                'bleu_pollution':0,
        }


        METEO = {'beau_temps':0,
         'nuageux':0,
         'pluie':0,
        }



































    
