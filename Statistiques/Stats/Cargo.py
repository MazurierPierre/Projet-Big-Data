import pandas as pd

cargo = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset1.xlsx", sheet_name='Cargo')

nbTrucks = max(cargo['IDTruck'])
print("Nombre de camions utilisés : " + repr(nbTrucks))
print("Nombre d'objets chargés dans les camions : " + repr(len(cargo['IdObject'])))

x = 0
count = 0
countMax = 0
for i in range(0, nbTrucks+1):
    if count > countMax:
        countMax = count
    count = 0
    for y in cargo["IDTruck"]:
        if y == i:
            count = count+1
            print("Le camion " + repr(i) + " transporte l'objet : " + repr(cargo["IdObject"][x]))
            x = x + 1

print("Charge Max d'un camion : " + repr(countMax))


