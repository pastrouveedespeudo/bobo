
import os
import cv2
from colour import Color
from PIL import Image, ImageDraw, ImageChops

PATH_DOSSIER = r"C:\Users\jeanbaptiste\bobo\bobo\polution\26 frvrier 2019\apprentissage"




class couleur_ciel:
    
    CIEL = {'bleu':0,
            'gris':0,
            'rouge':0,
            'bleu_pollution':0,
    }


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

        for i in liste_dico:
            liste.append([c for c,v in dico.items() if v==i])
            if i <= 5:
                break

        
        liste_dico = liste_dico[0:50]
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
                #CIEL['bleu'] += 1

            elif i[0] == i[1] == i[2] > 200:
                blanc += 1
            #else
            pass
            #ici faut définir les couleurs

        print(bleu, blanc, bleu_pollution)
        #ici faire le poid
        
class meteo:
    METEO = {'beau_temps':0,
             'nuageux':0,
             'pluie':0,
             }

    
class climat:

    CLIMAT = {'0_10':0,
              '11_20':0,
              '21_30':0,
              '31_40':0,
            }

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

    liste_dossier = os.listdir(PATH_DOSSIER)
    print(liste_dossier)
    
    for i in liste_dossier:
        if i == "pol.py" or i == "essais.py" or i == "ciel.png":
            pass
        else:
            mask = yo.mask(i)
            print(i)
            couleur_du_ciel = yo.ciel_terre(mask)
            yo.analyse_ciel_couleur(couleur_du_ciel)








































    
