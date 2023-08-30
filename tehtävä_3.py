#4-Bittisen muuntaminen desimaaliin

binaari = input("anna 4-bittinen binaariluku:")

if binaari.isdigit() and len(binaari) == 4 :
    binaari2 = int(binaari, 2)
    print("Binääriluku ",binaari, " on desimaalilukuna:",binaari2)
else:
    print("Arvo ei ole nelimerkkinen tai sisälsi kirjaimia!!")
