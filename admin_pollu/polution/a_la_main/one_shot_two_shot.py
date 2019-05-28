import psycopg2

def suppression_table():
    

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    cursor.execute("""DROP TABLE ville_pression""")
    conn.commit()

    cursor.execute("""DROP TABLE ville""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_vent""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_météo""")
    conn.commit()


    cursor.execute("""DROP TABLE ville_climat""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_saison""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_ville_pollué""")
    conn.commit()


    cursor.execute("""DROP TABLE ville_region_industrielle""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_population_active""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_traffique""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_heure""")
    conn.commit()
    cursor.execute("""DROP TABLE ville_weekend""")
    conn.commit()
    cursor.execute("""DROP TABLE ville_bouchon""")
    conn.commit()
    cursor.execute("""DROP TABLE ville_activité""")
    conn.commit()

    cursor.execute("""DROP TABLE ville_nb_particule""")
    conn.commit()


    




suppression_table()
