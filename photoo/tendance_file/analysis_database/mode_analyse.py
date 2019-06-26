from .database import visualisation_table



class visu:

    def visu(self):
        vision = visualisation_table.visualisation_donnée(self)
##        print(vision[0][0])
##        print(vision[0][1])
##        print(vision[0][2])
##        print(vision[0][3])
##        print(vision[0][4])
##        print(vision[0][5])
##        print(vision[0][6])
##        print(vision[0][7])
        
        return vision
        
        

    def visu2(self):
        
        vision2 = visualisation_table.visualisation_donnée2(self)
        print(vision2)
        print(vision2[0][0])
        print(vision2[0][1])
        print(vision2[0][2])
        print('88888888888884463545646879878967487496')


visu = visu()
vision = visu.visu()


def recup():
    return vision


    
