import xlsxwriter

'''
from Algorithmes import generateXLXS
generateXLXS.generatedataset()

numeroexec : Numéro d'exécution pour nom du fichier
# Structure attendue avec exemples :
listeCities = (
                [IDCity, OpenHours, ObjectNecessity, TimeDelivered],
                [1, "[7,22]", 1, 2],
                [2, "[7,22]", 5, 5],
                [3, "[7,22]", 6, 8],
                [4, "[7,22]", 4, 12],
               )

listeRoads = (
                [IDCitySource, IDCityTarget, Weight],
                [1, 3, 2],
                [1, 2, 3],
                [2, 1, 3],
                [2, 3, 2],
                [2, 4, 2],
            )

listeTrucks = (
                [IDTruck, Type],
                [1, 0],
                [2, 1],
                [3, 0],
                [4, 1],
                [5, 0],
            )

listeCargo = (
                [IDTruck, IdObject],
                [1, 1],
                [1, 4],
                [1, 2],
                [2, 5],
                [2, 2],
            )

listeParams = (
                [NomParamètre, Value, Description],
                ["NB_CITY", 3, "Number of cities in the graph."],
                ["NB_TRUCKS", 10, "Max number of trucks that can be deployed"],
                ["NB_OBJECT", 9, "Number of different objects that can be dispatched / needed by cities"],
                ["DENSITY", 1, "Number of connections between cities (0 = none, 1 = All cities are interconnected)."],
                ["OBJECT_SIZE", 2, "Maximum object size"],
                ["RATIO_TRUCK", 0.7, "Ratio of small trucks (Big trucks is 1- RATIO_TRUCK)."],
                ["DISTANCE", 5, "Max distance between cities"],
            )

listeMachine = (
                [Data, Value],
                ["ResolvedTime", 0.7],
                ["NbIterations", 1386],
            )


listeObject = (
                [IDObjet, Effectif, Weight],
                [1, 2, 2],
                [2, 4, 2],
                [3, 0, 1],
                [4, 2, 3],
                [5, 1, 2],
                [6, 0, 1],
            )
'''


def generatedataset(numeroexec, listeCities, listeRoads, listeTrucks, listeCargo, listeParams, listeMachine,
                    listeObject):
    workbook = xlsxwriter.Workbook('Dataset' + repr(numeroexec) + '.xlsx')
    bold = workbook.add_format({'bold': True})
    # Ligne et colonne de départ pour l'écriture

    print("Cities Generation....")
    row = 1
    col = 0

    worksheet = workbook.add_worksheet("Cities")
    # Write some data headers.
    worksheet.write('A1', 'IDCity', bold)
    worksheet.write('B1', 'OpenHours', bold)
    worksheet.write('C1', 'ObjectNecessity', bold)
    worksheet.write('D1', 'TimeDelivered', bold)

    # Iterate over the data and write it out row by row.
    for item, horaire, robject, timedelivered in listeCities:
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, horaire)
        worksheet.write(row, col + 2, robject)
        worksheet.write(row, col + 3, timedelivered)
        row += 1

    print("Roads generation...")
    row = 1
    col = 0
    worksheet2 = workbook.add_worksheet("Roads")
    # Write some data headers.
    worksheet2.write('A1', 'IDCitySource', bold)
    worksheet2.write('B1', 'IDCityTarget', bold)
    worksheet2.write('C1', 'Weight', bold)

    # Iterate over the data and write it out row by row.
    for iDCitySource, iDCityTarget, weight in listeRoads:
        worksheet2.write(row, col, iDCitySource)
        worksheet2.write(row, col + 1, iDCityTarget)
        worksheet2.write(row, col + 2, weight)
        row += 1

    print("Trucks generation...")
    row = 1
    col = 0

    worksheet3 = workbook.add_worksheet("Truck")
    # Write some data headers.
    worksheet3.write('A1', 'IDTruck', bold)
    worksheet3.write('B1', 'Type', bold)

    # Iterate over the data and write it out row by row.
    for iDTruck, vtype in listeTrucks:
        worksheet3.write(row, col, iDTruck)
        worksheet3.write(row, col + 1, vtype)
        row += 1

    print("Cargo generation...")
    row = 1
    col = 0

    worksheet4 = workbook.add_worksheet("Cargo")
    # Write some data headers.
    worksheet4.write('A1', 'IDTruck', bold)
    worksheet4.write('B1', 'IdObject', bold)

    for iDTruck, vobject in listeCargo:
        worksheet4.write(row, col, iDTruck)
        worksheet4.write(row, col + 1, vobject)
        row += 1

    print("Params generation...")
    row = 1
    col = 0

    worksheet5 = workbook.add_worksheet("Params")
    # Write some data headers.
    worksheet5.write('A1', 'NomParamètre', bold)
    worksheet5.write('B1', 'Value', bold)
    worksheet5.write('C1', 'Description', bold)

    # Iterate over the data and write it out row by row.
    for paramName, value, desc in listeParams:
        worksheet5.write(row, col, paramName)
        worksheet5.write(row, col + 1, value)
        worksheet5.write(row, col + 2, desc)
        row += 1

    print("Machine generation...")
    row = 1
    col = 0

    worksheet6 = workbook.add_worksheet("Machine")
    # Write some data headers.
    worksheet6.write('A1', 'Data', bold)
    worksheet6.write('B1', 'Value', bold)

    # Iterate over the data and write it out row by row.
    for vdata, value in listeMachine:
        worksheet6.write(row, col, vdata)
        worksheet6.write(row, col + 1, value)
        row += 1

    print("Object generation...")
    row = 1
    col = 0

    worksheet7 = workbook.add_worksheet("Object")
    # Write some data headers.
    worksheet7.write('A1', 'IDObjet', bold)
    worksheet7.write('B1', 'Effectif', bold)
    worksheet7.write('C1', 'Weight', bold)

    # Iterate over the data and write it out row by row.
    for iDObject, effectif, weight in listeObject:
        worksheet7.write(row, col, iDObject)
        worksheet7.write(row, col + 1, effectif)
        worksheet7.write(row, col + 2, weight)
        row += 1

    workbook.close()
