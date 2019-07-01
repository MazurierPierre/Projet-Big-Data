import pandas as pd
from pylab import *

cities = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset1.xlsx", sheet_name='Cities')

print("=================VILLES=======================")
# print(cities)
maxCity = max(cities['IDCity'])
maxTimeDelivered = max(cities['TimeDelivered'])
print('Nombre de villes totales : ' + repr(maxCity))
print('Temps total programme : ' + repr(maxTimeDelivered) + ' tics')
print('Temps moyen pour une livraison : ' + repr(maxTimeDelivered / maxCity) + ' tics')

print(cities)

x = []
y = cities['TimeDelivered']
count = 0
for time in y:
    x.append(count)
    count = count+1
plt.xlabel("itérations")
plt.ylabel("tics numbers")
plot(x, y, "b:o", label="Time Delivered - Ville 1")
legend()
show()
