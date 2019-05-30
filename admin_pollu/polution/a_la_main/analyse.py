import psycopg2




def visu1(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
    
    cursor.execute("""select * from angrais where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste
    

def visu2(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from saison where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))


    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu3(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from pression where date = '{}'
                and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu4(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from vent where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu5(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                        user='pwtfmpvfpsujtw',
                        host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                        password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from météo where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu6(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
        
    cursor.execute("""select * from climat where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu7(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
        
    cursor.execute("""select * from region_industrielle where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu8(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from population_active where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))


    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu9(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
        
    cursor.execute("""select * from traffique where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu10(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                        user='pwtfmpvfpsujtw',
                        host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                        password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from heure where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu11(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                        user='pwtfmpvfpsujtw',
                        host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                        password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from weekend where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste




def visu12(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
    
    cursor.execute("""select * from diesel where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))


    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu13(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()


    
    cursor.execute("""select * from activité where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu14(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from eruption where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu15(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from incendie where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu16(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

        
    cursor.execute("""select * from jour_nuit where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu17(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                        user='pwtfmpvfpsujtw',
                        host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                        password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
    cursor.execute("""select * from polenne where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu18(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
        
    cursor.execute("""select * from voisin where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visu19(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
        
    cursor.execute("""select * from pos_france where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu21(date, heure):


    conn = psycopg2.connect(database='datu8fkornnndh',
                        user='pwtfmpvfpsujtw',
                        host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                        password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()
    cursor.execute("""select * from nuit_froide where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))

    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste

def visu22(date, heure):

    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')


    cursor = conn.cursor()

    
    cursor.execute("""select * from bouchon where date = '{}'
                    and heure_donnée = '{}';""".format(date, heure))
                    
    rows = password=cursor.fetchall()
    liste = [i for i in rows]

    return liste







date = '30_5_2019'
heure = '19_56'

print(visu1(date, heure))
print(visu2(date, heure))
print(visu3(date, heure))
print(visu4(date, heure))
print(visu5(date, heure))
print(visu6(date, heure))
print(visu7(date, heure))
print(visu8(date, heure))
print(visu9(date, heure))
print(visu10(date, heure))
print(visu11(date, heure))
print(visu12(date, heure))
print(visu13(date, heure))
print(visu14(date, heure))
print(visu15(date, heure))
print(visu16(date, heure))
print(visu17(date, heure))
print(visu18(date, heure))
print(visu19(date, heure))
print(visu20(date, heure))
print(visu21(date, heure))
print(visu22(date, heure))




































