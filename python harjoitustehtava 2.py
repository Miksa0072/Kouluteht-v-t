teksti = input("Anna teksti:",)

alijono = input("Anna haettava:")

yks = teksti.find(alijono)
kaks = teksti.find(alijono, yks+1)

print(alijono,"löytyy indeksistä",yks, "alkaen.","Alijonon", alijono,"toinen esiintymä indeksistä", kaks, "eteenpäin")
