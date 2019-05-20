
import psycopg2



DATABASE = 'bobo'
PASSWORD = 'tiotiotio333'
USER = 'root'
HOST = '127.0.0.1'




def creation_table():

    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""create table ville(
                    id serial PRIMARY KEY,
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
                    particule varchar(100))
                    
                    """)
    
    conn.commit()


def suppression_table():
    

    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""DROP TABLE ville""")


    conn.commit()





def insertion_meteo(ville, date, heure_donnée, pressure, weather, wind):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333') 

    cursor = conn.cursor()
    
    sql = ("""insert into ville
                    (nom_ville, date, heure_donnée, pression, météo, vent)
                     values(%s, %s, %s, %s, %s, %s);""")

    values = (ville, date, heure_donnée,
              pressure, weather, wind)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_climat(climat, saison, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333') 

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET climat=%s, saison=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (climat, saison, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_polution(ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET ville_pollué=%s,
               REGION_INDUSTRIEL_POLLUEE=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_sociologie(POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET POPULATION_ACTIVE_HABITANT=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_trafic_routier(TRAFIQUE, HEURE,
                             POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE,
                             date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')  

    cursor = conn.cursor()
    
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

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_particule_plage(PARTICULE_PLAGE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET nombre_particule=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (PARTICULE_PLAGE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_particule(PARTICULE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET particule=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (PARTICULE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def clean_data():
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')
    
    cursor = conn.cursor()
    
    cursor.execute("""DELETE FROM ville
                    WHERE particule IS NULL;""")


    conn.commit()
    print('données nulles effacées')




def visualisation(ville):
    
    conn = psycopg2.connect(database='bobo',
                             user='postgres',
                             host='127.0.0.1',
                             password='tiotiotio333')
    cursor = conn.cursor()

    cursor.execute("""SELECT date, heure_donnée,
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
                       
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste












































































































































