r1 = input("Telefonou para a vitima? [0 = não, 1 = sim]")
r2 = input("Esteve no local do crime? [0 = não, 1 = sim]")
r3 = input("Mora perto da vitima? [0 = não, 1 = sim]")
r4 = input("Devia para vitima? [0 = não, 1 = sim]")
r5 = input("já trabalhou para a vitima? [0 = não, 1 = sim]")

lista = [r1, r2, r3, r4, r5]
contadorSim = 0

for i in lista:
    if i == 1:
        contadorSim = contadorSim + 1
    if contadorSim == 2
    print("suspeita")

    elif contadorSim > 2 and contadorSim <= 5
    print("cumplice")

    elif contadorSim == 5
    print("Assassino")

    else:
        print("inocente")


    
