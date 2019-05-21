import psycopg2

def un():
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()


    ##cursor.execute("""delete from ville where (bouchon='non_weekend and
    ##                bouchon='weekend'""")

    cursor.execute("""SELECT POINTE, HEURE particule FROM ville;""")

    conn.commit()



##    rows = cursor.fetchall()
##    liste = [i for i in rows]
##
##    for i in liste:
##        print(i)
##        print('\n')

def deux():
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()


    ##cursor.execute("""delete from ville where (bouchon='non_weekend and
    ##                bouchon='weekend'""")

    cursor.execute("""alter table ville drop POINTE;""")

    conn.commit()












un()
