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
#Access parent directory and create path to load json input file into function
prfileoutput = ('TransformedPracRole.json')

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'TransformedPrac.json'

#Loading transformed JSON using function
prdataTransformer= getResourceFile(prfileoutput)

# pulling key value PROVIDER_ROLE_ID from practitioner role fhir resource
print(prdataTransformer['identifier'][0]['value']) 

# pulling key value PROVIDER_ACTIVE from practitioner role fhir resource
print(prdataTransformer['active']) 

# pulling key value PROVIDER_ACTIVE_START  from practitioner role fhir resource
print(prdataTransformer['period'][0]['start']) 

# pulling key value PROVIDER_ACTIVE_END  from practitioner role fhir resource
print(prdataTransformer['period'][0]['start']) 

# pulling key value Practitioner/id  from practitioner role fhir resource
print(prdataTransformer['practitioner'][0]['reference']) 

# pulling key value PRACTITIONER from practitioner role fhir resource
print(prdataTransformer['practitioner'][0]['display'])

# pulling key value PROVIDER_ORGANIZATION from practitioner role fhir resource
print(prdataTransformer['organization']['reference'])

# pulling key value PROVIDER_ORGANIZATION from practitioner role fhir resource
print(prdataTransformer['organization']['display'])

# pulling key code.coding value PROVIDER_ROLE_CODE from practitioner role fhir resource
print(prdataTransformer['code'][0]['coding'][0]['code'])

# pulling key code.coding value PROVIDER_ROLE_CODE_DESC from practitioner role fhir resource
print(prdataTransformer['code'][0]['text'])

# pulling key value PROVIDER_SPECIALITY_CODE from practitioner role fhir resource
print(prdataTransformer['specialty'][0]['coding'][0]['code'])

# pulling key value PROVIDER_SPECIALITY_DESC from practitioner role fhir resource
print(prdataTransformer['specialty'][0]['text'])

#pulling key value PROVIDER_LOCATION from practitioner role fhir resource
print(prdataTransformer['location']['reference'])

#pulling key value PROVIDER_LOCATION from practitioner role fhir resource
print(prdataTransformer['location']['display'])

#pulling key value PROVIDER_HEALTHCARE_SERVICE from practitioner role fhir resource
print(prdataTransformer['healthcareService']['reference'])

#pulling key value PROVIDER_HEALTHCARE_SERVICE from practitioner role fhir resource
print(prdataTransformer['healthcareService']['display'])

#pulling key value PROVIDER_PHONEPRIMARY from practitioner role fhir resource
print(prdataTransformer['telecom'][0]['value'])

#pulling key value PROVIDER_PHONESECONDARY from practitioner role fhir resource
print(prdataTransformer['telecom'][1]['value'])

#pulling key value PROVIDER_CONTACT from practitioner role fhir resource
print(prdataTransformer['telecom'][2]['value'])

#pulling key value PROVIDER_FAX from practitioner role fhir resource
print(prdataTransformer['telecom'][3]['value'])

#pulling key value PROVIDER_AVAILABLE_STARTTIME from practitioner role fhir resource
print(prdataTransformer['availableTime'][0]['availableStartTime'])

#pulling key value PROVIDER_AVAILABLE_ENDTIME from practitioner role fhir resource
print(prdataTransformer['availableTime'][0]['availableEndTime'])

#pulling key value PROVIDER_SERVICE_NOT_AVAILABLE_FROM from practitioner role fhir resource
print(prdataTransformer['notAvailable'][0]['during']['start'])

#pulling key value PROVIDER_SERVICE_NOT_AVAILABLE_TO from practitioner role fhir resource
print(prdataTransformer['notAvailable'][0]['during']['end'])

# pulling key value AVAILABILIY_EXCEPTION from practitioner role fhir resource
print(prdataTransformer['availabilityExceptions']) 

# pulling key value ENDPOINT_ACCESS from practitioner role fhir resource
print(prdataTransformer['endpoint'][0]['reference']) 

# pulling key value ENDPOINT_ACCESS from practitioner role fhir resource
print(prdataTransformer['endpoint'][0]['display']) 
