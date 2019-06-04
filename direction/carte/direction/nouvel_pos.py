from math import *

def long_lat(lat, long, km, sens):
    print(km)
    km = float(km)
    #print(lat, long, km, sens)

    #print(sens)
    
    kilometre = km * 0.009
    
    #print('metre, kilometre: ',km, kilometre)

    
    if sens == 'nordnordouest':
        lat1 = kilometre
        nouvel_lat = lat + lat1
        return nouvel_lat, long

    elif sens == 'nord':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(67.7))
        return lat, long

    elif sens == 'nordnordest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(45))
        return lat, long
        
    elif sens == 'nordest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(22.5))
        return lat, long

    elif sens == 'estnordest':
        long = long + kilometre
        return lat, long
        
    elif sens == 'est':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(157.5))
        return lat, long
        
    elif sens == 'estsudest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(135))
        return lat, long
        
    elif sens == 'sudest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(112.5))
        return lat, long

    elif sens == 'sudsudest':
        lat1 = kilometre
        nouvel_lat = lat - lat1
        return nouvel_lat, long

    elif sens == 'sud':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(337))
        return lat, long

    elif sens == 'sudsudouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(315))
        return lat, long
        
    elif sens == 'sudouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(292.5))
        return lat, long

    elif sens == 'ouestsudouest':
        
        kilo = kilometre
        long1 = long - kilo
      
        return lat, long1

    elif sens == 'ouest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(337))
        return lat, long
        
    elif sens == 'ouestnordouest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(315))
        return lat, long
        
    elif sens == 'nordouest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(292.5))
        return lat, long

