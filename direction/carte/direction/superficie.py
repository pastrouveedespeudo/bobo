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
        
    kilometre_carre = ''
    
    for i in liste:
        number = ''
        numbe = ''

        c = 0
        for j in i:
            c1 = 0
            if j == ',' or j == '.':
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
            c1 += 1
        if kilometre_carre == True:
            break
    c+=1
    print(number)

    number_final = ''
    c2 = 0
    for i in number:

        if i == '.':
            if number[c2 - 1] != '.' and number[c2 + 1] != '.':
                number_final += '.'
        try:
            i = int(i)
            if i == int(i):
                number_final += str(i)
        except:
            pass
        
        c2 += 1
        
    print(number_final)
    return number_final


superficie_ville("crest")

























































