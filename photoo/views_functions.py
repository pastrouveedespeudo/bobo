"""here we try to lighten the views in code"""

#We trying or pass because
#it's a function who calling the database
#if the database is empty
#it return an error

#All of this
#is content into static.bobo becase
#they are functions
#who trait picture


from .tendance_file.analysis_database.tendance import la_tendance



from .magasins.address import *
from .magasins.gym import *
from .magasins.hairdresser import *



def the_colors_function(color):

    liste10 = la_tendance()

    if color == 'blonde':
        coul_analyse_haut = liste10[1][0]
        coul_analyse_bas = liste10[1][1]
         
    elif color == 'brune' or color == 'noire':
        coul_analyse_haut = liste10[0][0]
        coul_analyse_bas = liste10[0][1]

    elif color == 'chatain' or color == 'rousse':
        
        coul_analyse_haut = liste10[2][0]
        coul_analyse_bas = liste10[2][1]

    return coul_analyse_haut, coul_analyse_bas




def gymm_map_function(gymm_map, gym_pays):
    """here we retrieve the name of the
    gym sought by the user and
    seek his address"""
    
    the_address = address_geo(gymm_map, gym_pays)
    lat_long = city_geo(the_address)

    if lat_long == "Oups nous n'avons rien trouvé":
        return lat_long

    else:
        data = str(lat_long[0]) + ' ' + str(lat_long[1])
        return data



def gymm_function(gymm):
    
    gym_list = []

    the_cities = big_city_gym(gymm)
    
    for i in the_cities:
        if len(gym_list) == 4:
            return gym_list
            
        a = schedule_gym(i, gymm)

        if a != []:
            gym_list.append([i, a, ""])

    return gym_list



def haircut_style_function(haircut_style):
    
    coif = []
  
    the_hairdressers = cities(haircut_style)
    
    for i in the_hairdressers: 
        schedule1 = schedule_hair(i, haircut_style)

        if [schedule1] == [] or schedule1 == []\
           or schedule1 == "" or schedule1 == " "\
           or schedule1 == None:
            the_hairdressers.remove(i)
            
        else:
            coif.append([i, schedule1, ""])
            the_hairdressers.remove(i)

    return coif


def map_hairdresser_function(map_hairdresser, vivile):
    
    the_address = address_geo(map_hairdresser, vivile)
    
    lat_long = city_geo(the_address)
    if lat_long == "Oups nous n'avons rien trouvé":
        data =  "Oups nous n'avons rien trouvé"
        
    else:
        data = str(lat_long[0]) + ' ' + str(lat_long[1])
    
    return data


























