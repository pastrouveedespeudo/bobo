from database import visualisation_table
from database import creation_conditions

from variable import LIST_CITY

liste = ['paris']

class data:

    def condition(self):
        
        for ville in liste:
            print('\n')
            print(ville)
            data = creation_conditions.visualisation_without_time(self, ville)
            data = set(data)
            c = 0
            for i in data:
                #print(i)


                id_data = creation_conditions.recuperate_id(self, ville,
                                                            i[0],i[1],i[2],i[3],
                                                            i[4],i[5],i[6],i[7],
                                                            i[8],i[9],i[10],i[11],
                                                            i[12],i[13])
                
                particle = creation_conditions.recuperate_particle(self, ville,
                                                                   i[0],i[1],i[2],i[3],
                                                                   i[4],i[5],i[6],i[7],
                                                                   i[8],i[9],i[10],i[11],
                                                                   i[12],i[13])


                hour = creation_conditions.recuperate_hour(self, ville,
                                                            i[0],i[1],i[2],i[3],
                                                            i[4],i[5],i[6],i[7],
                                                            i[8],i[9],i[10],i[11],
                                                            i[12],i[13])
                

                #print(id_data)
                #print(hour)
                #print(particle)
                nb_particle = len(particle)
                mean = 0
                for i in particle:
                    mean += int(i[0])


                #print(mean)
                print(mean/nb_particle)
                c+=1
            
            print("il y a : ", c, 'données pour ', ville)
            






if __name__ == '__main__':
    
    data = data()
    data.condition()



































