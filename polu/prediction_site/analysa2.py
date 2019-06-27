import psycopg2
import datetime

from .angrais import *
from .climat import *
from .diesel import *
from .eruption import *
from .incendie import *
from .jour_nuit import *
from .météo import *
from .particule import *
from .polenne import *
from .socio import *
from .trafique import *

from .aide_analysa2 import *

from statistics import *

def predi_analysa2(ville):
    
    liste = [ville]

    condition = []
    for i in liste:
        
        m = particule2(i)
        print('taux de particule de', m, 'a', i)


        a = periode_angrais()
        condition.append(a)
       
        c = saison()
        condition.append(c)
       
        d = recup_tag()
        condition.append(d)
      
##        e = eruption()
##        condition.append(e)
     
        g = nuit_jour()
        condition.append(g)
      
        r = trafique_circulation()
        condition.append(r)
     
        s = heure_de_pointe()
        condition.append(s)
        
        t = habitude()
        condition.append(t)
     
        u = bouchons(i)
        condition.append(u)
     
        v = activité_execptionnelle(i)
        condition.append(v)

        q = habitant(i)
        condition.append(q)
      
##        n = industrie(i)
##        condition.append(n)

        #o = polenne(i)
        #condition.append(o)

##        l = france(i)
##        condition.append(l)
      
        h = recuperation_donnée_météo(i)
        condition.append(h)
        
        j = vent(i)
        condition.append(j)
        
        k = pression(i)
        condition.append(k)
        
        b = recuperation_donnée_température(i)
        condition.append(b)
     
##        f = incendie(i)
##        condition.append(f)

        
    print(condition)
    les_conditions = vision(ville)

    same = []
    for i in les_conditions:
        c = 0
        diff = 0
        for j in i[:-1]:
            if j != condition[c]:
                diff += 1
            c+=1
        if diff == 0:
            same.append(i[-1])

    print(same)

    liste_pol = []
    for i in same:
        i = int(i)
        liste_pol.append(i)


    for i in liste_pol:
        print(i)

    try:
        moyenne = mean(liste_pol)
        print(moyenne)
    except:
        moyenne = 'pas de donnée'

    return moyenne





























