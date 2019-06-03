

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



    didif = []
    c1 = 0
    for i in liste:

        for j in liste:
            compteur = 0
            c = 0
            #print(i)
            #print(j)
    
            ici = []
            
            for ii in i:
                #print(ii, j[compteur])
                if ii != j[compteur]:
                    c += 1
                    ici.append(c)
                compteur+=1

            
            #print('\n')
            if c == 1:
                didif.append([ici[0], c1])
        c1 += 1 

        break
       

    print(didif)
    
    print(mini)
    print(pol_mini)

    for i in didif:
        print(liste_pol[i[0]])
        print(liste[i[0]])
        print(liste[i[0]][i[1]])





















yoyo()

    























