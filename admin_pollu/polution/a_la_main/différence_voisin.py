import psycopg2
import datetime



def heure_jour():
    
    date = datetime.datetime.now()
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute

    jour = str(jour)+'_'+str(mois)+'_'+str(année)
    heure = str(heure)+'_'+str(minute)
    
    return jour, heure




def visusu():

    datatime = heure_jour()
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    cursor = conn.cursor()


    cursor.execute("""select * from voisin_vent_pollution
                    where heure_donnée = '{}';""".format('11_37'))

    conn.commit()

    rows = cursor.fetchall()
    liste = [i for i in rows]


    liste_premier = [[i[1], i[2], i[3], i[4]] for i in liste]
    date = liste[0][5]
    
    return liste_premier, date



def différence(liste, liste_premier, date):


    datatime = heure_jour()
    
    print(date)
    print(datatime[1])
    print('\n')



    for i in liste_premier:
        print(i)
        
    print('\n')


    for i in liste:
        for j in i:
            print(j)























liste_premier = visu()
lliste = [[['duisburg-military-golf-club', 'Ouest', '20', 33], ['antwerp-golf-school', 'Sud-Ouest', '20', 26], ['bruxelles', 'Sud', '15', 15], ['liege', 'Sud-Ouest', '30', 22], ['antwerp-golf-school', 'Sud-Ouest', '20', 26]], []]

différence(lliste, liste_premier[0], liste_premier[1])
















































