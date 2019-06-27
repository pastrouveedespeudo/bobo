"""Here we look if it's during the day or the night
for increment database"""

import datetime

def nuit_jour():
    nuit = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]


    date = datetime.datetime.now()
    heure = date.hour
    if heure == 23:
        heure = 1
    elif heure == 24:
        heure = 2
    else:
         heure = heure + 2
    #heure + 2

    la_nuit = ''
    non_nuit = ''

    
    for i in nuit:
        if i == heure:
            la_nuit = 'nuit'
            return la_nuit
        else:
            non_nuit = 'jour'

    return non_nuit

    

