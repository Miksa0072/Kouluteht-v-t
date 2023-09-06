alkuluku = int(input("Anna luku:"))

if alkuluku <= 1:
    print("Numero ei ole alkuluku")
else:
    alkuluku_on_alkuluku = True
    for i in range(2, alkuluku):
        if alkuluku % i == 0:
            alkuluku_on_alkuluku = False
            break
    
    if alkuluku_on_alkuluku:
        print("Numero on alkuluku")
    else:
        print("Numero ei ole alkuluku")
