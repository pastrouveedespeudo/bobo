
import os
import cv2
from PIL import Image, ImageDraw, ImageChops

PATH_DOSSIER = r"C:\Users\jeanbaptiste\bobo\bobo\polution\26 frvrier 2019\apprentissage"




class couleur_ciel:
    
    CIEL = {'bleu':0,
            'gris':0,
            'rouge':0,   
    }




    def ciel_terre(self, image):
        self.image = image

        valeur_mask = []

        img = cv2.imread(self.image)
        imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgrey, 127, 255, cv2.THRESH_BINARY_INV)
        
        for x in range(thresh.shape[0]):
            for y in range(thresh.shape[1]):
                if thresh[x,y] == 255:
                    valeur_mask.append(x,y)
                    x = 0
                    y += 1
                    
        #le but prendre une autre image soit la grise soit la couleur y appliquer
                    #un contour bleu
                    #faire le mask
                    #prendre la couleur
        cv2.imshow("image", img)

    
    #analyse couleur
    #dire pourquoi cette couleur


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


        def mask(self, image):
        self.image = image
        
        img = Image.open(self.image)

        
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[0] 
        b = img.size[1] / 100 * 70

        c = 0
        d = 0

        coords = (a,b, c,d)
   
        
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        diff.save("ciel.jpg")
        return "ciel.jpg"



if __name__ == "__main__":

    yo = couleur_ciel()

    liste_dossier = os.listdir(PATH_DOSSIER)
    print(liste_dossier)
    
    for i in liste_dossier:
        if i == "pol.py" or i == "essais.py":
            pass
        else:
            mask = yo.mask(i)
            yo.ciel_terre(i)
            








































    
