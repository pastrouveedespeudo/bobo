import requests
from bs4 import *

LISTE = ['coiffure', 'COIFFURE', 'salon', 'salon de coiffure']





def rayon(ville):
    pass





def ville(ville):
    path = 'https://www.google.com/search?q={}+coiffeur&oq={}+coiffeur'
    path = path.format(ville, ville)
    #print(path)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")

    for i in propriete:
        print(i)


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



    

#ville('crest')
horraire("maryline coiffure crest", "crest")











