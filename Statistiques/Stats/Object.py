import pandas as pd

robject = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset.xlsx", sheet_name='Object')

print("=================OBJETS=======================")

effectifs = robject["Objet"].value_counts().sort_values()
modalites = effectifs.index # l'index de effectifs contient les modalités
print("Effectifs")
print(effectifs)

print("Fréquence")
tab = pd.DataFrame(modalites, columns = ["Objet"]) # création du tableau à partir des modalités
tab["n"] = effectifs.values
tab["f"] = tab["n"] / len(robject) # len(data) renvoie la taille de l'échantillon
for i in tab["f"]:
    print("Fréquence de " + repr(i[0]) + " à " + repr(i[1]))


print("Fréquence cumulée croissant")
tab = tab.sort_values("Objet") # tri des valeurs de la variable X (croissant)
tab["F"] = tab["f"].cumsum() # cumsum calcule la somme cumulée
print(tab["F"])