
def début():
    return False

def condition_min(liste, LISTE_DEJA):

    c = 0
    liste_min_pol = []

    for i in liste:
        liste_min_pol.append(int(i[14]))

##        print(i[2], i[3],i[4],i[5],i[6],i[7],
##              i[8],i[9],i[10],i[11],i[12],i[13],
##              i[14],i[16],i[17],i[18],i[19],
##              i[20],i[21])
##        print('\n')

        c+=1


    #print(min(liste_min_pol))



    liste_condition_min = []
    for i in liste:
        if str(i[14]) == str(min(liste_min_pol)):
            liste_condition_min.append(i)

    #print(liste_condition_min)


    
    return liste_condition_min



def différence(liste, liste_condition_min, LISTE_DEJA):

    
    try:
        liste_condition_min_reduit = list(liste_condition_min[0][2:-2])
    except:
        liste_condition_min_reduit = list(liste_condition_min[2:-2])


    nombre_de_différence = []
    les_différences = []
    c = 0


    for i in liste:
        
        i_list = list(i[2:-2])
        c1 = 0
        counter = 0
        diff = []
        diff_origine = []
        
        for j in i_list:
            if j == liste_condition_min_reduit[c1]:
                counter += 1

            elif j!= liste_condition_min_reduit[c1]:
                diff.append(j)
                diff_origine.append(liste_condition_min_reduit[c1])
            c1+=1
        
        nombre_de_différence.append([len(diff)])
        les_différences.append(diff)
        
##        print(diff, 'différence de: ', len(diff))
##        print(diff_origine)
##
##        print('\n')

        c+=1


    return nombre_de_différence, les_différences, liste_condition_min_reduit,\
            liste



def différences(nombre_de_différence,
               les_différences,
               liste_condition_min_reduit,
               liste, LISTE_DEJA):


##    print(liste_condition_min_reduit)
##    print('\n\n')


    c = 0
    for i in liste:

##        print(int(i[14]), 'soit nombre de diff de pollu :', int(i[14]) - int(liste_condition_min_reduit[12]))
##
##        print('difference de condition :', nombre_de_différence[c])
##        print('qui sont :' , str(les_différences[c]))
##
##        print('\n')

        c+=1

    

    liste1 = []
    

    for i in liste:
        for j in LISTE_DEJA:
            if i[0] == j:
                liste.remove(i)
    
    for i in nombre_de_différence:
        liste1.append(i[0])

    liste2 = sorted(liste1)

    mini = min(liste2[1:])


    



    c = 0
    nb = 0
    for i in liste1:
        if mini == i:
            nb += c
            
        c+=1


##    print(liste_condition_min_reduit)
##    print('\n')
##    print(list(liste[nb][2:-2]))
##    print(les_différences[nb])
##    print(liste[nb][0])
    LISTE_DEJA.append(liste[nb][0])
##    print('\n')
##    print(LISTE_DEJA)

    
    return liste[nb]


































