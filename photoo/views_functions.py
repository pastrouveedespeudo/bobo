"""Here we cut code
from the weight"""

#We trying or pass because
#it's a function who calling the database
#if the database is empty
#it return an error

#All of this
#is content into static.bobo becase
#they are functions
#who trait picture
try:
    from static.bobo.tendance import dataaa
    from static.bobo.tendance import i_into_i
    from static.bobo.tendance import unification
    from static.bobo.tendance import suppression_en_trop
    from static.bobo.tendance import re_elment_de_liste
    from static.bobo.tendance import mise_en_dico
    from static.bobo.tendance import determination_couleur
    from static.bobo.tendance import les_tendances_couleurs
    from static.bobo.tendance import analyse_tendance  
except:
    pass



def the_colors_function(color):

    liste = dataaa()
    liste1 = i_into_i(liste)
    liste2 = unification(liste1)
    liste3 = suppression_en_trop(liste2)
    liste6 = re_elment_de_liste(liste3)
    liste7 = mise_en_dico(liste6)
    liste8 = determination_couleur(liste7)
    liste9 = les_tendances_couleurs(liste8)
    liste10 = analyse_tendance(liste9)
    
    if color == 'blonde':
        coul_analyse_haut = liste10[1][0]
        coul_analyse_bas = liste10[1][1]
         
    elif color == 'brune' or couleur == 'noire':
        coul_analyse_haut = liste10[0][0]
        coul_analyse_bas = liste10[0][1]

    elif color == 'chatain' or couleur == 'rousse':
        
        coul_analyse_haut = liste10[2][0]
        coul_analyse_bas = liste10[2][1]

    return coul_analyse_haut, coul_analyse_bas
