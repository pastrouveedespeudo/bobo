import datetime

def display_dict(*args):
    liste = []
    for i in args:
        for key, value in i.items():
            if i[key] != 0:
                liste.append(key)
    print(liste)
    return liste

def display_dict_particule(*args):
    liste = []
    for i in args:
        for key, value in i.items():
            print(key, value)
            if i[key] != 0:
                liste.append(value)
    print(liste)
    return liste

def raise_dict(*args):
    for i in args:
        for key, value in i.items():
            i[key] = 0


def date_heure():

    date = datetime.datetime.now()

    
    day = date.day
    month = date.month

    date_donnée = str(day)+ str(month)
    date_donnée = int(date_donnée)

    hour = date.hour
    minute = date.minute

    heure_donnée = str(hour)+ str(minute)
    

    return date_donnée, heure_donnée

















