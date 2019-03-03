import matplotlib.pyplot as plt
import numpy as np
import pylab



def heurePointeBeauSemaine():
    
    fig = plt.figure()

    x = [1,2,3,4,5,6]
    BarName = [7,8,9,17,18,19]

    
    height = [50,60,70,80,90,100]
    width = 0.00


    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=40)

    plt.xlim(0,11)
    plt.ylim(40,150)


    plt.ylabel('Taux de pollution')
    plt.xlabel('Heure')
    plt.title('Taux moyen de pollution exprimé en heure\n condition beau temps jour de semaine 1(mars) heure de pointe')

    pylab.xticks(x, BarName, rotation=40)

    plt.savefig('HeurePointeBeauSemaine.png')
    plt.show()



def heurePointePluieSemaine():
    
    fig = plt.figure()

    x = [1,2,3,4,5,6]
    BarName = [7,8,9,17,18,19]

    
    height = [50,60,70,80,90,100]
    width = 0.00

    

    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=40)

    plt.xlim(0,11)
    plt.ylim(0,14)


    plt.ylabel('Taux de pollution')
    plt.xlabel('Heure')
    plt.title('Taux de pollution exprimé en heure\n condition beau temps jour de semaine heure de pointe')

    pylab.xticks(x, BarName, rotation=40)

    plt.savefig('HeurePointeBeauSemaine.png')
    plt.show()




heurePointeBeauSemaine()
heurePointePluieSemaine()


