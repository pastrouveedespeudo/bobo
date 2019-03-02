#pour dnas 9 jours jb du futur, yaura un bug, pour paris pour les manif sert toi de marseille en gros essais de faire un int pour 2 chaine
#sinon on isole le chiffre oauis fin tu verra jtm

import os
import cv2
import json
import pyglet
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops

PATH_DOSSIER = r"C:\Users\jeanbaptiste\bobo\bobo\polution\26 frvrier 2019\apprentissage"

    


METEO = {'beau_temps':0,
         'nuageux':0,
         'pluie':0,
}

VENT = {'tres fort':0,
        'fort':0,
        'moyen fort':0,
        'faible':0, 
}

CLIMAT = {'> 0':0,
          '0_10':0,
          '11_20':0,
          '21_30':0,
          '31_40':0,
          '>40':0,
}


        
TRAFIQUE = {'depart_routier':0,
            'heure_pointe':0,
            'non_heure_pointe':0,
            'regulier jour':0,
}

PARTICULE = {'0_20':0,
            '21_40':0,
            '41_60':0,
            '61_80':0,
            '81_100':0,
            '101_120':0,
            '121_140':0,
            '141_160':0,
            '161_180':0,
            '181_200':0,
            '>200':0
}

PRESSION = {'forte':0,
            'faible':0,
            'normale':0,
}

SAISON = {'primtemps':0,
          'été':0,
          'hiver':0,
          'automne':0,
}

BOUCHON = {'non':0,
           'petit':0,
           'moyen':0,
           'grand':0,
           'assez grand':0,
           'tres grand':0,
}

POINTE = {'pointe':0,
}

WEEKEND = {'weekend':0,
}

VILLE_POLLUE2018 = {'VILLE_POLLUE2018':0,
                    'un':0,
                    'deux':0,
                    'trois':0,
                    'quattre':0,
                    'non':0,
}

POPULATION_ACTIVE_HABITANT = {'sup1M':0,
                              'sup500K':0,
                              'supp300K':0,
}



ACTIVITE_EXEPTIONNELLE = {'aggissement':0,
                          'manifestation':0,
                          'circulation dense':0,
                          'condition a polution':0,



}

REGION_INDUSTRIEL_POLLUEE = {'oui':0,
                             'non':0,
}


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
        #print(data)

        méteo = data['weather'][0]['main']

        if méteo == "Rain":
            METEO['pluie'] +=1
        elif méteo == "Clouds":
            METEO['nuageux'] +=1
        elif méteo == "Clear":
            METEO['beau_temps'] +=1

        #print(data)
        try:
            vent_degres = data['wind']['deg']
        except:
            pass

        
        vent = data['wind']['speed']
        #print(vent)
        #0 90 180 270 300def vent m/s

        if vent <= 3 :
            VENT['faible'] += 1
            
        elif vent <= 6 and vent > 3:
            VENT['moyen fort'] += 1

        elif vent <= 8 and vent > 6:
            VENT['fort'] += 1

        elif vent <= 12 and vent > 8:
            VENT['tres fort'] += 1


        date = datetime.datetime.now()
        mois = date.month

        pression = data['main']['pressure']



        if pression >= 1030:#anti
            PRESSION['forte'] += 1

        elif pression <= 1013:
            PRESSION['faible'] += 1#depression

        else:
            PRESSION['normale'] += 1

        #forte pression == antycyclone= bo temps mais en hyver == tres froid
        #plus un rond est petit plus y'a de vent
        #dépression == pluie


 



class climat:


    def recuperation_donnée(self, lieu):
        self.lieu = lieu
        
        clé = '5a72ceae1feda40543d5844b2e04a205'
        
        localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(self.lieu,clé)

        r = requests.get(localisation)

        data=r.json()

        température = data['main']['temp']
        température = température - 273.15
        
        #print(str(round(température)) + ' Celsius')

        if température < 0:
            CLIMAT['> 0']+=1
        elif température >= 0 and température <= 10:
            CLIMAT['0_10']+=1
        elif température >= 11 and température <= 20:
            CLIMAT['11_20']+=1
        elif température >= 21 and température <= 30:
            CLIMAT['21_30']+=1
        elif température >= 31 and température <= 40:
            CLIMAT['31_40']+=1
        elif température >= 41:
            CLIMAT['41>']+=1

    
 
    def saison(self):
        
        date = datetime.datetime.now()
        mois = date.month
        jour = date.day

       
        
        if mois == 12 or mois == 1\
           or mois == 2:
            SAISON['hiver'] += 1 #pollution au bois

        elif mois == 3 or mois == 4\
             or mois == 5:
            SAISON['primtemps'] += 1

        elif mois == 6 or mois == 7\
             or mois == 8\
             or mois == 9:
            SAISON['été'] += 1 

        elif mois == 10 or mois == 11\
             or mois == 12:
            SAISON['automne'] += 1




class trafique:
    
    def trafique_circulation(self):

        date = datetime.datetime.now()
        
        jour = date.day
        mois = date.month
        année = date.year

        heure = date.hour
        minute = date.minute



        heure_pointe_semaine = [12, 18,19]

        départ_routier = [(2,1), (5,1), (9,2), (16,2), (22,2),(23,2),
                          (1,3),(2,3),(8,3),(9,3),
                          (19,4),(22,4),(26,4),(27,4),(28,4),
                          (4,5),(5,5),(29,5),(30,5),
                          (5,6),(6,6),(7,6),(10,6),(28,6),
                          (5,7),(6,7),(7,7),(12,7),(13,7),(14,7),(19,7),(20,7),(21,7),(26,7),(27,7),(28,7),
                          (2,8),(3,8),(4,8),(9,8),(10,8),(11,8),(16,8),(17,8),(18,8),(19,8),(23,8),(24,8),(25,8),(30,8),(31,8),
                          (1,9),
                          (18,10),(25,10),(26,10),(31,10),
                          (3,11),(8,11),(11,11),
                          (20,12),(21,12),(22,12),(24,12),(27,12),(28,12)
            ]



        
        #print(jour, mois, année)
        #print(str(heure) + ":" + str(minute))



        dep = ""
        pointe = ""
        normale = ""
        non_pointe = ""

        
        for i in départ_routier:
            if (jour, mois) == i :
                dep = True

            elif (jour, mois) != i :
                normale = True

        for i in heure_pointe_semaine:
            if i == heure:
                pointe = True
            else:
                non_pointe == True
            

        if dep == True:
            TRAFIQUE['depart_routier'] += 1

        elif normale == True:
            TRAFIQUE['regulier jour'] += 1

        if pointe == True:
            TRAFIQUE['heure_pointe'] += 1
            
        elif non_pointe == True:
            TRAFIQUE['non_heure_pointe jour'] += 1

            
        #print("jour de départ :",dep)
        #print("normal jour: ",normale)

            

    def habitude(self):

        pointe = [8,9,16,17,18,19]#reverifie les pointes
        jour = ['samedi', 'dimanche']

        
        date = datetime.datetime.now()

        heure = date.hour
        jour = date.weekday()
        
        #print(heure, jour)

        for i in pointe:
            if heure == i:
                POINTE['pointe'] += 1


        if jour == 5 or jour == 6:
            WEEKEND['weekend'] += 1

    


    def bouchons(self, lieu):
        self.lieu = lieu

      
        if self.lieu == "lyon":
            path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(self.lieu)
          
            r = requests.get(path)

            liste = []

            page = r.content
            soup = BeautifulSoup(page, "html.parser")
        
            liste.append(str(soup))
            bouchon = liste[0][28678:28685]
            

            liste_bouchon = []
            for i in bouchon:
                try:
                    if i == ",":
                        liste_bouchon.append(".")
                    i = int(i)
                    liste_bouchon.append(str(i))
                except:
                    pass

            liste2 = []
            a = ','.join(liste_bouchon)
            for i in a:
                #print(i)
                if i == ",":
                    pass
                else:
                    liste2.append(i)
         
            b = "".join(liste2)
            try:
                b = float(b)
            except:
                pass
            try:
                b = int(b)
            except:
                pass

           
            if b == 0 or b == 0.0:
                BOUCHON['non'] += 1 

        
            elif b > 0  and b <= 5:
                BOUCHON['petit'] += 1 


            elif b > 5 and b <= 9:
                BOUCHON['moyen'] += 1 

            elif b > 9 and b <= 15:
                BOUCHON['grand'] += 1 

            elif b > 15 and b <= 20:
                BOUCHON['assez grand'] += 1 

            elif b > 20:
                BOUCHON['tres grand'] += 1

        elif self.lieu == "marseille":
            pass


        elif self.lieu == "paris":
        
            path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

            r = requests.get(path)

            liste = []

            page = r.content
            soup = BeautifulSoup(page, "html.parser")

            liste.append(str(soup))
            bouchon = liste[0][1874:1877]
            bouchon = str(bouchon)

            kmbouchon = []
            liste = []
            for i in bouchon:
                try:
                    i = int(i)
                    kmbouchon.append(str(i))
                except:
                    pass

            kmbouchon = "".join(kmbouchon)
            kmbouchon = int(kmbouchon)

            b = kmbouchon

            if b == 0 or b == 0.0:
                BOUCHON['non'] += 1 

            elif b > 0  and b <= 5:
                BOUCHON['petit'] += 1 

            elif b > 5 and b <= 9:
                BOUCHON['moyen'] += 1 

            elif b > 9 and b <= 15:
                BOUCHON['grand'] += 1 

            elif b > 15 and b <= 20:
                BOUCHON['assez grand'] += 1 

            elif b > 20:
                BOUCHON['tres grand'] += 1
                       


    
    def autoroute_proximité(self):
        pass


    def requete_lyon_traffique(self, path):
        self.path = path

        liste = []
        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        propriete = soup.find('div',attrs={"class":u"news"})
        
        
        agissement = str(propriete).find(str("pollution"))
        agissement2 = str(propriete).find(str("circulation différenciée"))

        if agissement >= 0 and agissement2 >= 0:
            ACTIVITE_EXEPTIONNELLE['aggissement'] += 1



        trafic = str(propriete).find(str("circulation"))
        trafic1 = str(propriete).find(str("dense"))
        trafic2 = str(propriete).find(str("très dense"))

        if trafic >= 0 and trafic1 >= 0 or trafic2 >= 0:
            ACTIVITE_EXEPTIONNELLE['circulation dense'] += 1

        manif = str(propriete).find(str("Manifestation"))
        manif1 = str(propriete).find(str("manifestation"))
  

        if manif >= 0 or manif1 >=0 :
            ACTIVITE_EXEPTIONNELLE['manifestation'] += 1

        news = [str(propriete)]
        nombre = news[0][160:165]
        nombre2 = []
        for i in nombre:
            
            try:
                i = int(i)
                nombre2.append(i)

            except:
                pass

        
        if nombre2[0] > 0:
            ACTIVITE_EXEPTIONNELLE['condition a polution'] += 1




        
    def requete_paris_traffique(self, path):
        self.path = path

        semaine = {'lundi':0, 'mardi':1, 'mercredi':2, 'jeudi':3, 'vendredi':4, 'samedi':5,
                   'dimanche':6}

        liste = [[],[]]
        
        date = datetime.datetime.now()
        jour = date.day
        jour_semaine = date.weekday()


        liste = []
        r = requests.get(path)
        

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        propriete = soup.find_all("table")
       

        for i in propriete:
            date = soup.find('span',attrs={"class":u"wday"})
        


        date = str(date)
    

        lundi = str(date).find("lundi")
        mardi = str(date).find("mardi")
        mercredi = str(date).find("mercredi")
        jeudi = str(date).find("jeudi")
        vendredi = str(date).find("vendredi")
        samedi = str(date).find("samedi")
        dimanche = str(date).find("dimanche")
        
        if lundi > 0 :
            a = 0
        if mardi > 0 :
            a = 1
        if mercredi > 0 :
            a = 2
        if jeudi > 0 :
            a = 3
        if vendredi > 0 :
            a = 4
        if samedi > 0 :
            a = 5
        if dimanche > 0 :
            a = 6

        numero_mois = [date]
        
        numero_mois = numero_mois[0][23:42]
  

        num = []
       
        for i in numero_mois:
            try:
                i = int(i)
                num.append(i)
                
            except:
                pass

        #print(type(num[0]))
        #print(num)
        #print(a)
  

        if a == jour_semaine and num[0] == jour:
            ACTIVITE_EXEPTIONNELLE['manifestation'] += 1
           
        #a dans 9 jours hihi faut faire pour le 10 par ex


    def requete_marseille_traffique(self, path):
        r = requests.get(path)

        date = datetime.datetime.now()
        jour = date.day
        jour_semaine = date.weekday()
        
        
        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        date = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
       
        date = str(date)
        
        a = 0
        lundi = str(date).find("lundi")
        mardi = str(date).find("mardi")
        mercredi = str(date).find("mercredi")
        jeudi = str(date).find("jeudi")
        vendredi = str(date).find("vendredi")
        samedi = str(date).find("samedi")
        dimanche = str(date).find("dimanche")
        
        if lundi > 0 :
            a = 0
        if mardi > 0 :
            a = 1
        if mercredi > 0 :
            a = 2
        if jeudi > 0 :
            a = 3
        if vendredi > 0 :
            a = 4
        if samedi > 0 :
            a = 5
        if dimanche > 0 :
            a = 6


        numero = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
        #print(numero)
        numero = str(numero)
        numero = numero[20:]
        
        try:
            numero = int(numero)
        except:
            liste = []
            numero = str(numero)

            for i in numero:
                try:
                    i = int(i)
                    liste.append(i)
                except:
                    pass
        #print(a)
        if a == jour_semaine and liste[0] == jour:
            ACTIVITE_EXEPTIONNELLE['manifestation'] += 1

    def activité_execptionnelle(self, lieu):
        self.lieu = lieu

        
        if self.lieu == "lyon":
            path = "https://www.onlymoov.com/trafic/"
            trafique.requete_lyon_traffique(path)

            

        elif self.lieu == "paris":
            path = "https://paris.demosphere.net/manifestations-paris"
            trafique.requete_paris_traffique(path)

        elif self.lieu == "marseille":
            path = "https://mars-infos.org/spip.php?page=agenda"
            trafique.requete_marseille_traffique(path)






class particule:

    def particule(self, lieu):
        self.lieu = lieu

        liste = []

        path = "https://air.plumelabs.com/fr/live/{}".format(self.lieu)

        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        propriete = soup.find_all("div")
        for i in propriete:
            liste.append(i.get_text())

        phrase_clé = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"
        
        recherche_taux = str(liste).find(str(phrase_clé))
        liste_epluché = liste[20:21]
        polution = liste_epluché[0][31:33]
        polution = int(polution)

        if polution <= 20:
            PARTICULE['0_20'] += 1

        elif polution >=21 and polution <= 40:
            PARTICULE['21_40'] += 1
            
        elif polution >=41 and polution <= 60:
            PARTICULE['41_60'] += 1
            
        elif polution >=61 and polution <= 80:
            PARTICULE['61_80'] += 1
            
        elif polution >=81 and polution <= 100:
            PARTICULE['81_100'] += 1
            
        elif polution >=101 and polution <= 120:
            PARTICULE['101_120'] += 1
            
        elif polution >=121 and polution <= 140:
            PARTICULE['121_140'] += 1
            
        elif polution >=141 and polution <= 160:
            PARTICULE['141_160'] += 1
            
        elif polution >=161 and polution <= 180:
            PARTICULE['161_180'] += 1
            
        elif polution >=181 and polution <= 200:
            PARTICULE['181_200'] += 1
            
        elif polution >200:
            PARTICULE['>200'] += 1


    def france(self, lieu):
        self.lieu = lieu

        liste = ["lyon", "marseille","paris","roubaix"]


        c = 0
        for i in liste:

            if i == liste[0]:
                VILLE_POLLUE2018['un'] += 1

            elif c == liste[1]:
                VILLE_POLLUE2018['deux'] += 1

            elif c == liste[2]:
                VILLE_POLLUE2018['trois'] += 1

            elif c == liste[3]:
                VILLE_POLLUE2018['quattre'] += 1
            else:
                VILLE_POLLUE2018['non'] += 1
                

                
            c+=1
        


    def industrie(self, lieu):
        self.lieu = lieu


        path = "https://fr.wikipedia.org/wiki/{}".format(self.lieu) 

        r = requests.get(path)

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find('table',attrs={"class":u"infobox_v2"})
        propriete = str(propriete)

        try:
            code_postal = propriete[5649:5654]
            code_postal = int(code_postal)
            
        except:
            pass

        liste = []

        path = "http://www.cartesfrance.fr/recherche/?q={}".format(code_postal)

        r = requests.get(path)

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        
        propriete = soup.find_all('Département')




        pole_poluant = {'1':'Nord',
                        '2':'Bouches-du-Rhône',
                        '3':'Moselle',
                        '4':'Seine-Maritime',
                        '5':'Loire-Atlantique',
                        '6':'Haute-Normandie',
                        '7':'Meurthe-et-Moselle',
                        '8':'Seine-Maritime',
                        '9':'Rhône'

                        }


        for i in pole_poluant.keys():
            a = str(soup).find(str(pole_poluant[i]))
        #    print(a,pole_poluant[i])

        if a > 0:
            REGION_INDUSTRIEL_POLLUEE['oui'] += 1

        else:
            REGION_INDUSTRIEL_POLLUEE['non'] += 1
            




    
class geographie:

    def situation(self):
        pass
    #dans un trou entre des montagnes? pres de la mer ect
    





    
class socio:

    def habitant(self, lieu):
        self.lieu = lieu

        lyon = 328469
        paris = 1350800 
        marseille = 762480 

        if self.lieu == 'lyon':
            POPULATION_ACTIVE_HABITANT['supp300K'] += 1

        if self.lieu == 'paris':
            POPULATION_ACTIVE_HABITANT['sup1M'] += 1

        if self.lieu == 'marseille':
            POPULATION_ACTIVE_HABITANT['sup500K'] += 1
        #population active de 15 a 59 ans






class analyse:

    def analyse(self, dico):
        self.dico = dico

        for cle, valeur in self.dico.items():
            if valeur == 1:
                print(cle)

        return cle
     





    def score(self):
        trafic_chemin = {'départ':2,
                         'heure':1,
                         'non heure':-1,
                         'régulier':-2,
            }


        bouchon_chemin = {'non':0,
                   'petit':0.5,
                   'moyen':0.75,
                   'grand':1,
                   'assez grand':1.5,
                   'tres grand':2,
        }
        


        pointe_chemin = {'pointe':2,
        }

        weekend_chemin = {'weekend':-2,
        }
        #---


        METEO = {'beau_temps':1,
                 'nuageux':0,
                 'pluie':-2,
        }
        
        SAISON = {'primtemps':1,
                  'été':2,
                  'hiver':2,
                  'automne':-1,
        }
        CLIMAT = {'> 0':1,
                  '0_10':-1,
                  '11_20':-1,
                  '21_30':2,
                  '31_40':2,
                  '>40':2,
        }

        PRESSION = {'forte':2,
                    'faible':-2,
                    'normale':0,
        }

        #---

        VILLE_POLLUE2018 = {'non':-1,
                            'un':2,
                            'deux':2,
                            'trois':2,
                            'quattre':2,
        }


        POPULATION_ACTIVE_HABITANT = {'sup1M':2,
                                      'sup500K':1,
                                      'supp300K':1,
        }


        ACTIVITE_EXEPTIONNELLE = {'aggisement':-2,
                                  'manifestation':1,
                                  'circulation dense':2,
                                  'condition a polution':2,



        }


        REGION_INDUSTRIEL_POLLUEE = {'oui':2,
                                     'non':-1,
        }


        
    def print(self):

        
        print(METEO)
        print("\n")
        print(VILLE_POLLUE2018)
        print("\n")
        print(TRAFIQUE)
        print("\n")
        
        print(CLIMAT)
        print("\n")

        print(VENT)
        print("\n")
        print(PRESSION)
        print("\n")
        print(SAISON)
        print("\n")
        print(BOUCHON)
        print("\n")
        print(POINTE)
        print("\n")
        print(WEEKEND)
        print("\n")

        print(POPULATION_ACTIVE_HABITANT)
        print("\n")
        print(REGION_INDUSTRIEL_POLLUEE)
        print("\n")
        print(ACTIVITE_EXEPTIONNELLE)
        print("\n")







if __name__ == "__main__":


    meteo = météo()
    
    climat = climat()

    trafique = trafique()

    particule = particule()

    socio = socio()

    analyse = analyse()
    
    liste_dossier = ["marseille","paris","lyon"]

    
    
    for i in liste_dossier:
        
        print(i)
        
        position = meteo.recuperation_lieu(i)


        
        meteo.recuperation_donnée(position)

        trafique.bouchons(i)
        trafique.habitude()
        trafique.trafique_circulation()
        trafique.activité_execptionnelle(position)
        
        climat.saison()
        climat.recuperation_donnée(position)

        particule.particule(position)
        particule.france(i)
        particule.industrie(i)
        
        socio.habitant(i)
        


        analyse.analyse(TRAFIQUE)
        analyse.analyse(WEEKEND)
        analyse.analyse(POINTE)
        analyse.analyse(BOUCHON)
    


        analyse.analyse(METEO)
        analyse.analyse(VENT)
        analyse.analyse(SAISON)
        analyse.analyse(CLIMAT)
        analyse.analyse(PRESSION)


        analyse.analyse(VILLE_POLLUE2018)
        analyse.analyse(ACTIVITE_EXEPTIONNELLE)
        analyse.analyse(POPULATION_ACTIVE_HABITANT)
        analyse.analyse(REGION_INDUSTRIEL_POLLUEE)
  




        #a comparer avec
        #print(PARTICULE)
     
    
        

        TRAFIQUE = {'depart_routier':0,
            'heure_pointe':0,
            'non_heure_pointe':0,
            'regulier jour':0,
        }



        VENT = {'tres fort':0,
        'fort':0,
        'moyen fort':0,
        'faible':0, 
        }



        METEO = {'beau_temps':0,
                 'nuageux':0,
                 'pluie':0,
        }
        
        SAISON = {'primtemps':0,
                  'été':0,
                  'hiver':0,
                  'automne':0,
        }
        CLIMAT = {'> 0':0,
                  '0_10':0,
                  '11_20':0,
                  '21_30':0,
                  '31_40':0,
                  '>40':0,
        }

        PRESSION = {'forte':0,
                    'faible':0,
                    'normale':0,
        } 

        PARTICULE = {'0_20':0,
                    '21_40':0,
                    '41_60':0,
                    '61_80':0,
                    '81_100':0,
                    '101_120':0,
                    '121_140':0,
                    '141_160':0,
                    '161_180':0,
                    '181_200':0,
                    '>200':0
        }











        BOUCHON = {'non':0,
                   'petit':0,
                   'moyen':0,
                   'grand':0,
                   'assez grand':0,
                   'tres grand':0,
        }
        


        POINTE = {'pointe':0,
        }

        WEEKEND = {'weekend':0,
        }


        VILLE_POLLUE2018 = {'non':0,
                            'un':0,
                            'deux':0,
                            'trois':0,
                            'quattre':0,
        }


        POPULATION_ACTIVE_HABITANT = {'sup1M':0,
                                      'sup500K':0,
                                      'supp300K':0,
        }


        ACTIVITE_EXEPTIONNELLE = {'aggisement':0,
                                  'manifestation':0,
                                  'circulation dense':0,
                                  'condition a polution':0,



        }


        REGION_INDUSTRIEL_POLLUEE = {'oui':0,
                                     'non':0,
        }




















        
