import mysql.connector

def method():
    connexion = mysql.connector.connect(host='127.0.0.1',
                                             user='root',
                                             password='TioTioTio333')
    cursor = connexion.cursor()

    cursor.execute("""use POLUTION""")
    connexion.commit()


    cursor.execute("""select * from ville;""")


    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


a = method()

for i in a:
    c = 0
    for j in i[1:]:
        with open('fichier_texte.py', 'a') as file:
            file.write(str(j))
            file.write(' ')
            file.close()

        c+=1 
    c = 0
    with open('fichier_texte.py', 'a') as file2:
        file2.write('STOP ')

