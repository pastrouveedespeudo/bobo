
def analyse_tendance(liste):

    c = 0
    liste_haut_marron = []
    liste_haut_blond = []
    liste_haut_chatain = []
    
    for i in liste:
        try:
            print(liste[c][0], liste[c][1], liste[c][3])
            
            if liste[c][3] == 'marron':
                liste_haut_marron.append(liste[c][0])
            elif liste[c][3] == 'blond':
                liste_haut_blond.append(liste[c][0])
            elif liste[c][3] == 'chatin':
                liste_haut_chatain.append(liste[c][0])
            
            c+=2
            
        except:
            pass


    print(liste_haut_marron,
          liste_haut_blond,
          liste_haut_chatain)


    dico_haut_marron = {}
    dico_haut_blond = {}
    dico_haut_chatin = {}
    
    for i in liste_haut_marron:
        dico_haut_marron[i] = 0
        
    for i in liste_haut_blond:
        dico_haut_blond[i] = 0
        
    for i in liste_haut_chatain:
        dico_haut_chatin[i] = 0


    for i in liste_haut_marron:
        for cle, valeur in dico_haut_marron.items():
            if i == cle:
                dico_haut_marron[cle] += 1

    for i in liste_haut_blond:
        for cle, valeur in dico_haut_blond.items():
            if i == cle:
                dico_haut_blond[cle] += 1

    for i in liste_haut_chatain:
        for cle, valeur in dico_haut_chatin.items():
            if i == cle:
                dico_haut_chatin[cle] += 1

                

    print(dico_haut_marron, dico_haut_blond, dico_haut_chatin)


    print('\n')


    liste_bas_marron = []
    liste_bas_blond = []
    liste_bas_chatain = []

    d = 1
    for i in liste:
        try:
            print(liste[d][0], liste[d][1], liste[d][3])

            if liste[d][3] == 'marron':
                liste_bas_marron.append(liste[d][0])
            elif liste[d][3] == 'blond':
                liste_bas_blond.append(liste[d][0])
            elif liste[d][3] == 'chatin':
                liste_bas_chatain.append(liste[d][0])

            d+=2
        except:
            pass
    
       
    print(liste_bas_marron,
          liste_bas_blond,
          liste_bas_chatain)

    dico_bas_marron = {}
    dico_bas_blond = {}
    dico_bas_chatin = {}
    
    for i in liste_bas_marron:
        dico_bas_marron[i] = 0
        
    for i in liste_bas_blond:
        dico_bas_blond[i] = 0
        
    for i in liste_bas_chatain:
        dico_bas_chatin[i] = 0


    for i in liste_bas_marron:
        for cle, valeur in dico_bas_marron.items():
            if i == cle:
                dico_bas_marron[cle] += 1

    for i in liste_bas_blond:
        for cle, valeur in dico_bas_blond.items():
            if i == cle:
                dico_bas_blond[cle] += 1

    for i in liste_bas_chatain:
        for cle, valeur in dico_bas_chatin.items():
            if i == cle:
                dico_bas_chatin[cle] += 1

    print(dico_bas_marron, dico_bas_blond, dico_bas_chatin)








    


























la_liste = liste = [('rouge', '2a.jpg', 'haut', 'marron'), ('bleu', '2a.jpg', 'bas', 'marron'), ('blanc', '3a.jpg', 'haut', 'marron'), ('bleu', '3a.jpg', 'bas', 'marron'), ('blanc', '4a.jpg', 'haut', 'marron'), ('bleu', '4a.jpg', 'bas', 'marron'), ('gris', '5a.jpg', 'haut', 'blond'), ('bleu', '5a.jpg', 'bas', 'blond'), ('blanc', '6a.jpg', 'haut', 'chatin'), ('blanc', '6a.jpg', 'bas', 'chatin'), ('gris', '7a.jpg', 'haut', 'marron'), ('gris', '7a.jpg', 'bas', 'marron'), ('rose', '8a.jpg', 'haut', 'marron'), ('bleu', '8a.jpg', 'bas', 'marron')] 

analyse_tendance(la_liste)
