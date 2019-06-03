

import psycopg2




def mini():
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




def all():
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

    return liste
    
    

def rangement_mini():

    minimum = mini()

    minimum_pol = [minimum[14]]
    minimum1 = list(minimum[2:14])
    minimum2 = list(minimum[15:-2])

    minimum3 = minimum1 + minimum2



    return minimum3, minimum_pol


def rangement_liste():

    liste = all()
    liste_pol = []
    liste_liste = []
    for i in liste:
        
        liste_pol.append(i[14])
        
        list_i1 = list(i[2:14])
        list_i2 = list(i[15:-2])
        list_i3 = list_i1 + list_i2

        liste_liste.append(list_i3)



    return  liste_liste, liste_pol


def yoyo():
    
    mini, pol_mini = rangement_mini()
    liste, liste_pol = rangement_liste()


    

    pression = []
    vent = []
    météo = []
    climat = []
    saison = []
    region_industrielle = []
    traffique = []
    heure = []
    weekend = []
    bouchon = []
    activité = []
    angrais = []
    diesel = []
    eruption = []
    incendie = []
    jour_nuit = []
    polenne = []
    pos_france = []



    c1 = 0
    diff = []
    
    for i in liste:
        #print(liste.index(i))
        #print('\n')
        c1 = 0
        for j in liste:

            c = 0
            c2 = 0
            
            for ii in i:
                #print(ii, liste[c1][c])
                #print(c1)
                if ii != liste[c1][c]:
                    c2 +=1
                c+=1
       
            #print(c2)
            if c2 == 1:
                diff.append([liste.index(i), c1, c])
            c1+=1
            #print('\n')
                
    print(diff)
    
    print(liste[0])
    print(liste[2])





















yoyo()

    























