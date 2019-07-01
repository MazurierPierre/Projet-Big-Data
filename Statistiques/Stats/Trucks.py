import pandas as pd
import matplotlib.pyplot as plt

trucks = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset1.xlsx", sheet_name='Truck')

print("=================TRUCKS=======================")
nbTrucks = (max(trucks['IDTruck']))
nbHTrucks = 0
nbLTrucks = 0
for i in trucks['Type']:
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