import pandas as pd
from collections import Counter
from pylab import *
# Import des dix derniers fichiers pour faire des stats

cities = []
rglobals = []
cargos = []
robjects = []
roads = []
trucks = []
machines = []

nombreFichiers = 0
# Remplacer le 4 par le nombre de de fichiers lu (+1)
for i in range(1, 4):
    chaine = "C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset"+repr(i)+".xlsx"
    print(chaine)
    cities.append(pd.read_excel(chaine, sheet_name='Cities'))
    rglobals.append(pd.read_excel(chaine, sheet_name='Params'))
    cargos.append(pd.read_excel(chaine, sheet_name='Cargo'))
    robjects.append(pd.read_excel(chaine, sheet_name='Object'))
    roads.append(pd.read_excel(chaine, sheet_name='Roads'))
    trucks.append(pd.read_excel(chaine, sheet_name='Truck'))
    machines.append(pd.read_excel(chaine, sheet_name='Machine'))
    nombreFichiers = nombreFichiers + 1


print("=================VILLES=======================")
maxTimeDelivered = 0
maxCity = 0
for city in cities:
    maxTimeDelivered = maxTimeDelivered + max(city['TimeDelivered'])
    maxCity = maxCity + max(city['IDCity'])

print('Nombre de villes totales : ' + repr(maxCity))
print('Temps total des programmes : ' + repr(maxTimeDelivered) + ' tics')
print('Temps moyen pour une livraison : ' + repr(maxTimeDelivered / maxCity) + ' tics')
# Display sous forme de graphe des différentes évolutions de tics

x = []
y = []
count = 0
countCity = 0
for city in cities:
    count = 0
    countCity = countCity + 1
    x = []
    y = city['TimeDelivered']
    for time in y:
        x.append(count)
        count = count + 1
    plot(x, y, "b:o", label="Time Delivered - Ville " + repr(countCity))

title("Temps de livraison", fontdict=None, loc='center', pad=None)
plt.xlabel("Itérations")
plt.ylabel("Tics numbers")
legend()
show()


print("=================ROUTES - LIAISONS=====================")
# print(Counter(roads['IDCityTarget'].values))
eurelien = True
for road in roads:
    for i in Counter(road['IDCityTarget'].values).most_common(100):
        # print("La ville " + repr(i[0]) + " est en relation avec " + repr(i[1]) + " routes")
        if i[1] % 2 != 0:
            eurelien = False
if eurelien:
    print("Il existe un cycle eurélien parmis toutes les éxécutions")
else:
    print(" /!\\ Il n'existe pas de cycle eurélien parmis toutes les exécutions")
print("=================ROUTES - POIDS=======================")
avgWeightRoads = 0
medianWeightRoads = 0
Q1WeightRoads = 0
Q3WeightRoads = 0
modeWeightRoads = 0
for road in roads:
    avgWeightRoads = avgWeightRoads + road['Weight'].mean()  # moyenne poids
    medianWeightRoads = medianWeightRoads + road['Weight'].sort_values().median()  # mediane poids
    Q1WeightRoads = Q1WeightRoads + road['Weight'].sort_values().quantile(0.25)
    Q3WeightRoads = Q3WeightRoads + road['Weight'].sort_values().quantile(0.75)
    modeWeightRoads = modeWeightRoads + road['Weight'].mode()[0]

# 3 = nombre de fichiers
avgWeightRoads = avgWeightRoads / nombreFichiers
medianWeightRoads = medianWeightRoads / nombreFichiers
Q1WeightRoads = Q1WeightRoads / nombreFichiers
Q3WeightRoads = Q3WeightRoads / nombreFichiers
modeWeightRoads = modeWeightRoads / nombreFichiers
print('Temps moyen sur chaque route : ' + repr(avgWeightRoads) + ' tics')  # Equivaut au temps moyen pour une livraison
print('Q1 : ' + repr(Q1WeightRoads))
print('Médiane : ' + repr(medianWeightRoads))
print('Q3 : ' + repr(Q3WeightRoads))
print('Most common value : ' + repr(modeWeightRoads))

count = 1
data = []
BoxName = []
countBxPlot = []
for road in roads:
    BoxName.append("data" + repr(count))
    data.append(road['Weight'])
    countBxPlot.append(count)
    count = count+1

title("POIDS - ROUTES - SERIES", fontdict=None, loc='center', pad=None)
plt.boxplot(data)
xticks(countBxPlot, BoxName)
plt.show()

print("=================TRUCKS=======================")
nbTrucks = 0
nbHTrucks = 0
nbLTrucks = 0
for truck in trucks:
    nbTrucks = nbTrucks + (max(truck['IDTruck']))
    for i in truck['Type']:
        if i == 1:
            nbHTrucks = nbHTrucks + 1
        else:
            nbLTrucks = nbLTrucks + 1

print("Nombre de trucks : " + repr(nbTrucks))
print("Grand Camion : " + repr(nbHTrucks) + " --- " + repr(nbHTrucks/nbTrucks) + " %")
print("Petit Camion : " + repr(nbLTrucks) + " --- " + repr(nbLTrucks/nbTrucks) + " %")

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Grand Camions', 'Petits Camions'
sizes = [nbHTrucks, nbLTrucks]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

print("==================== OBJETS & EFFECTIFS =======================")

sumObject = 0
for robject in robjects:
    sumObject = sumObject + max(robject['IDObjet'])

print("Somme des objets : " + repr(sumObject))

sumObject = 0
effectifTotal = 0
valeurObjet = 0
# Proportion d'objets
print("Frequence")
tabFreq = []
tabObjet = []
tabFinalFreq = []
var = 0
for robject in robjects:
    # tabFinal
    # Récupération des fréquences
    tabFreq = []
    tabObjet = []
    valeurObjet = robject["Effectif"]
    sumObject = max(robject['IDObjet'])
    effectifTotal = sum(robject["Effectif"])
    for i in robject["IDObjet"]:
        if valeurObjet[i - 1] != 0:
            tabFreq.append(valeurObjet[i-1] / effectifTotal)
            tabObjet.append(i)
    # First init de tabFinalFreq
    if not tabFinalFreq:
        for x in range(0, len(tabFreq)):
            tabFinalFreq.append(0)
    for x in range(0, len(tabFreq)):
        tabFinalFreq[x] = tabFinalFreq[x] + tabFreq[x]

for i in range(0, len(tabFinalFreq)):
    tabFinalFreq[i] = tabFinalFreq[i]/nombreFichiers
    print("Objet " + repr(tabObjet[i]) + " = " + repr(tabFinalFreq[i]) + "%")


# Plots :

fig = plt.figure()
x = tabObjet
height = tabFinalFreq
width = 1.0
plt.bar(x, height, width, edgecolor="black")
title("Freq apparition objets", fontdict=None, loc='center', pad=None)
plt.show()

print("Frequence Cumulée Croissant")
y = 0
FreqCC = 0
tabFinalFreqCC = []
for robject in robjects:
    y = 0
    FreqCC = 0
    tabFinalFreqCC = []
    for i in robject["IDObjet"]:
        if valeurObjet[i - 1] != 0:
            FreqCC += tabFinalFreq[y]
            y = y+1
            tabFinalFreqCC.append(FreqCC)

for i in range(0, len(tabFinalFreqCC)):
    print("Objet " + repr(tabObjet[i]) + " = " + repr(tabFinalFreqCC[i]) + "%")


fig = plt.figure()
x = tabObjet
height = tabFinalFreqCC
width = 1.0
plt.bar(x, height, width, edgecolor="black")
title("Freq CC apparition objets", fontdict=None, loc='center', pad=None)
plt.show()

print("=====================Poids des objets=========================")
avgWeight = 0
medianWeight = 0
Q1Weight = 0
Q3Weight = 0
modeWeight = 0
poids = 0
for robject in robjects:
    avgWeight = avgWeight + robject['Weight'].mean()  # moyenne poids
    medianWeight = medianWeight + robject['Weight'].sort_values().median()  # mediane poids
    Q1Weight = Q1Weight + robject['Weight'].sort_values().quantile(0.25)
    Q3Weight = Q3Weight + robject['Weight'].sort_values().quantile(0.75)
    modeWeight = modeWeight + robject['Weight'].mode()[0]
    poids = poids + sum(robject['Weight'])

# 3 = nombre de fichiers
avgWeight = avgWeight / nombreFichiers
medianWeight = medianWeight / nombreFichiers
Q1Weight = Q1Weight / nombreFichiers
Q3Weight = Q3Weight / nombreFichiers
modeWeight = modeWeight / nombreFichiers

print("Total des poids Objet : " + repr(poids))
print('Moyenne des poids: ' + repr(avgWeight))  # Equivaut au temps moyen pour une livraison
print('Q1 : ' + repr(Q1Weight))
print('Médiane : ' + repr(medianWeight))
print('Q3 : ' + repr(Q3Weight))
print('Most common value : ' + repr(modeWeight))

count = 1
data = []
BoxName = []
countBxPlot = []
for robject in robjects:
    BoxName.append("data" + repr(count))
    data.append(robject['Weight'])
    countBxPlot.append(count)
    count = count+1

title("POIDS - OBJETS", fontdict=None, loc='center', pad=None)
plt.boxplot(data)
xticks(countBxPlot, BoxName)
plt.show()

print("==========================CARGAISON===============================")
nbTrucks = 0
nbObject = 0

for cargo in cargos:
    nbTrucks = nbTrucks + max(cargo['IDTruck'])
    nbObject = nbObject + len(cargo['IdObject'])

print("Nombre de camions utilisés : " + repr(nbTrucks))
print("Nombre d'objets chargés dans les camions : " + repr(nbObject))

x = 0
count = 0
countMax = 0
for cargo in cargos:
    # print("SERIE")
    nbTrucks = max(cargo['IDTruck'])
    x = 0
    for i in range(0, nbTrucks+1):
        if count > countMax:
            countMax = count
        count = 0
        for y in cargo["IDTruck"]:
            if y == i:
                count = count+1
                # print("Le camion " + repr(i) + " transporte l'objet : " + repr(cargo["IdObject"][x]))
                x = x + 1

print("Charge Max d'un camion : " + repr(countMax))

print("=================GLOBAL=======================")
# print(cities)

NB_CITY = 0
tNB_CITY = []
NB_TRUCKS = 0
NB_OBJECT = 0
DENSITY = 0
OBJECT_SIZE = 0
RATIO_TRUCK = 0
DISTANCE = 0
for rglobal in rglobals:
    NB_CITY = NB_CITY + rglobal['Value'][0]
    NB_TRUCKS = NB_TRUCKS + rglobal['Value'][1]
    NB_OBJECT = NB_OBJECT + rglobal['Value'][2]
    DENSITY = DENSITY + rglobal['Value'][3]
    OBJECT_SIZE = OBJECT_SIZE + rglobal['Value'][4]
    RATIO_TRUCK = RATIO_TRUCK + rglobal['Value'][5]
    DISTANCE = DISTANCE + rglobal['Value'][6]
    tNB_CITY.append(rglobal['Value'][0])

NB_CITY = NB_CITY / nombreFichiers
NB_TRUCKS = NB_TRUCKS / nombreFichiers
NB_OBJECT = NB_OBJECT / nombreFichiers
DENSITY = DENSITY / nombreFichiers
OBJECT_SIZE = OBJECT_SIZE / nombreFichiers
RATIO_TRUCK = RATIO_TRUCK / nombreFichiers
DISTANCE = DISTANCE / nombreFichiers
nbTotal = NB_CITY + NB_TRUCKS + NB_OBJECT


print('% villes dans le programme : ' + repr((NB_CITY / nbTotal) * 100) + '%')
print('% camions dans le programme : ' + repr((NB_TRUCKS / nbTotal) * 100) + '%')
print('% objets dans le programme : ' + repr((NB_OBJECT / nbTotal) * 100) + '%')
print('Moyenne DENSITY : ' + repr(DENSITY))
print('Moyenne OBJECT_SIZE : ' + repr(OBJECT_SIZE))
print('Moyenne RATIO_TRUCK : ' + repr(RATIO_TRUCK))
print('Moyenne DISTANCE : ' + repr(DISTANCE))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '%villes', '%camions', '%objets'
sizes = [(NB_CITY / nbTotal) * 100, (NB_TRUCKS / nbTotal) * 100,(NB_OBJECT / nbTotal) * 100]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

print("======================MACHINE==========================")
resolvedTime = 0
nbIterations = 0
tResolvedTime = []
for machine in machines:
    resolvedTime = resolvedTime + machine['Value'][0]
    nbIterations = nbIterations + machine['Value'][1]
    tResolvedTime.append(machine['Value'][0])

resolvedTime = resolvedTime / nombreFichiers
nbIterations = nbIterations / nombreFichiers
print('Moyenne temps de résolution (s) : ' + repr(resolvedTime))
print('Moyenne nombre itérations : ' + repr(nbIterations))


x = tNB_CITY
y = tResolvedTime
plt.scatter(x,y)
plt.title('Nuage de points avec Matplotlib')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(tNB_CITY)