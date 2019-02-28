
class couleur_ciel:

    def recherche_image_paris(self, path):

        self.path = path
        liste = []

        
        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        propriete = soup.find_all("script")
        for i in propriete:
            liste.append(i.get_text())
        return liste




    def lieu(self, lieu):
        self.lieu = lieu

    
        if self.lieu == "Paris" or self.lieu == "paris":
            
            path = "https://www.viewsurf.com/univers/ville/vue/16924-france-ile-de-france-paris-la-defense"
            couleur_ciel.recherche_image_paris(self, path)
            image = couleur_ciel.recherche_image_paris(self, path)
            image = image[11][628:702]
            urllib.request.urlretrieve(image, "paris3.jpg")

            return "paris.jpg"

        elif self.lieu == "Marseille" or self.lieu == "marseille":
            path = "http://films.viewsurf.com/marseille06/12/10/media_1551374405.jpg"
            urllib.request.urlretrieve(str(path), "marseille.png")

            return "marseille.png"

        elif self.lieu == "Lyon" or self.lieu == "lyon":
            
            path = "https://fr.webcams.travel/webcam/1511302382-lyon-radisson-blu"
            urllib.request.urlretrieve(str(path), "lyon3.png")

            return "lyon.png"



        elif self.lieu == "Pekin" or self.lieu == "pekin":
            pass



            
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
        
        self.bleu = 0
        blanc = 0
        self.bleu_pollution = 0

        for i in self.liste:

            if  i[0] <= i[1] < i[2] and\
                 i[1]>= i[2] - 30:
                 self.bleu_pollution += 1
                
            elif i[0] <= i[1] < i[2]:
                self.bleu += 1
                

            elif i[0] == i[1] == i[2] > 200:
                blanc += 1
            

        #print(bleu, blanc, bleu_pollution)
        total = len(liste)
    
    
        if self.bleu * 100 / total > 2:
            CIEL['bleu'] += 1
        if  self.bleu_pollution * 100 / total > 2:
            CIEL['bleu_pollution'] += 1
        if blanc * 100 / total > 2:
            CIEL['blanc'] += 1

      
            
        def bleu_ou_bleu_pollution(self):
            
            if self.bleu > self.bleu_pollution:
                CIEL_bleu_ou_bleu_polu['bleu'] += 1
            else:
                CIEL_bleu_ou_bleu_polu['bleu_polu'] += 1
                


        def teinte_gris(self, liste):
            self.liste = liste

            if i[0] == i[1] == i[2]\
               and i[0] == 69:
                TEINTE_GRIS['lvl 6'] += 1
                
            if i[0] == i[1] == i[2]\
               and i[0] >= 70 and i[0] <= 91:
                TEINTE_GRIS['lvl 5'] += 1
                
            if i[0] == i[1] == i[2]\
               and i[0] >= 92 and i[0] <= 120:
                TEINTE_GRIS['lvl 4'] += 1

            if i[0] == i[1] == i[2]\
               and i[0] >= 121 and i[0] <= 145:
                TEINTE_GRIS['lvl 3'] += 1
                
            if i[0] == i[1] == i[2]\
               and i[0] >= 146 and i[0] <= 182:
                TEINTE_GRIS['lvl 2'] += 1

            if i[0] == i[1] == i[2]\
               and i[0] >= 183 and i[0] <= 205:
                TEINTE_GRIS['lvl 3'] += 1





    
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


        vent_degres = data['wind']['deg']
        vent = data['wind']['speed']
        print(vent)
        #0 90 180 270 300def vent m/s

        if vent <= 3 :
            VENT['faible'] += 1
            
        elif vent <= 6 and vent > 3:
            VENT['moyen fort'] += 1

        elif vent <= 8 and vent > 6:
            VENT['fort'] += 1

        elif vent <= 12 and venet > 8:
            VENT['tres fort'] += 1




    def phénomene(self):
        pass
    #anticyclone par exemple, savoir si apres une semaine de pluie, solei ect les parti sont les meme
    #anti aug polution

    

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


    def durée_température(self):
        pass

    #faire hier et demain
    #faire la semaine ex une semaine de canicule pollu ? une semaine de froit intense polu?

 

        



class trafique:
    
    def trafique(self):

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
            agé = [9, 15 ,18]
            enfant = [8, 12, 14, 16, 17]
            pointe = []#reverifie les pointes

            #activité le mercredi samedi jeudi soir ?
            #savoir quand est ce que les types de gens sortent:
        #vieux 9 15 18
        #jeune enfant 8 12h/14h/16 /17
        #moyen vieux heure de pointe 


        
        def voiture_presente(self):
            pass
        #savoir quel type de voiture est présente sur la voie



        def travaux(self):
            pass
        #les travaux impactent ils la pollution? si oui fais chier pcque faut aussi chercher si c
        #une rue principale

        def essence(self):
            pass
        #savoir dans la semaine, dans les semaines quelles type dessence a ete le plus acheter


        def poid_lourd(self):
            pass


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



            

    
class geographie:

    def situation(self):
        pass
    #dans un trou entre des montagnes? pres de la mer ect
    
    def voisinage(self):
        pass
    #savoir si la ville d'a coté peux influer et donc rentre en jeu avec vent


    def sol(self):
        pass
    #savoir si un sol influe

    
class socio:

    def habitant(self):
        pass
    #type de population ok vieux = vieille voiture
        #et pas de deplacement aux horriare de point car stratégie de leur expérience
    #type economique region riche? vieille voiture
    

    






class analyse:

    def analyse(self):
        pass#faire les combo et prendre le meilleur sauf que y'a pas de combo a faire j'ai deja le resurtat...



    
    #sinon faire de la prédiction mais je sais pas faire
    #en vrai j'ai juste le dessin je sais pas si ca marche ca


    def prédiction(self):
        pass
    #selon les truk faire des ca sera entre tant et tant de pollution
    #tentre t'as ville et ca fait des recherches automatiquement

    #nuage de pts







if __name__ == "__main__":

    yo = couleur_ciel()
    meteo = météo()
    température = climat()
    trafique = trafique()
    particule = particule()
    liste_dossier = os.listdir(PATH_DOSSIER)

    
    #-----------------ici un forme genre voir donnée paris ca prend l'image et bim
    yo.lieu("marseille")
    #mettre un form
    #a = form
    #b = yo.lieu(a) et ca fait tout le bordel dapres
    #-------------------------------------------------------


    #------------------------------------------ici
    #un autre qui apprend

    for i in liste_dossier:
        if i == "pol.py" or i == "essais.py" or i == "ciel.png"\
           or i == "ciel.jpg":
            pass
        else:

            print(i)
            
            #mask = yo.mask(i) <- mask = yo.mask(b)
            
            #couleur_du_ciel = yo.ciel_terre(mask)
            #yo.analyse_ciel_couleur(couleur_du_ciel)

            #position = meteo.recuperation_lieu(i)
            
            #meteo.recuperation_donnée(position)

            #température.recuperation_donnée(position)

            #trafique.trafique()

            #particule.particule(position)

            #print(CIEL)
            #print(METEO)
            #print(CLIMAT)
            #print(TRAFIQUE)
            #print('\n\n\n')




        #ecrire ca dans un fichier

    
            
        CIEL = {'bleu':0,
                'gris':0,
                'blanc':0,
                'bleu_pollution':0,
        }


        METEO = {'beau_temps':0,
                 'nuageux':0,
                 'pluie':0,
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



        VENT = {'tres fort':0,
        'fort':0,
        'moyen fort':0,
        'faible':0, 
        }

        TEINTE_GRIS = {'lvl 1':0,
               'lvl 2':0,
               'lvl 3':0,
               'lvl 4':0,
               'lvl 5':0,
               'lvl 6':0,
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




















    

