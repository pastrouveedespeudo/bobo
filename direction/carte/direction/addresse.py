import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
    
    return result
  

      
def dress_to_ville(lat, long):
    
    coordinates =(lat, long) 
    a = reverseGeocode(coordinates) 
    liste = []
    c = 0
    for i,j in a[0].items():
        if c == 2:
            liste.append(j)

        c+=1

    #print(liste)
    return liste[0]

    
    
