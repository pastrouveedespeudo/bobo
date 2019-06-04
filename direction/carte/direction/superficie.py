import requests
from bs4 import *
from math import *


def superficie_ville(ville):

    path = 'https://www.google.com/search?ei=wjnsXOzeIZCAjLsPm62CgAo&q={}+superficie&oq={}+superficie'
    path = path.format(ville, ville)
    #print(path)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("div")

    liste = []

    for i in propriete:
        liste.append(str(i.string))
        
  
        
        print('\n')

        
    kilometre_carre = ''
    
    for i in liste:
        number = ''
        numbe = ''
        if kilometre_carre == True:
            break
        for j in i:
            if j == ',' or j == '.' and numbe == True:
                number+= str('.')
            try:
                j = int(j)
                if j == int(j):
                    number+=str(j)
                    numbe = True
            except:
                pass
            if j == '²':
                kilometre_carre = True
                break
                
        if kilometre_carre == True:
            break
       
    print(number)
    return number


        
#superficie_ville("crest")

























































