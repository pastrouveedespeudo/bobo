import psycopg2

from .config import DATABASE
from .config import USER
from .config import HOST
from .config import PASSWORD


class table:
    def creation_table_donnée(self):

        conn = psycopg2.connect(database=DATABASE,
                                        user=USER,
                                        host=HOST,
                                        password=PASSWORD) 


        cur = conn.cursor()
        
        cur.execute("""create table bobo1(
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
        
        conn.commit()



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
    def visualisation_donnée(self):
        connexion_database.connexion(self)


        self.cursor.execute("""SELECT * from bobo1
                            """)
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]



        for i in liste:
            print(i)
            print('\n')





















