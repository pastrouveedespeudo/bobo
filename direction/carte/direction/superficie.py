import requests
from bs4 import *
from math import *


def superficie_ville(ville):

    path = 'https://www.google.com/search?ei=wjnsXOzeIZCAjLsPm62CgAo&q={}+superficie&oq={}+superficie&gs_l=psy-ab.3..33i160l3.47870.49141..49264...0.0..0.316.1867.0j9j1j1......0....1..gws-wiz.......0i71j35i39j0i20i263j0i67j0j0i10j0i203j0i22i30.KKnu850MPRU'
    path = path.format(ville, ville)
 
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("div")

    liste = []

    for i in propriete:
        liste.append(str(i.string))


    kilometre_carre = ''
    for i in liste:
        number = ''
        for j in i:
            if j == ',':
                number+= str('.')
            try:
                j = int(j)
                if j == int(j):
                    number+=str(j)
            except:
                pass
            if j == '²':
                kilometre_carre = True
                
        if kilometre_carre == True:
            break

    return number


        
#superficie_ville('Jardin')

























































