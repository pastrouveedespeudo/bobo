import datetime

def nuit_jour():
    nuit = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]


    date = datetime.datetime.now()
    heure = date.hour + 2
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

    

