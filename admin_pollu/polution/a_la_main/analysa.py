

import psycopg2




def mini():
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    aaa = 'marseille'

    cursor.execute("""select *  from conditions2 where nom_ville = '{}' order by nombre_particule ;""".format(aaa))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]
##    ess = liste[:5]
##
##    for i in ess:
##        print(i)
##        print('\n')
   

    return liste[0]




def all():
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    aaa = 'marseille'

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

    c1 = 0
    diff = []
    
    for i in liste:
        c1 = 0
        for j in liste:
            c = 0
            c2 = 0
            com = 0
            for ii in i:
                if ii != liste[c1][c]:
                    c2 +=1
                    com = c
                c+=1
            if c2 == 1:
                diff.append([liste.index(i), c1, com])
            c1+=1
            com += 1


    MINI_TO_DIFF = []

    
    for i in diff:

        c = 0
        compteur = 0
        diffs = []
    
        
        for j in liste[i[0]]:
            if j != mini[c]:
                diffs.append(j)
                compteur += 1
            c+=1
            
        if compteur == 1:
            MINI_TO_DIFF.append([liste[i[0]], liste_pol[i[0]], diffs])



    return MINI_TO_DIFF
    
  
def différence(MINI_TO_DIFF):

    all_condition, polution = rangement_liste()
    minimum = mini()

    data = []
    yoyo = 0
    
    while True:

        if yoyo = 0:
            yo = []
            c_polu = 0
            for condition in all_condition:
                
                for i in MINI_TO_DIFF:
                    c = 0
                    compteur = 0
                    e = []
                    for condi in condition:
                        if condi != i[0][c]:
                            e.append([i[0][c], condi])
                            compteur += 1
                        c += 1
                    if compteur == 1:
                        yo.append(condition)
                        data.append([e, polution[c_polu]])
          
                 c_polu += 1
                 yoyo += 1
        
        else:
            a = len(yo)
            c_polu = 0
            for condition in yo:
                
                for i in MINI_TO_DIFF:
                    c = 0
                    compteur = 0
                    e = []
                    for condi in condition:
                        if condi != i[0][c]:
                            e.append([i[0][c], condi])
                            compteur += 1
                        c += 1
                    if compteur == 1:
                        yo.append(condition)
                        data.append([e, polution[c_polu]])
          
                 c_polu += 1
                 yoyo += 1
                 yo = yo[len:]
        

    


a = yoyo()
différence(a)
























