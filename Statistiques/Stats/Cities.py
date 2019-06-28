import pandas as pd

cities = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset.xlsx", sheet_name='Cities')

print("=================VILLES=======================")
# print(cities)
maxCity = max(cities['IDCity'])
maxTimeDelivered = max(cities['TimeDelivered'])
print('Nombre de villes totales : ' + repr(maxCity))
print('Temps total programme : ' + repr(maxTimeDelivered) + ' tics')
print('Temps moyen pour une livraison : ' + repr(maxTimeDelivered / maxCity) + ' tics')
