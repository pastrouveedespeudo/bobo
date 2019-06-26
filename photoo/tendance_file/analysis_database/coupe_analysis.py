from .database import visualisation_table

class visu:
    
    def visu2(self):
        """We call database"""
        
        vision2 = visualisation_table.visualisation_donnée2(self)
        liste = []
        
        for i in vision2:
            liste.append(i)

        return liste



visu = visu()
vision2 = visu.visu2()

def recup2():
    return vision2
