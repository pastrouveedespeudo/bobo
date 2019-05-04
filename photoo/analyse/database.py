import mysql.connector

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE



class create_base:
    def database(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE BOBO""")
        self.connexion.commit()



class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use BOBO""")
        self.connexion.commit()




class table:
    def creation_table_donnée(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""create table bobo1(
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            image varchar(100),
                            sexe varchar(100),
                            coiffure varchar(100),
                            haut text,
                            bas text,
                            taille_haut int,
                            taille_bas int,
                            PRIMARY KEY(id) )
                            ENGINE=InnoDB;
                            """)
        self.connexion.commit()





class insertion_table:
     
    def insertion_info(self, nom, sexe, haut, bas, taille_haut, taille_bas):
        connexion_database.connexion(self)

        self.taille_haut = taille_haut
        self.taille_bas = taille_bas
        self.nom = nom
        self.sexe = sexe
        self.haut = haut
        self.bas = bas
        
        
        sql = ("""insert into bobo1
                 (image, sexe, haut, bas, taille_haut, taille_bas)
                 values(%s, %s, %s, %s, %s, %s);""")

        values = (self.nom, self.sexe, self.haut, self.bas, self.taille_haut,
                  taille_bas)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def coiffure(self, coiffure, image):

        self.coiffure = coiffure
        self.image = image

        connexion_database.connexion(self)
        
        sql = ("""update bobo1
                set coiffure = %s
                where image = %s;""")

        values = (self.coiffure, self.image)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()



class visualisation_table:
    
    def visualisation(self, ville):
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT date, heure_donnée,
                            pression, météo, vent, climat,
                            saison, ville_pollué,
                            REGION_INDUSTRIEL_POLLUEE,
                            POPULATION_ACTIVE_HABITANT,
                            TRAFIQUE, HEURE, POINTE, WEEKEND,
                            BOUCHON, ACTIVITE_EXEPTIONNELLE,
                            particule
                            FROM ville
                            WHERE nom_ville = %s
                            ORDER BY particule
                            """, (ville,))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste



#if __name__ == "__main__":
    
    #create_base = create_base()
    #table = table()
    
    #create_base.database()

    #table.creation_table_donnée()
    #table.creation_table_donnée()




    








    








    








    





        
