import datetime

def nuit_jour():
    nuit = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]


    date = datetime.datetime.now()
    heure = date.hour
    #heure + 2

    la_nuit = ''
    non_nuit = ''

    
    for i in nuit:
        if i == heure:
            la_nuit = 'nuit'
            return la_nuit
        else:
            non_nuit = 'non_nuit'

    return non_nuit

    
a = nuit_jour()
print(a)
