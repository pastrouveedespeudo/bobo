from conteneur import conteneur
import psycopg2
def lecture():

    


    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()




    
    liste = []
    with open('fichier_texte.py', 'r') as file:
        liste.append(file.read())


    c = 0
    mot = ''
    for i in liste:
        for j in i:
            
            if mot == 'STOP':
                c+=1
                mot = ''
                
            elif j == ' ':
                conteneur[c].append(mot)
                mot = ''
                
            else:
                mot += j
        
    liste3 = []
    for i in conteneur:
        if i == []:
            pass
        else:
            liste3.append(i)


    for i in liste3:
        for j in i:
            if j == 'moyen_fort':
                index = i.index(j)
                i[index] = 'moyen fort'
                
            elif j == 'tres_fort':
                index = i.index(j)
                i[index] = 'tres fort'
                
            elif j == 'regulier_jour':
                index = i.index(j)
                i[index] = 'regulier jour'
                
            elif j == 'assez_grand':
                index = i.index(j)
                i[index] = 'assez grand'
                
            elif j == 'tres_grand':
                index = i.index(j)
                i[index] = 'tres grand'
                       
           
            

        sql = ("""insert into yoyo
                (nom_ville, date, heure_donnée, pression, météo, vent, climat, saison, ville_pollué,
                REGION_INDUSTRIEL_POLLUEE, POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE, POINTE,
                WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE, nombre_particule, particule)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
                
        values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],
                  i[16],i[17],i[18])


        cursor.execute(sql, values)

        conn.commit()








    
lecture()
