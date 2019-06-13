import psycopg2

conn = psycopg2.connect(database='datu8fkornnndh',
                         user='pwtfmpvfpsujtw',
                         host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                         password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


cursor = conn.cursor()

cursor.execute("""drop table conditions""")
