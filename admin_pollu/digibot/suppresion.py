import psycopg2


conn = psycopg2.connect(database='bobo',
                        user='postgres',
                        host='127.0.0.1',
                        password='tiotiotio333')  

cursor = conn.cursor()


cursor.execute("""delete from ville where (bouchon='non_weekend and
                bouchon='weekend'""")


conn.commit()



rows = cursor.fetchall()
liste = [i for i in rows]

for i in liste:
    print(i)
    print('\n')
