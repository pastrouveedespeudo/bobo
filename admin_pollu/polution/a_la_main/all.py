import psycopg2




conn = psycopg2.connect(database='datu8fkornnndh',
                         user='pwtfmpvfpsujtw',
                         host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                         password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


cursor = conn.cursor()

liste1 = ['angrais', 'incendie', 'pression',
          'vent', 'météo', 'climat', 'saison',
          'region_industrielle',
          'population_active', 'traffique',
          'heure', 'weekend', 'bouchon',
          'activité', 'diesel', 'eruption',
          'jour_nuit', 'polenne', 'voisin',
          'pos_france']

liste2 = ['conditions']


for i in liste1:
    
    cursor.execute("""select *  from {};""".format(i))


    conn.commit()



  
    rows = cursor.fetchall()
    liste = [i for i in rows]


    for i in liste:
        print(i)
























