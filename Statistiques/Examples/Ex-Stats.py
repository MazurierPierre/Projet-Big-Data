import pandas as pd

import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\operations_enrichies.csv", parse_dates=[0])


print('moyenne : ' + repr(data['montant'].mean()))
print('médiane : ' + repr(data['montant'].median()))
print('mode : ' + repr(data['montant'].mode()))
print('variance: ' + repr(data['montant'].var()))
print('standard deviation = ecart type: ' + repr(data['montant'].std()))

for cat in data["categ"].unique():
    subset = data[data.categ == cat]
    print("-"*20)
    print(cat)
    print("moy:\n",subset['montant'].mean())
    print("med:\n",subset['montant'].median())
    print("mod:\n",subset['montant'].mode())
    print("var:\n",subset['montant'].var(ddof=0))  # ddof= 0 == degrés de liberté
    print("ect:\n",subset['montant'].std(ddof=0))
    subset["montant"].hist()
    plt.show()
    subset.boxplot(column="montant", vert=False) # Boîte à moustache
    plt.show()