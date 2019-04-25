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
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            nom_ville varchar(100),
                            date INT,
                            heure_donnée INT,
                            pression varchar(100),
                            vent varchar(100),
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
                            nombre_particule varchar(100),
                            PRIMARY KEY(id) )
                            ENGINE=InnoDB;
                            
                            """)
        self.connexion.commit()




class insertion_table:
    def insertion_meteo(self, ville, date, heure_donnée, pressure, weather, wind):
        connexion_database.connexion(self)
        
        sql = ("""insert into ville
                        (nom_ville, date, heure_donnée, pression, météo, vent)
                         values(%s, %s, %s, %s, %s, %s);""")

        values = (ville, date, heure_donnée,
                  pressure, weather, wind)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_climat(self, climat, saison, date, heure_donnée, ville):
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET climat=%s, saison=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (climat, saison, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_polution(self, ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville):
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET ville_pollué=%s,
                   REGION_INDUSTRIEL_POLLUEE=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_sociologie(self, POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET POPULATION_ACTIVE_HABITANT=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_trafic_routier(self, TRAFIQUE, HEURE,
                                 POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE,
                                 date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET TRAFIQUE=%s,
                   HEURE=%s,
                   POINTE=%s,
                   WEEKEND=%s,
                   BOUCHON=%s,
                   ACTIVITE_EXEPTIONNELLE=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (TRAFIQUE, HEURE, POINTE, WEEKEND,
                  BOUCHON, ACTIVITE_EXEPTIONNELLE,
                  date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_particule(self, PARTICULE, date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET nombre_particule=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (PARTICULE, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()



class visualisation_table:
    def visualisation(self):
        connexion_database.connexion(self)

        self.cursor.execute("""select * from ville""")
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

           
    
#if __name__ == "__main__":

    #partie database creation    
    #create_base = create_base()
    #create_base.database()


    #suppression_table = suppression_table()
    #suppression_table.suppression()

    #creation de la table
    #table = table()
    #table.creation_table_donnée()

































    
