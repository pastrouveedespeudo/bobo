import psycopg2


def creation_table():



    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    
    cursor = conn.cursor()
    
    cursor.execute("""create table ville_pression(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    pression varchar(100));""")

    conn.commit()


    cursor.execute("""create table ville_vent(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    vent varchar(100));""")

    cursor.execute("""create table ville_météo(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    météo varchar(100));""")
    conn.commit()


    cursor.execute("""create table ville_climat(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    climat varchar(100));""")
    conn.commit()

    
    cursor.execute("""create table ville_saison(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    saison varchar(100));""")

    conn.commit()


    cursor.execute("""create table ville_ville_pollué(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    ville_pollué varchar(100));""")

    conn.commit()

    cursor.execute("""create table ville_region_industrielle(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    REGION_INDUSTRIEL_POLLUEE varchar(100));""")

    cursor.execute("""create table ville_population_active(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    POPULATION_ACTIVE_HABITANT varchar(100));""")

    conn.commit()


    cursor.execute("""create table ville_traffique(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    TRAFIQUE varchar(100));""")


    conn.commit()

    cursor.execute("""create table ville_heure(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    HEURE varchar(100));""")


    conn.commit()



    cursor.execute("""create table ville_weekend(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    WEEKEND varchar(100));""")

    cursor.execute("""create table ville_bouchon(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100),
                    BOUCHON varchar(100));""")


    conn.commit()

    cursor.execute("""create table ville_activité(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    nombre_particule varchar(100),
                    heure_donnée INT,
                    ACTIVITE_EXEPTIONNELLE varchar(100));""")


    conn.commit()

    cursor.execute("""create table ville_nb_particule(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date INT,
                    heure_donnée INT,
                    nombre_particule varchar(100));""")
    conn.commit()






def suppression_table():
    

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    cursor.execute("""DROP TABLE ville""")


    conn.commit()





def insertion_meteo(ville, date, heure_donnée, pressure, weather, wind):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""insert into ville
                    (nom_ville, date, heure_donnée, pression, météo, vent)
                     values(%s, %s, %s, %s, %s, %s);""")

    values = (ville, date, heure_donnée,
              pressure, weather, wind)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_climat(climat, saison, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET climat=%s, saison=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (climat, saison, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_polution(ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET ville_pollué=%s,
               REGION_INDUSTRIEL_POLLUEE=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_sociologie(POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET POPULATION_ACTIVE_HABITANT=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_trafic_routier(TRAFIQUE, HEURE,
                             WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE,
                             date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET TRAFIQUE=%s,
               HEURE=%s,
               WEEKEND=%s,
               BOUCHON=%s,
               ACTIVITE_EXEPTIONNELLE=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (TRAFIQUE, HEURE,WEEKEND,
              BOUCHON, ACTIVITE_EXEPTIONNELLE,
              date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_particule_plage(PARTICULE_PLAGE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET nombre_particule=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (PARTICULE_PLAGE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def insertion_particule(PARTICULE, date, heure_donnée, ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""UPDATE ville
               SET particule=%s
               WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

    values = (PARTICULE, date, heure_donnée, ville)

    
    cursor.execute(sql, values)
    conn.commit()


def clean_data():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()
    
    cursor.execute("""DELETE FROM ville
                    WHERE particule IS NULL;""")


    conn.commit()
    print('données nulles effacées')


def clean_data2():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()
    
    cursor.execute("""DELETE FROM ville
                    WHERE (bouchon = 'None' and
                    climat = 'None');""")


    conn.commit()
    print('données nulles effacées')


def clean_data3():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()
    
    cursor.execute("""DELETE FROM ville
                    WHERE (bouchon = 'None' and
                    particule = 'None');""")


    conn.commit()
    print('données nulles effacées')

def clean_data4():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()
    
    cursor.execute("""DELETE FROM ville
                    WHERE particule = 'None';""")


    conn.commit()
    print('données nulles effacées')

def visualisation(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()

    cursor.execute("""SELECT date, heure_donnée,
                        pression, météo, vent, climat,
                        saison, ville_pollué,
                        REGION_INDUSTRIEL_POLLUEE,
                        POPULATION_ACTIVE_HABITANT,
                        TRAFIQUE, HEURE, WEEKEND,
                        BOUCHON, ACTIVITE_EXEPTIONNELLE,
                        particule
                        FROM ville
                        WHERE nom_ville = %s;
                        """, (ville,))
                       
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visualisation_without_time(ville):

    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()
    
    cursor.execute("""SELECT pression, météo, vent, climat,
                        saison, ville_pollué,
                        REGION_INDUSTRIEL_POLLUEE,
                        POPULATION_ACTIVE_HABITANT,
                        TRAFIQUE, HEURE, WEEKEND,
                        BOUCHON, ACTIVITE_EXEPTIONNELLE
                        FROM ville
                        WHERE nom_ville = %s
                        ORDER BY particule
                        """, (ville,))
                       
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def recuperate_particle(ville, pression, météo, vent, climat,
                      saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                      POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                      WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    
    cursor = conn.cursor()

    cursor.execute("""SELECT particule
                    FROM ville
                    WHERE (nom_ville = %s AND
                    pression LIKE %s AND
                    météo LIKE %s AND
                    vent LIKE %s AND
                    climat LIKE %s AND
                    saison LIKE %s AND
                    ville_pollué LIKE %s AND
                    REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                    POPULATION_ACTIVE_HABITANT LIKE %s AND
                    TRAFIQUE  LIKE %s AND
                    HEURE LIKE %s AND
                    WEEKEND LIKE %s AND
                    BOUCHON LIKE %s AND
                    ACTIVITE_EXEPTIONNELLE LIKE %s);
                    """, (ville, pression, météo, vent, climat,
                          saison, ville_pollué,
                          REGION_INDUSTRIEL_POLLUEE,
                          POPULATION_ACTIVE_HABITANT,
                          TRAFIQUE, HEURE, WEEKEND,
                          BOUCHON, ACTIVITE_EXEPTIONNELLE))
                       
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste













creation_table()























































































































