import pandas as pd

robject = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset1.xlsx", sheet_name='Object')

print("=================OBJETS & EFFECTIFS =======================")
print("Somme des objets : " + repr(max(robject['IDObjet'])))
# Proportion d'objets
print("Frequence")
effectifTotal = sum(robject["Effectif"])
valeurObjet = robject["Effectif"]
tabFreq = []
for i in robject["IDObjet"]:
    if valeurObjet[i - 1] != 0:
        print("Objet " + repr(i) + " = " + repr(valeurObjet[i-1] / effectifTotal) + "%")
        tabFreq.append(valeurObjet[i-1] / effectifTotal)

print("Frequence Cumulée Croissant")
y = 0
FreqCC = 0
for i in robject["IDObjet"]:
    if valeurObjet[i - 1] != 0:
        FreqCC += tabFreq[y]
        y = y+1
        print("Objet " + repr(i) + " = " + repr(FreqCC) + "%")


print("=====================Poids des objets=========================")
# Calculs sur les poids des objets
avgWeight = robject['Weight'].mean();  # moyenne poids
medianWeight = robject['Weight'].sort_values().median()  # mediane poids
Q1Weight = robject['Weight'].sort_values().quantile(0.25)
Q3Weight = robject['Weight'].sort_values().quantile(0.75)
modeWeight = robject['Weight'].mode()[0]
print("Somme des poids : " + repr(sum(robject['Weight'])))
print('Moyenne des poids: ' + repr(avgWeight))  # Equivaut au temps moyen pour une livraison
print('Q1 : ' + repr(Q1Weight))
print('Médiane : ' + repr(medianWeight))
print('Q3 : ' + repr(Q3Weight))
print('Most common value : ' + repr(modeWeight))
