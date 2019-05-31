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
        elif c == 3:
            liste.append(j)
        c+=1

    ad = str(liste[0]+'+'+liste[1])
    return liste[0], ad

##if __name__ == '__main__':
##
##    a = dress_to_ville(45.4963988, 4.9078121)
##    print(a[0])
##    print(a[1])
    
