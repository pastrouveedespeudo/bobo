from database import visualisation_table



class visu:

    def visu(self):
        vision = visualisation_table.visualisation_donnée(self)
        print(vision[0][0])
        print(vision[0][1])
        print(vision[0][2])
        print(vision[0][3])
        print(vision[0][4])
        print(vision[0][5])
        print(vision[0][6])
        print(vision[0][7])
        
        vision2 = visualisation_table.visualisation_donnée2(self)
        print(vision2[0][0])
        print(vision2[0][1])
        print(vision2[0][2])


        

        
        


if __name__ == '__main__':

    visu = visu()
    visu.visu()
