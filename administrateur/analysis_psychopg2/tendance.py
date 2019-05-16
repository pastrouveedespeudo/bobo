import psycopg2
from database import *


def data():
    conn = psycopg2.connect(database='bobo',
                        user='postgres',
                        host='127.0.0.1',
                        password='tiotiotio333')

    cur = conn.cursor()

    cur.execute("""select * from analyse_donnee1;""")

    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste


def i_into_i(liste):

    liste1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]

    c=0
    d = 0
    for i in liste[0][0]:
        try:
            if liste[0][0][d] == ')' and\
               liste[0][0][d+1] == ',' and liste[0][0][d+2] == ' '\
               and liste[0][0][d+3] == '('\
               and liste[0][0][d+4] == '[':
                c+=1
            
            elif i == '[':
                pass

            else:
                liste1[c].append(i)

            d+=1
            
        except:
            pass
        
    return liste1
    
def unification(liste1):
 
    liste2 = []
    for i in liste1:
        if i == []:
            pass
        else:
            i = "".join(i)
            liste2.append(i)
            
    return liste2

def suppression_en_trop(liste2):
    liste3 = []
    for i in liste2:
        liste3.append(i.split())


    liste4 = []
    for i in liste3:
        for j in i:
            mot = ''
            for k in j:
                if k == '(' or k == '"' or k == ',' or k == ')'\
                   or k ==']':
                    pass
                else:
                    mot += k
            liste4.append(mot)
    print(liste4)
                
    


def les_tendances_couleurs():
    pass



liste = data()
liste1 = i_into_i(liste)
liste2 = unification(liste1)
suppression_en_trop(liste2)
