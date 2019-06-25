def the_colors_function(color):
    
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
