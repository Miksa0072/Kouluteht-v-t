import random

def luo_lottorivi():
    return random.sample(range(1, 40), 7)

def tarkista_voitto(annettu_rivi, arvottu_rivi):
    oikein = 0
    for numero in annettu_rivi:
        if numero in arvottu_rivi:
            oikein += 1
    return oikein

def main():
    annettu_rivi = [int(x) for x in input("Anna lottorivi (7 lukua väliltä 1-39): ").split(",")]
    arvontojen_maara = int(input("Kuinka monta riviä arvotaan: "))

    voitot = [0, 0, 0, 0]
    
    for _ in range(arvontojen_maara):
        arvottu_rivi = luo_lottorivi()
        oikein = tarkista_voitto(annettu_rivi, arvottu_rivi)
        if oikein >= 4:
            voitot[oikein - 4] += 1

    for i, voittojen_maara in enumerate(voitot):
        if i == 0:
            print(f"{voittojen_maara} kertaa neljä oikein!")
        elif i == 1:
            print(f"{voittojen_maara} kertaa viisi oikein!")
        elif i == 2:
            print(f"{voittojen_maara} kertaa kuusi oikein!")
        elif i == 3:
            print(f"{voittojen_maara} kertaa seitsemän oikein!")

main()
