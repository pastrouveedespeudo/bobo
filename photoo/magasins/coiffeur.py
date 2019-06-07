import requests
from bs4 import *
import datetime


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
             or i.string == 'Etablir un lien':
             
             
            pass
             
        else:
            liste.append(i.string)

    liste = liste[3:]
    
    return liste #villes aux alentours


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
  
    return liste #coiffeur dans ces villes

def horraire(nom, ville):

    path = 'https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q={}+{}+horraires&oq={}+{}+horraires'
    path = path.format(nom, ville, nom, ville)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("tr")
    
    liste = []
    for i in propriete:
        liste.append(str(i))
    
    
    semaine = ['lundi',
              'mardi',
              'mercredi',
              'jeudi',
              'vendredi',
              'samedi',
              'dimanche',
             ]
    
    liste1 = []

    liste = liste[1:]

    for i in liste:
        heure = ''
        
        for j in semaine:
            b = str(i).find(str(j))
            if b >= 0:
                jour = j
        c = 0
        for ii in i:
            try:
                ii = int(ii)
                if ii == int(ii) and i[c+1] == ':' or i[c+2] == ':' or\
                   i[c-1] == ':' or i[c-2] == ':':
                    heure += str(ii)
            except:
                pass
            
            if ii == ':':
                heure += str(ii)
             
            if ii == '–':
                heure += str(ii)
            if ii == ',':
                heure += str(ii)
                    
            c += 1
        liste1.append([jour, heure])

    #print(liste1)
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
        #print(i)
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

les_coiffeurs = []

la_ville = 'eurre'


#alentour = rayon(la_ville)

##for i in alentour:
##    coif_alentour = les_coiffeurs = ville(i)
##    les_coiffeurs.extend(coif_alentour)
##
##
##print(les_coiffeurs)
    
#for i in les_coiffeurs:
#horraire('Coiffure Marilyne', 'crest')
numero('Coiffure Marilyne', 'crest')










