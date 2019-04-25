from database import visualisation_table

from variable import LIST_CITY

class data:
    def recup_météo_by_particle(self):

        for i in LIST_CITY:
            print('\n')
            print(i)
            
            meteo = visualisation_table.visualisation(self, i)
            for i in meteo:
                print(i)




data = data()
data.recup_météo_by_particle()
