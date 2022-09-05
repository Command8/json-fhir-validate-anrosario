import csv

with open ('HCS_CombinedData.csv', 'r') as (dataInventory):
    CombinedData = csv.DictReader(dataInventory)


    dataelements = []
    # .get(row['Data.Domain  '] ) + [row['Data.Data Element']]
    for row in CombinedData:
        #print(row['Data.Domain'], row['Data.Data Element'])
        dataelements = (row['Data.Domain'],row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])
        if 'Encounter' in dataelements:
            print(row['Data.Domain'], row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])

            
dataInventory.close()       