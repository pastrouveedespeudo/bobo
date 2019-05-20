import psycopg2

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

a = visualisation('marseille')

for i in a:
    print(i)
    print('\n')






































