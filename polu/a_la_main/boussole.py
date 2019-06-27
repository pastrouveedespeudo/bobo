def calcul_vent(direction):

    if direction == 0 or direction == 360:
        return 'nord'


    elif direction > 0 and direction <= 22.5:
      
        return 'nordnordest'
    
    elif direction > 22.5 and direction <= 45:
      
        return 'nordnordest'
    
    elif direction == 45:
     
        return 'nordest'

    
    elif direction > 45 and direction <= 67.5:
     
        return 'estnordest'
    
    elif direction > 67.5 and direction <= 90:
  
        return 'estnordest'
    
    elif direction > 90 and direction <= 112.5:
        
        return 'est'
    
    elif direction > 112.5 and direction <= 135:
     
        return 'estsudest'
    
    elif direction == 135:
        
        return 'sudest'

    
    elif direction > 135 and direction <= 157.5:
       
        return 'sudsudest'

    
    elif direction > 157.5 and direction <= 180:
      
        return 'sudsudest'

    
    elif direction == 180:
      
         return 'sud'
         
    elif direction > 180 and direction <= 202.5:
    
        return 'sudsudouest'

    
    elif direction > 202.5 and direction <= 225:
     
        return 'sudsudouest'
    
    elif direction == 225:
        
        return 'sudouest'

    elif direction > 225 and direction <= 247.5:
       
        return 'sudouest'
    
    elif direction > 247.5 and direction <= 270:
     
        return 'ouestsudouest'
    
    elif direction > 270:
      
        return 'ouest'
    
    elif direction > 270 and direction <= 292.5:
      
        return 'ouestnordouest'
    
    elif direction > 292.5 and direction <= 315:
  
        return 'nordouest'
    
    elif direction == 315:

        return 'nordouest'
    
    elif direction > 315 and direction <= 337.5:
        return 'nordnordouest'
    
    #print('degres : ',degres)
