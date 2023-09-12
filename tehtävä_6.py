lista = ["Petra", "Heidi", "Janne", "Petra", "Heidi", "Petra", "Petra"]
lista2 = [1, 1, 2, 3, 1, 5, 2, 4, 3]

def poistaDuplikaatit(lista):

    uusilista = set(lista)
    print(uusilista)

poistaDuplikaatit(lista)
poistaDuplikaatit(lista2)


