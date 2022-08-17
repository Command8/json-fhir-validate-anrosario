from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
import json
from ntpath import join
from turtle import pd

#import pathlib - Other library that can be used to reference directories

# Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Functions.fhir_functions import getResourceFile

#Using os, Import filepath of directory that file resides in
import os
dir_path = os.path.dirname((__file__))

print("////////////////////////////SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'PractitionerRole_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
dataPracRoleInput = getResourceFile(fileinput)

#Traversing through json to identify the key values for validation        
print(dataPracRoleInput['PROVIDER_ROLE_ID']) 
print(dataPracRoleInput['PROVIDER_ACTIVE'])
print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
print(dataPracRoleInput['PROVIDER_ACTIVE_END'])
print(dataPracRoleInput['PRACTITIONER']) 
print(dataPracRoleInput['PROVIDER_ORGANIZATION']) 
print(dataPracRoleInput['PROVIDER_ROLE_CODE'])
print(dataPracRoleInput['PROVIDER_ROLE_CODE_DESC']) 
print(dataPracRoleInput['PROVIDER_SPECIALITY_CODE'])
print(dataPracRoleInput['PROVIDER_SPECIALITY_DESC'])
print(dataPracRoleInput['PROVIDER_LOCATION'])
print(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'])
print(dataPracRoleInput['PROVIDER_PHONEPRIMARY'])
print(dataPracRoleInput['PROVIDER_PHONESECONDARY'])
print(dataPracRoleInput['PROVIDER_FAX'])
print(dataPracRoleInput['PROVIDER_CONTACT'])
print(dataPracRoleInput['PROVIDER_AVAILABLE_STARTTIME'])
print(dataPracRoleInput['PROVIDER_AVAILABLE_ENDTIME'])
print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'])
print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'])
print(dataPracRoleInput['AVAILABILIY_EXCEPTION'])
print(dataPracRoleInput['ENDPOINT_ACCESS'])
      
print("////////////////////////////Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileoutput = (dir_path + '/' +'TransformedPrac.json')

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'TransformedPrac.json'

#Loading transformed JSON using function
dataTransformer= getResourceFile(fileoutput)

# pulling key value PROVIDER_ID from patient profile
print(dataTransformer['identifier'][10]['value']) 

# pulling key value PROVIDER_NPI from patient profile
print(dataTransformer['identifier'][1]['value']) 

# pulling key value PROVIDER_PIN from patient profile
print(dataTransformer['identifier'][2]['value']) 