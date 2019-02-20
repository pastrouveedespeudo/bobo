import os
from PIL import Image



#chignon = {"haut":"t-shirt rouge", "bas":"jean bleu"}
#LISTE = [chignon]
CHIGNON = ["t-shirt rouge", "jean bleu"]
NOIR = [255, 255, 255]
BLEU = [0,0,255]

TRAITEMENT = []
POIDS = 0

#ici vetement selon la coupe
#selon le site

#faudra ajuster les para ex: chignon ou frange

def ajustage_couleur(bleu):

    ok = "BLEU"
    pas_ok = "PAS BLUWW"
    if bleu[0] >= 0 or bleu[0] <= 86\
       and bleu[1] >= 0 or bleu[1] <= 140\
       and bleu[2] >= 187 and bleu[2] <= 255:
        return ok
    else:
        return pas_ok
    
    #ne marche que pour le bleu et les autre peut etre
      #0     0    255
      #86     140  187
    

    
    


class vetement:

    def reinitialisation(self):
        POIDS = 0

    def search_data(self):
        pass


    def search_couleur(self):

        os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\vetement\pantalon")
        liste = os.listdir()

        dico = {}
        
        for i in liste:
            im = Image.open(str(i))
            for value in im.getdata(): 
                if value in dico.keys():
                    dico[value] += 1
                else:
                    dico[value] = 1
                break
            
  
        couleur_max = max(dico)

        ajustage = ajustage_couleur(couleur_max)

        if ajustage == "BLEU":
            POIDS += 1 #normalement ici on met genre pas bleu mais un autre truk
        elif ajustage != "BLEU":
            POIDS -= 1
        

    #1/-1/0

    def search_sexe(self):
        pass
    #-1 non 1 oui f=f 0 je sais pas

    def haut_bas(self):
        pass
    #comment reconnaitre un tshirt d'un pull?
    #forme pts image
    #on montre un fois on fait les poids
    #et sur 20 essais on lui fais apprendre ok


    
    #tshit tshirt manghe longue == skin detector oki
    #short//pantalon ok
    #shot//bermuda ok




    def choix(self):
        pass
    #ici affiche tous les max liste




    def ajout(self):
        pass
    #if + de 3 images chignon == t-shit+bermuda LISTE.append et du coup on doit
    #reco



yo = vetement()
yo.search_couleur()










        
