def vasemmalle(bitit, kierros):
    for _ in range(kierros):
        bitit = bitit[1:] + bitit[0]
    return bitit


def oikealle(bitit, kierros):
    for _ in range(kierros):
        bitit = bitit[-1] + bitit[:-1]
    return bitit


def main():
    bitit = input("Anna bitit: ")
    kierros = int(input("Anna Kierroksien lukumäärä: "))
    suunta = input("Anna Kierroksien suunta (vasen/oikea): ").lower()

    if suunta == "vasen":
        tulos = vasemmalle(bitit, kierros)
    elif suunta == "oikea":
        tulos = oikealle(bitit, kierros)

    print("Pyöritettynä:", tulos)


# En keksinyt muuta tapaa aloittaa Funktiota :)
if 0 == 0:
    main()
