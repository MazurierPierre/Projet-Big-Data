import pandas as pd
from pylab import *
from scipy import stats

# Import des dix derniers fichiers pour faire des stats

rglobals = []
machines = []

nombreFichiers = 0
# Remplacer le 4 par le nombre de de fichiers lu (+1)
for i in range(80, 110):
    chaine = "C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\datasets\\Dataset" + repr(
        i) + ".xlsx"
    print(chaine)
    rglobals.append(pd.read_excel(chaine, sheet_name='Params'))
    machines.append(pd.read_excel(chaine, sheet_name='Machine'))
    nombreFichiers = nombreFichiers + 1

# On récupère les data de nos fichiers (Axe Y)
tNB_CITY = []
tNB_TRUCKS = []
tDISTANCE = []
tCoolRate = []

for rglobal in rglobals:
    tNB_CITY.append(rglobal['Value'][0])
    tNB_TRUCKS.append(float(rglobal['Value'][1]))
    tDISTANCE.append(float(rglobal['Value'][6]))
    tCoolRate.append(float(rglobal['Value'][8]))

# On récupère notre temps (Axe X)
tResolvedTime = []
for machine in machines:
    tResolvedTime.append(machine['Value'][0])

var = []
def predict(var):
    for v in range(0, len(var)):
       var[v] = var[v] * slope + intercept
    return var


print("===========GRAND [SOMETHING]===============")
# Remplacer X = à ce que vous voulez mesurer
# tNB_CITY
# tNB_TRUCKS
# tDISTANCE
X = tCoolRate
for i in X:
    var.append(i)
Y = tResolvedTime
slope, intercept, r_value, p_value, std_err = stats.linregress(var, Y)  # Regression linéaire
fitLine = predict(var)
axes = plt.axes()
axes.grid()
plt.scatter(X, Y)  # Nuage de point
plt.title('High Cool Number')
plt.xlabel('nb Cool')
plt.ylabel('Exec Time')
plt.plot(X, fitLine, c='r')
plt.show()
print("OK")