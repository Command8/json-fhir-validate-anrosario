from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
import json
import csv
from ntpath import join
from turtle import pd
from extract import json_extract

# Open csv to read data to make comparisons
with open('SnowflakePatient1.csv', 'r') as a:
    csv_reader = csv.DictReader(a)

    #Traversing through csv to identify the key values for validation
    for line in csv_reader:
        
        print(line['MEMBER_LAST_NAME']) 
        print(line['MEMBER_FIRST_NAME'])
        print(line['MEMBER_MIDDLE_NAME']) # bug
        print(line['MEMBER_COUNTY']) #bug
        print(line['CENSEOID']) 
        print(line['MEMBER_ADDRESS1'])
        print(line['MEMBER_ADDRESS2'])
        print(line['MEMBER_CITY'])
        print(line['MEMBER_DATE_OF_BIRTH'])
        print(line['ETHNICITY']) # bug
        
        #print(line['PCP_ID']) #not present in snowflake json
        print(line['PCP_FIRSTNAME'])
        print(line['PCP_LASTNAME'])
        #print(line['MEMBER_CURRENT_INSURER_ID'],line['MEDICAIDID'],line['CMSID']) - Not present in combined data spreadsheet 

        #Member Gender logic
        if (line['MEMBER_GENDER']) =='1':
                input_memgender ="male"
        elif (line['MEMBER_GENDER']) =='2':
                input_memgender ="female"
        elif (line['MEMBER_GENDER']) =='3':
                input_memgender ="unknown"
        else: input_memgender ="other"
        print(line['MEMBER_GENDER'])                  
        print (input_memgender)

# Open Transformed JSON and retrieve values
with open("TransformedPatient.json", "r") as d: 
    dataTransformer= json.load(d)

    # pulling key value MEMBER_LAST_NAME from patient profile
    #patient_memlname = json_extract(dataTransformer['name'], 'family')
    #print((patient_memlname[1][0]))
    print(dataTransformer['name'][0]['family'])      

    # pulling key value MEMBER_FIRST_NAME from patient profile
    #patient_memfname = json_extract(dataTransformer['name'], 'given')
    #print((patient_memfname[1][0][0]))
    print(dataTransformer['name'][0]['given'][0])    

    # pulling key value MEMBER_MIDDLE_NAME from patient profile
    #patient_memfname = json_extract(dataTransformer['name'], 'given')
    #print((patient_memfname[1][0][1]))
    print(dataTransformer['name'][0]['given'][1])     

    # pulling key value CENSEOID from patient profile
    #patient_censeoid = json_extract(dataTransformer['identifier'], 'value')
    #print(patient_censeoid[1][0])
    print(dataTransformer['identifier'][0]['value']) 

    # pulling key value MEMBER_ADDRESS1 from patient profile
    #patient_memaddress1 = json_extract(dataTransformer['address'], 'line')
    #print(patient_memaddress1[1][0].split(',')[0])
    print(dataTransformer['address'][0]['line'].split(',')[0]) 

    # pulling key value MEMBER_ADDRESS2 from patient profile
    #patient_memaddress2 = json_extract(dataTransformer['address'], 'line')
    #print(patient_memaddress2[1][0].split(',')[1].strip())
    print(dataTransformer['address'][0]['line'].split(',')[1].strip()) 

    # pulling key value CITY from patient profile
    #patient_memcity = json_extract(dataTransformer['address'], 'city')
    #print(patient_memcity[1][0])
    print(dataTransformer['address'][0]['city'])

    # pulling key value CITY from patient profile
    #patient_memcity = json_extract(dataTransformer['address'], 'state')
    #print(patient_memcity[1][0])
    print(dataTransformer['address'][0]['state'])

    # pulling key value DOB from patient profile
    #patient_memdob = json_extract(dataTransformer['birthDate'], 'birthDate')
    #print(patient_memdob[0])
    print(dataTransformer['birthDate'])

    # pulling key value ETHNICITY from patient profile
    #print(dataTransformer['ETHNICITY'])

    # pulling key value GENDER from patient profile
    print(dataTransformer['gender'])

    # pulling key value PCP_ID from patient profile
    print(dataTransformer['generalPractitioner'][0]['reference'].split('/')[1])

    # pulling key value PCP_firstname from patient profile
    print(dataTransformer['generalPractitioner'][0]['display'].split(' ')[0])

    # pulling key value PCP_lastname from patient profile
    print(dataTransformer['generalPractitioner'][0]['display'].split(' ')[1])    

d.close()