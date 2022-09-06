import csv
from dataclasses import dataclass
from distutils import text_file


filename = 'HCS_CombinedData.csv'
dataDomain = 'Claims'


#Function to open csv file populate the list arrary
def csvValidate(filename, dataDomain):
        with open (filename, 'r') as (dataInventory):
            CombinedData = csv.DictReader(dataInventory)
            dataelements = [] # empty array
            # search for data point 
            for row in CombinedData:
                #print(row['Data.Domain'], row['Data.Data Element'])
                dataelements = (row['Data.Domain'],row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])
                #if value in row['Data.Domain']
                if dataDomain in row['Data.Domain']:
                    print(row['Data.Domain'], row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])
            return dataelements
        
       # dataInventory.close()

#Function to open text file populate the list arrary
def ValidateTxtfile(Template):
    TemplateVariables = []
    try:
        #Read the file and read individual lines
      with open (Template, 'r') as (liquidTemp):
           # TemplateVariables = (liquidTemp)
            RemplateVariablesments = [] # empty array
            for items in liquidTemp:
                print(items)  

    except FileExistsError:
        print ("Template cannot be found. ")
    return items

print('THIS IS THE HCS SHEET***************************************************')

csvValidate(filename, dataDomain)

print('THIS IS THE LIQUID TEMPLATE*********************************************')

templatedata = ValidateTxtfile('Output.txt')

