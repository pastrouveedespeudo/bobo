import mysql.connector
from config import *


        
class create_base:
    def database(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE POLUTION""")
        self.connexion.commit()

class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use POLUTION""")
        self.connexion.commit()


class table:
    def creation_table_donnée(self):
        connexion_database.connexion(self)
        self.cursor.execute("""create table ville(
                            nom_ville varchar(100),
                            date integer,
                            pression varchar(100),
                            météo varchar(100),
                            climat varchar(100),
                            saison varchar(100),
                            ville_pollué varchar(100),
                            REGION_INDUSTRIEL_POLLUEE varchar(100),
                            POPULATION_ACTIVE_HABITANT varchar(100),
                            TRAFIQUE varchar(100),
                            HEURE varchar(100),
                            POINTE varchar(100),
                            WEEKEND varchar(100),
                            BOUCHON varchar(100),
                            ACTIVITE_EXEPTIONNELLE varchar(100),
                            nombre_particule varchar(100));
                            
                            """)
        self.connexion.commit()




class insertion_table:
    def insertion(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""insert into 
                            () value('');
                
                            """)
        self.connexion.commit()

class visualisation_table:
    def visualisation(self):
        connexion_database.connexion(self)

        self.cursor.execute("""select * from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

    def visualisation_carre(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste
    
    def visualisation_rond(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste
    
    def visualisation_rectangle(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste
    
class suppression_table:
    def suppression(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""drop table ville;
                            """)
        self.connexion.commit()

           
    
if __name__ == "__main__":

    #partie database creation    
    #create_base = create_base()
    #create_base.database()

    #creation de la table
    #table = table()
    #table.creation_table_donnée()


    #suppression_table = suppression_table()
    #suppression_table.suppression()































    
