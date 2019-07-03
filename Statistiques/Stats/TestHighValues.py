import pandas as pd
from collections import Counter
from pylab import *
from scipy import stats

# Import des dix derniers fichiers pour faire des stats

rglobals = []
machines = []

nombreFichiers = 0
# Remplacer le 4 par le nombre de de fichiers lu (+1)
for i in range(1, 6):
    chaine = "C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\HighExecutionCities\\Dataset" + repr(
        i) + ".xlsx"
    print(chaine)
    rglobals.append(pd.read_excel(chaine, sheet_name='Params'))
    machines.append(pd.read_excel(chaine, sheet_name='Machine'))
    nombreFichiers = nombreFichiers + 1

# On récupère les data de nos fichiers (Axe Y)
tNB_CITY = []
tNB_TRUCKS = []
tDISTANCE = []

for rglobal in rglobals:
    tNB_CITY.append(rglobal['Value'][0])
    tNB_TRUCKS.append(float(rglobal['Value'][1]))
    tDISTANCE.append(float(rglobal['Value'][6]))
# On récupère notre temps (Axe X)
tResolvedTime = []
for machine in machines:
    tResolvedTime.append(machine['Value'][0])


def predict(X):
    for v in range(0, len(X)):
        X[v] = X[v] * slope + intercept
    return X


'''
print("===========GRAND NOMBRE CITIES===============")
X = tNB_CITY
Y = tResolvedTime
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)  # Regression linéaire
fitLine = predict(X)
axes = plt.axes()
axes.grid()
plt.scatter(X, Y)  # Nuage de point
plt.title('High Cities Number')
plt.xlabel('nb Cities')
plt.ylabel('Exec Time')
plt.plot(X, fitLine, c='r')
plt.show()
print(tNB_CITY)
print(tResolvedTime)
print("OK")
'''

'''
print("===========GRAND NOMBRE DISTANCE===============")
X = tDISTANCE
Y = tResolvedTime
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)  # Regression linéaire
fitLine = predict(X)
axes = plt.axes()
axes.grid()
plt.scatter(X, Y)  # Nuage de point
plt.title('High Trucks number')
plt.xlabel('nb Cities')
plt.ylabel('Exec Time')
plt.plot(X, fitLine, c='r')
plt.show()
print(tDISTANCE)
print(tResolvedTime)
print("OK")
'''

print("===========GRAND NOMBRE TRUCKS===============")
X = tNB_TRUCKS
Y = tResolvedTime
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)  # Regression linéaire
fitLine = predict(X)
axes = plt.axes()
axes.grid()
plt.scatter(X, Y)  # Nuage de point
plt.title('High Trucks number')
plt.xlabel('nb Cities')
plt.ylabel('Exec Time')
plt.plot(X, fitLine, c='r')
plt.show()
print(tNB_TRUCKS)
print(tResolvedTime)

