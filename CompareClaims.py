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

print("////////////////////////////SNOWFLAKE(INPUT) JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'Claims_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
dataClaimsInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation    
print(dataClaimsInput['']) 
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput['']) 
print(dataClaimsInput['']) 
print(dataClaimsInput[''])
print(dataClaimsInput['']) 
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
print(dataClaimsInput[''])
        
print("////////////////////////////Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load json input file into function
clmsfileoutput = ('TransformedClaims.json')

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'Transformedclmsac.json'

#Loading transformed JSON using function
clmsdataTransformer= getResourceFile(clmsfileoutput)

# pulling key value RESOURCE_TYPE from claims fhir resource
print(clmsdataTransformer['resourcesType'])

# pulling key value CLAIMS_ID from claims fhir resource
#print(clmsdataTransformer['id'])

# pulling key value CLAIMS_TEXT from claims fhir resource
#print(clmsdataTransformer['text'][0]['status'])

# pulling key value identifer.use CLAIMS_IDENTIFIER from claims fhir resource
print(clmsdataTransformer['identifier'][0]['use'])

# pulling key value identifer.system CLAIMS_IDENTIFIER from claims fhir resource
#print(clmsdataTransformer['identifier'][0]['system']) 

# pulling key value identifier.value CLAIMS_IDENTIFIER from claims fhir resource
print(clmsdataTransformer['identifier'][0]['value']) 

# pulling key value status CLAIMS_STATUS from claims fhir resource
print(clmsdataTransformer['status']) 

# pulling key type.coding.system value CLAIMS_TYPE from claims fhir resource
print(clmsdataTransformer['type'][0]['coding'][0]['system'])

# pulling key type.coding.code value CLAIMS_TYPE from claims fhir resource
print(clmsdataTransformer['type'][0]['coding'][0]['code'])

# pulling key value status CLAIMS_USE from claims fhir resource
print(clmsdataTransformer['use']) 

# pulling key patient.reference value CLAIMS_PATIENT from claims fhir resource
print(clmsdataTransformer['patient'][0]['reference'])

#pulling key billablePeriod.start created value status CLAIMS_BILLABLE_START from claims fhir resource
print(clmsdataTransformer['billablePeriod'][0]['start']) 

#pulling key billablePeriod.end created value status CLAIMS_BILLABLE_START from claims fhir resource
print(clmsdataTransformer['billablePeriod'][0]['end'])

#pulling key created value status CLAIMS_CREATED from claims fhir resource
print(clmsdataTransformer['created'])

#pulling key entered value status CLAIMS_ENTERED from claims fhir resource
print(clmsdataTransformer['entered'][0]['reference'])

# pulling key value provider.reference PROVIDER_REFERENCE from claims fhir resource
print(clmsdataTransformer['provider'][0]['reference'])

# pulling key value priority.coding.code PRIORITY_CODE from claims fhir resource
print(clmsdataTransformer['priority'][0]['coding']['code']) 


# pulling key prescription.reference value CLAIMS_PRESCRIPTION  from claims fhir resource
print(clmsdataTransformer['prescription'][0]['reference']) 

# pulling key payee.type.coding.code  value CLAIMS_PAYEE  from claims fhir resource
print(clmsdataTransformer['payee'][0]['type'][0]['coding']['code']) 

# pulling key payee.type.coding.display value CLAIMS_PAYEE  from claims fhir resource
print(clmsdataTransformer['payee'][0]['type'][0]['coding']['display']) 

# pulling key insurer.reference value CLAIMS INSURER_ORGANIZATION  from claims fhir resource
print(clmsdataTransformer['insurer'][0]['reference']) 

# pulling key facility.identifier.value value CLAIMS_PAYEE from claims fhir resource
print(clmsdataTransformer['facility'][0]['identifier']['value']['display'])

# pulling key careTeam.sequence value CLAIMS_CARETEAM from claims fhir resource
print(clmsdataTransformer['careTeam'][0]['sequence'])

# pulling key careTeam.provider.reference value CLAIMS_CARETEAM from claims fhir resource
print(clmsdataTransformer['careTeam'][0]['provider']['reference'])

# pulling key diagnosis.sequence.diagnosisCodeableConcept.coding.code value CLAIMS_DIAGNOSIS1 from claims fhir resource
print(clmsdataTransformer['diagnosis'][0]['sequence']['diagnosisCodeableConcept']['coding']['code'])

# pulling key diagnosis.sequence.diagnosisCodeableConcept.coding.code value CLAIMS_DIAGNOSIS2 from claims fhir resource
print(clmsdataTransformer['diagnosis'][0]['sequence']['diagnosisCodeableConcept']['coding']['code'])

# pulling key diagnosis.sequence.diagnosisCodeableConcept.coding.code value CLAIMS_DIAGNOSIS3 from claims fhir resource
print(clmsdataTransformer['diagnosis'][0]['sequence']['diagnosisCodeableConcept']['coding']['code'])

# pulling key procedure.sequence value CLAIMS_PROCEDURE1 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['sequence'])

#  pulling key procedure.sequence.type.coding.code value CLAIMS_PROCEDURE1 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['type'][0]['coding']['code'])

#  pulling key procedure.date value CLAIMS_PROCEDURE1 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['date'])

#  pulling key procedure.procedureCodeableConcept.coding.code value CLAIMS_PROCEDURE2 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept'][0]['coding']['code'])

# pulling key procedure.sequence value CLAIMS_PROCEDURE1 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['sequence'])

#  pulling key procedure.sequence.type.coding.code value CLAIMS_PROCEDURE2 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['type'][0]['coding']['code'])

#  pulling key procedure.date value CLAIMS_PROCEDURE2 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['date'])

#  pulling key procedure.procedureCodeableConcept.coding.code value CLAIMS_PROCEDURE2 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept'][0]['coding']['code'])

# pulling key procedure.sequence value CLAIMS_PROCEDURE1 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['sequence'])

#  pulling key procedure.sequence.type.coding.code value CLAIMS_PROCEDURE3 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['type'][0]['coding']['code'])

#  pulling key procedure.date value CLAIMS_PROCEDURE3 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['date'])

#  pulling key procedure.procedureCodeableConcept.coding.code value CLAIMS_PROCEDURE3 from claims fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept'][0]['coding']['code'])

# pulling key insurance.sequence CLAIMS_INSURANCE from claims fhir resource
print(clmsdataTransformer['insurance'][0]['sequence'])

# pulling key insurance.focal value CLAIMS_INSURANCE from claims fhir resource
print(clmsdataTransformer['insurance'][0]['focal'])

# pulling key insurance.coverage.reference value CLAIMS_INSURANCE from claims fhir resource
print(clmsdataTransformer['insurance'][0]['coverage']['reference'])


# pulling key item.sequence value CLAIMS_ITEMS from claims fhir resource
#print(clmsdataTransformer['item'][0]['sequence'])

# pulling key item.careTeamSequence value CLAIMS_ITEMS from claims fhir resource
#print(clmsdataTransformer['item'][0]['careTeamSequence'][0])

# pulling key item.productOrService.coding.code value CLAIMS_ITEMS from claims fhir resource
#print(clmsdataTransformer['item'][0]['productOrService'][0]['coding']['code'])

# pulling key item.servicedDate  value CLAIMS_ITEMS from claims fhir resource
print(clmsdataTransformer['item'][0]['servicedDate'])

# pulling key item.unitPrice.value value CLAIMS_ITEMS from claims fhir resource
#print(clmsdataTransformer['item'][0]['unitPrice'][0]['value']['code'])

# pulling key item.unitPrice.currency value CLAIMS_ITEMS from claims fhir resource
#print(clmsdataTransformer['item'][0]['unitPrice'][0]['currency'])

#pulling key net.value value PROVIDER_LOCATION from claims fhir resource
#print(clmsdataTransformer['net'][0]['value'])

#pulling key net.currency value PROVIDER_LOCATION from claims fhir resource
#print(clmsdataTransformer['net'][0]['currency'])

#pulling key total.value value CLAIMS_TOTAL from claims fhir resource
print(clmsdataTransformer['total'][0]['value'])

