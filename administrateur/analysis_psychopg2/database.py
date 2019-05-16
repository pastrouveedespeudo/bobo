import psycopg2

from config import DATABASE
from config import USER
from config import HOST
from config import PASSWORD


class table:

    def creation_database(self):
        pass
    #faudra la faire create database bobo
    
    def creation_table_donnée(self):

        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        cur.execute("""create table bobo1(
                    id serial PRIMARY KEY,
                    image varchar(100),
                    sexe varchar(100),
                    coiffure varchar(100),
                    haut text,
                    bas text,
                    taille_haut int,
                    taille_bas int);
                    """)
        
        conn.commit()


    
    def creation_table_donnée2(self):

        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        cur.execute("""create table bobo1_coiffure(
                    id serial PRIMARY KEY,
                    image varchar(100),
                    coiffure varchar(100));
                    """)
        
        conn.commit()


    def table_analyse(self):

        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        cur.execute("""create table analyse_donnee1(
                    analyse_donnee text);
                    """)
        
        conn.commit()


class insertion_table:
     
    def insertion_info(self, nom, sexe, haut, bas, taille_haut, taille_bas):

        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333')

        cur = conn.cursor()

        
        self.taille_haut = taille_haut
        self.taille_bas = taille_bas
        self.nom = nom
        self.sexe = sexe
        self.haut = haut
        self.bas = bas
        
        
        cur.execute("""insert into bobo1
                 (image, sexe, haut, bas, taille_haut, taille_bas)
                 values(%s, %s, %s, %s, %s, %s);""",
                 (self.nom, self.sexe, self.haut, self.bas, self.taille_haut,
                 taille_bas))

        
        
        conn.commit()




    def coiffure(self, image, coiffure):
        
        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        self.coiffure = coiffure
        self.image = image


        
        cur.execute("""insert into bobo1_coiffure
                    (image, coiffure)
                    values(%s, %s);""", (self.image, self.coiffure))

        

        conn.commit()




class visualisation_table:
    def visualisation_donnée(self):
        
        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        cur.execute("""SELECT * from bobo1""")
                           
        
        rows = cur.fetchall()
        liste = [i for i in rows]


        return liste
        for i in liste:
            print(i)
            print('\n')

    def visualisation_donnée2(self):
        
        conn = psycopg2.connect(database='bobo',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333') 

        cur = conn.cursor()
        
        cur.execute("""SELECT * from bobo1_coiffure""")
                           
        
        rows = cur.fetchall()
        liste = [i for i in rows]


        return liste
        for i in liste:
            print(i)
            print('\n')

#table = table()
#table.table_analyse()
#table.creation_table_donnée()
#table.creation_table_donnée2()
#visualisation_table = visualisation_table()
#visualisation_table.visualisation_donnée()
















