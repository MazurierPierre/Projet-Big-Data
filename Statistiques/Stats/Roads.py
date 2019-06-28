import pandas as pd
from collections import Counter

roads = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset.xlsx", sheet_name='Roads')

print("=================LIAISON DES VILLES & DEGRES=======================")
# print(Counter(roads['IDCityTarget'].values))
eurelien = True
for i in Counter(roads['IDCityTarget'].values).most_common(100):
    print("La ville " + repr(i[0]) + " est en relation avec " + repr(i[1]) + " routes")
    if i[1] % 2 != 0:
        eurelien = False

if eurelien:
    print("Il existe un cycle eurélien")
else:
    print(" /!\\ Il n'existe pas de cycle eurélien")

print("=================ROUTES=======================")
# print(roads)

avgWeightRoads = roads['Weight'].mean();  # moyenne poids
medianWeightRoads = roads['Weight'].sort_values().median()  # mediane poids
Q1WeightRoads = roads['Weight'].sort_values().quantile(0.25)
Q3WeightRoads = roads['Weight'].sort_values().quantile(0.75)
modeWeightRoads = roads['Weight'].mode()[0]
# FirstQuarterWeightRoads = roads[]
print('Temps moyen sur chaque route : ' + repr(avgWeightRoads) + ' tics')  # Equivaut au temps moyen pour une livraison
print('Q1 : ' + repr(Q1WeightRoads))
print('Médiane : ' + repr(medianWeightRoads))
print('Q3 : ' + repr(Q3WeightRoads))
print('Most common value : ' + repr(modeWeightRoads))

