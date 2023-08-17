from math import sqrt # importaa matikka funktion
#kysyy käyttäjältä arvoa
a = int(input("anna arvo1:"))
#kysyy käyttäjältä arvoa
b = int(input("anna arvo2:"))
#kysyy käyttäjältä arvoa
c = int(input("anna arvo3:"))
#laskee neljö juuret
vastaus1 = (-b+sqrt(b**2-4*a*c))/(2*a)
vastaus2 = (-b-sqrt(b**2-4*a*c))/(2*a)
#tulostaa vastaukset
print(vastaus1, "ja", vastaus2)
