"""Datetime 16/04/2019"""

import datetime

def night_day():
    """Here we just recup information about the moment of
    the day"""
    
    night = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]

    date = datetime.datetime.now()
    hour = date.hour
    
    if hour == 23:  #If hour is 11pm we redefine hour to 1 am
        hour = 1
    elif hour == 24: #Same thing
        hour = 2
    else:
        hour + 2 #We add +2h because Heroku server has -2 hour

    the_night = ''
    no_night = ''

    
    for i in night:#If the current hour == nigth list
        if i == hour:
            the_night = 'nuit'
            return the_night  #We return night
        else:
            no_night = 'jour'

    return no_night#Else we return day

    


