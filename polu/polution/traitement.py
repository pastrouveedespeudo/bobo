
def display_dict(*args):
    liste = []
    for i in args:
        for key, value in i.items():
            if i[key] != 0:
                liste.append(key)
    print(liste)
    return liste


def raise_dict(*args):
    for i in args:
        for key, value in i.items():
            i[key] = 0

