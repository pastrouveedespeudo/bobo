

import psycopg2




def yo():
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    aaa = 'lyon'

    cursor.execute("""select *  from conditions2 where nom_ville = '{}' order by nombre_particule ;""".format(aaa))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste[0]





conn = psycopg2.connect(database='datu8fkornnndh',
                         user='pwtfmpvfpsujtw',
                         host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                         password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
cursor = conn.cursor()
aaa = 'lyon'

cursor.execute("""select *  from conditions2 where nom_ville = '{}';""".format(aaa))


conn.commit()

rows = cursor.fetchall()
liste = [i for i in rows]
en_cours = []

a = yo()

a = list(a[2:-2])
#print(a)
#print('\n')
deja = []
debut = ''



liste1 = []
diffdiff = []

for i in liste:
    c = 0
    compteur = 0
    i = list(i[2:-2])
    diff = []
    for j in i:
        if j != a[c]:
            compteur +=1
            diff.append(j)

        c+=1
    diffdiff.append(diff)
    liste1.append(compteur)
  
liste123 = []

difffff = [[],[],[],[],[],[],[],
           [],[],[],[],[],[],[],
           [],[],[],[],[],[],[],
           [],[],[],[],[],[],[],[],
           [],[],[],[],[],[],
           [],[],[],[],[],[],[],
           [],[],[],[],
           [],[],[],[],[],[],
           [],[],[],[],[],[]]


for i in diffdiff:
    difffff[len(i)].append(i)


c = 0
for i in difffff:
    
    if i == []:
        pass
    else:
        print(c)
        
        print(i)
        print('\n')


    c+=1
    
   



   

    

    























