import requests
from bs4 import *


GYM = ['fitness', 'gym', 'body','Body', 'musculation']

def rayon(ville):
    path = "https://www.villorama.com/ville/{}/villes-proches.html"
    
    path = path.format(ville)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("a")

    liste = []

    for i in propriete:
        if i.string == None:
            pass
        elif i.string == 'France' or i.string == 'Distance à vol d\'oiseau'\
             or i.string == 'Communes proches' or i.string == 'Présentation'\
             or i.string == 'En bref' or i.string == 'Sport'\
             or i.string == 'Météo' or i.string == 'Prévisions météo'\
             or i.string == 'Sorties culturelles' or i.string == 'Agenda'\
             or i.string == 'Hôtels' or i.string == 'Midi Moins Une'\
             or i.string == 'mentions légales' or i.string == 'Recrutement'\
             or i.string == 'Midi Moins Une' or i.string == 'Gestion des cookies'\
             or i.string == 'Tourisme' or i.string == 'Office de Tourisme'\
             or i.string == 'Distance routière' or i.string == 'Mairie'\
             or i.string == 'Plan' or i.string == 'Itinéraire' or i.string == 'Annuaire Services'\
             or i.string == 'Résultats d\'élections' or i.string == 'Loisirs' or i.string == 'Spectacles'\
             or i.string == 'Concerts' or i.string == 'Théâtre' or i.string == 'Historique météo'\
             or i.string == 'Rencontres' or i.string == 'Autres informations' or i.string == 'Cinéma'\
             or i.string == 'Sites web' or i.string == 'Identifiez-vous' or i.string == 'Votre espace'\
             or i.string == 'Publicité' or i.string == '' or i.string == 'Conditions d\'Utilisation'\
             or i.string == 'Etablir un lien':
             
             
            pass
             
        else:
            liste.append(i.string)

    liste = liste[3:]
    
    return liste #villes aux alentours


def grande_ville_gym(ville):
    
    path = "https://www.google.com/search?ei=w2n6XJ3hMMeOatXLjOgB&q=sale+de+gym+{0}&oq=sale+de+gym+{0}"
    
    path = path.format(ville)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")
    liste1 = []
    for i in propriete:

        for j in GYM:
            a = str(i.string).find(str(j))
            if a >= 0:
                liste1.append(i.string)
    print(liste1)
    return liste1
    liste = []
    

def horraire(nom, ville):
    path = 'https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q={0}+{1}+horraires&oq={0}+{1}+horraires'

    path = path.format(nom, ville)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")

    liste = []
    for i in propriete:
        liste.append(i.string)
    
    semaine = ['lundi',
              'mardi',
              'mercredi',
              'jeudi',
              'vendredi',
              'samedi',
              'dimanche',
             ]
    
    jour = ''

    liste1 = []
    c = 0
    for i in liste:
        heure = ''

        for j in semaine:
            a = str(i).find(str(j))
            if a >= 0:
                liste1.append([i, liste[c+1]])
                
        c+=1
      
       
    print(liste1)
    return liste1

    



def numero(nom, ville):

    path = "https://www.google.com/search?ei=oFr6XJ-0INGua6y9o4gJ&q={}+{}+numero&oq={}+{}+numero"
    path = path.format(nom, ville, nom, ville)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div")

    liste = []
    for i in propriete:
        if i.string == None:
            pass
        else:
            liste.append(i.string)


    tel = ''

    fini = ''
    for i in liste:

        c = 0
        for j in i:
            try:
                a = int(i[0])
                b = int(i[1])
                if a == int(a) and b == int(b):
                    tel += i
                    fini = True
                    break
            except:
                pass
            c += 1
        if fini == True:
            break

    print(tel)
    return tel






















#a = rayon('crest')
#print(a)
#grande_ville_gym('crest')
#horraire("Body's Studio", "crest")
numero("Body's Studio", "crest")






















