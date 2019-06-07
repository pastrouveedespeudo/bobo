import requests
from bs4 import *

LISTE = ['coiffure', 'COIFFURE', 'salon', 'salon de coiffure']





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
             or i.string == '' or i.string == 'Etablir un lien':
             
             
            pass
             
        else:
            liste.append(i.string)

    liste = liste[3:]
    print(liste)
    return liste


def ville(ville):
    path = 'https://www.google.com/search?q={}+coiffeur&oq={}+coiffeur'
    path = path.format(ville, ville)
    #print(path)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")

    liste = []

    for i in propriete:
        #print(i.string)
        for j in LISTE:
            a = str(i.string).find(str(j))
            if a >= 0:
                liste.append(i.string)
    print(liste)
    return liste

def horraire(nom, ville):

    path = 'https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q={}+{}+horraires&oq={}+{}+horraires'
    path = path.format(nom, ville, nom, ville)
    #print(path)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div")
    for i in propriete:
        print(i.string)



    

ville('crest')
#horraire("maryline coiffure crest", "crest")

#rayon('crest')









