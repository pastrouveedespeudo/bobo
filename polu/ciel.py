
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

    def recherche_image_lyon(self, path):

        self.path = path
        liste = []

        
        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")


        liste.append(str(soup))
        return liste


    def lieu(self, lieu):
        self.lieu = lieu

    
        if self.lieu == "Paris" or self.lieu == "paris":
            
            path = "https://www.viewsurf.com/univers/ville/vue/16924-france-ile-de-france-paris-la-defense"
            image = couleur_ciel.recherche_image_paris(self, path)
            image = image[11][628:702]
            urllib.request.urlretrieve(image, "paris.jpg")

            return "paris.jpg"

        elif self.lieu == "Marseille" or self.lieu == "marseille":
            pass

        elif self.lieu == "Lyon" or self.lieu == "lyon":
            
            path = "https://fr.webcams.travel/webcam/1511302382-lyon-radisson-blu"
            image = couleur_ciel.recherche_image_lyon(self, path)
            image = image[0][23207:23291]
            urllib.request.urlretrieve(str(image), "lyon.png")




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

