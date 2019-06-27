import datetime

def night_day():
    """Here we just recup information about the moment of
    the day"""
    
    night = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]

    date = datetime.datetime.now()
    hour = date.hour
    
    if hour == 23: 
        hour = 1
    elif hour == 24:
        hour = 2
    else:
        hour + 2 

    the_night = ''
    no_night = ''

    
    for i in night:
        if i == hour:
            the_night = 'nuit'
            return the_night 
        else:
            no_night = 'jour'

    return no_night

    


