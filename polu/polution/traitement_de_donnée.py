from database import visualisation_table
from database import creation_conditions

from variable import LIST_CITY

liste = ['paris']

class data:
    def recup_data_by_particle(self):

        for i in liste:
            print('\n')
            print(i)
            
            meteo = visualisation_table.visualisation(self, i)
            for i in meteo:
                print(i)

    def visualisation_without_time(self):
        for ville in liste:
            print('\n')
            print(ville)
            data = creation_conditions.visualisation_without_time(self, ville)
            data = set(data)
            c = 0
            for i in data:
                print(i)

                id_data = creation_conditions.recuperate_id(self, ville,
                                                            i[0],i[1],i[2],i[3],
                                                            i[4],i[5],i[6],i[7],
                                                            i[8],i[9],i[10],i[11],
                                                            i[12],i[13])

                print(id_data)
                c+=1
            
            print(c)
            






    def recup_id(self):
        pass



            
data = data()
#data.recup_data_by_particle()
data.visualisation_without_time()



































