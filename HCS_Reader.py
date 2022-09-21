import csv
import re
from dataclasses import dataclass
from distutils import text_file


csvfilename = 'HCS_CombinedData.csv'
dataDomain = 'Claims'


#Function to open csv file populate the list arrary
def csvValidate(filename, fhir_resource):
    with open (csvfilename, 'r') as (dataInventory):
            CombinedData = csv.DictReader(dataInventory)
            dataelements = [] # empty array
            # search for data point 
            for row in CombinedData:
                #print(row['Data.Domain'], row['Data.Data Element'])
                dataelements = (row['Data.Domain'],row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])
                #if value in row['fhir_resource']
                if fhir_resource in row['FHIR Resource Name']:
                    print(dataelements[1],)# ':',  dataelements[3])
                    
        
       # dataInventory.close()

#Function to open text file populate the list array
def ValidateTxtfile(Template):
    templateVariables = []
    #try:
        #Read the file and read individual lines
    with open (Template, 'r') as (liquidTemp):
           # TemplateVariables = (liquidTemp)
            for items in liquidTemp:
                print (items)
    #except FileExistsError:
       # print ("Template cannot be found. ")
    #return items

#print('THIS IS THE HCS SHEET***************************************************')

#csvValidate(filename, dataDomain)

#print('THIS IS THE LIQUID TEMPLATE*********************************************')

#templatedata = ValidateTxtfile('Output.txt')