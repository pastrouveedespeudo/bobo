
#faut refaire c chiant

def couleur_cheuvelure(couleur1, couleur2, couleur3):


    if couleur1 > couleur2 + 10 and\
       couleur1 > couleur3 + 10 and\
       couleur1 > 50 and\
       couleur1 < 130:
        return "marron"



    if couleur1 < 50 and\
       couleur2 < 50 and\
       couleur3 < 50:
        return "noir"

        
    
    if couleur1 > 90 and\
       couleur2 > 90 and\
       couleur3 > 90 and\
       couleur1 >= couleur2 + 10 and\
       couleur2 >= couleur3 + 10:
        return "blond"
        



    
























