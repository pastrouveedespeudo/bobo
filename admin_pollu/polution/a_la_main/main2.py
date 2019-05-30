from angrais import *
from climat import *
from diesel import *
from eruption import *
from incendie import *
from jour_nuit import *
from météo import *
from particule import *
from polenne import *
from socio import *
from trafique import *


liste = ['lyon','paris','marseille']

a = periode_angrais()
c = saison()
d = recup_balise()
e = eruption()
g = nuit_jour()
r = trafique_circulation()
s = heure_de_pointe()
t = habitude()






for i in liste:

    
    u = bouchons(i)
    print('a', i, 'il y a un', u, 'bouchon')
    v = activité_execptionnelle(i)
    print('a', i ,'il y a manif ou pas ?', v)
    q = habitant(i)
    print('population active de', i, 'de :', q)
    n = industrie(i)
    print(i,'est dans une zone industrielle polluante ?', n)
    o = polenne(i)
    print('le taux de polenne a ', i, 'est : ', o)
    m = particule2(i)
    print('taux de particule de', m, 'a', i)
    l = france(i)
    print(i, 'est', l, 'en france')

    h = recuperation_donnée_météo(i)
    j = vent(i)
    k = pression(i)
    b = recuperation_donnée_température(i)

    f = incendie(i)
    
    print('la pression est', k,'a', i)
    print('le vent est :', j, 'a', i)

    print('il fait', h, 'à', i)
    print('incendie a', i ,'ojd ?', f)
    print('la température est dans une plage de: ', b)



print('période engrais ?', a)
print('saison : ', c)
print('augmentation du prix barille de diesel, du d+ et du dollar : ', d)
print('erruption cet semaine ? le :', e)
print('nous sommes en periode de :', g)
print('aujourd\'hui est il un départ routier ?', r)
print('est ce une heure de pointe ?', s)
print('quel periode de la semaine ?', t)








