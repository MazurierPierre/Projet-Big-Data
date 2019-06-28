import pandas as pd

data = pd.read_csv("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\operations_enrichies.csv",parse_dates=[1,2])
# data.columns = ['identifiant_transaction', 'date_operation', 'date_valeur', 'libelle', 'debit', 'credit', 'solde']

# print(data)

effectifs = data["quart_mois"].value_counts()
# print(effectifs)
modalites = effectifs.index # l'index de effectifs contient les modalités

tab = pd.DataFrame(modalites, columns = ["quart_mois"]) # création du tableau à partir des modalités
tab["n"] = effectifs.values

tab["f"] = tab["n"] / len(data) # len(data) renvoie la taille de l'échantillon

tab = tab.sort_values("quart_mois") # tri des valeurs de la variable X (croissant)
tab["F"] = tab["f"].cumsum() # cumsum calcule la somme cumulée
print(tab["F"])

