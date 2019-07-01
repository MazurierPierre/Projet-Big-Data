import pandas as pd

rglobal = pd.read_excel("C:\\Users\\emili\\Desktop\\project\\tests\\analyse\\Dataset1.xlsx", sheet_name='Params')


print("=================GLOBAL=======================")
# print(cities)

NB_CITY = rglobal['Value'][0]
NB_TRUCKS = rglobal['Value'][1]
NB_OBJECT = rglobal['Value'][2]
DENSITY = rglobal['Value'][3]
OBJECT_SIZE = rglobal['Value'][4]
RATIO_TRUCK = rglobal['Value'][5]
DISTANCE = rglobal['Value'][6]

nbTotal = NB_CITY + NB_TRUCKS + NB_OBJECT

print('% villes dans le programme : ' + repr((NB_CITY / nbTotal) * 100) + '%')
print('% camions dans le programme : ' + repr((NB_TRUCKS / nbTotal) * 100) + '%')
print('% objets dans le programme : ' + repr((NB_OBJECT / nbTotal) * 100) + '%')
