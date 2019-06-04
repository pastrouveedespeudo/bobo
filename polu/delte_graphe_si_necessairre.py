import os

os.chdir('/app/static/popo')
liste = os.listdir()


liste = liste[1:]
for i in liste:
    os.remove(i)
