


def condition_min(liste):

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



def différence(liste, liste_condition_min):
    
    liste_condition_min_reduit = list(liste_condition_min[0][2:-2])
    #print('\n\n')

    
    différence_un = []

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
            
        if counter == len(liste_condition_min_reduit) - 1:
            différence_un.append(i)

            
        print(diff, 'différence de: ', len(diff))
        print(diff_origine)

        print('\n')

        
    print(différence_un)
  

        


























































