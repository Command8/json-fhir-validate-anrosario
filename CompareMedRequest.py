from email.headerregistry import Address
from msilib import sequence
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

print("////////////////////////////MEDREQUEST SNOWFLAKE(INPUT) JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'MedRequest_SampleData_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
MedRequestDataInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation    
print(MedRequestDataInput['CLAIM_NUMBER']) 
print(MedRequestDataInput['MEMBER_NUMBER'])
print(MedRequestDataInput['NDC_CODE'])
print(MedRequestDataInput['NDC_DESCRIPTION'])
print(MedRequestDataInput['HICN']) 
print(MedRequestDataInput['CLIENTNAME']) 
print(MedRequestDataInput['CLIENTID'])
print(MedRequestDataInput['DATE_OF_SERVICE']) 
print(MedRequestDataInput['QUANTITY'])
print(MedRequestDataInput['PAID_AMT'])
print(MedRequestDataInput['CENSEOID'])
print(MedRequestDataInput['FIRSTNAME'])
print(MedRequestDataInput['MIDDLENAME'])
print(MedRequestDataInput['LASTNAME'])

        
print("////////////////////////////MEDREQUEST Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load json input file into function
medreqfileoutput = ('CURES_fhir_MedicationRequest_converter.json')
#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'Transformedclmsac.json'
#Loading transformed JSON using function
medreqdataTransformer= getResourceFile(medreqfileoutput)

#RESOURCETYPE
#pulling key value RESOURCE_TYPE from medicationrequest.resourcetype fhir resource
print(medreqdataTransformer['resourceType'])

#pulling key value TEXT STATUS from medicationrequest.text.status fhir resource
print(medreqdataTransformer['text']['status'])

#pulling key value CONTAINED from medicationrequest.contained.resourceType fhir resource
print(medreqdataTransformer['contained'][0]['resourceType'])

#IDENTIFIER
#pulling key value IDENTIFIER from medicationrequest.identifier fhir resource
print(medreqdataTransformer['identifier'])


#STATUS
#pulling key value STATUS from medicationrequest.medicationReference.reference  fhir resource // R!  active | cancelled | draft | entered-in-error
print(medreqdataTransformer['status'])

#STATUS REASON  
#pulling key value STATUSREASON medicationrequest.statusreason fhir resource
print(medreqdataTransformer['statusReason'])

#CATAGORY
#pulling key value CATAGORY medicationrequest.catagory fhir resource
print(medreqdataTransformer['catagory'])

#INTENT
#pulling key value MEDICATION_REFERENCE from medicationrequest.intent fhir resource
print(medreqdataTransformer['intent']) 

#PRIORITY
#pulling key value PRIORITY from medicationrequest.priority fhir resource
print(medreqdataTransformer['priority']) 

#DONOTPERFORM
# pulling key value DONOTPERFORM  from medicationrequest.doNotPerform fhir resource
print(medreqdataTransformer['doNotPerform']) 

#REPORTEDBOOLEAN
#pulling key value reportedBoolean from medicationrequest.reportedBoolean fhir resource
print(medreqdataTransformer['reportedBoolean']) 

#REPORTEDREFERENCE
#pulling key value REPORTEDREFERENCE from medicationrequest.reportedReference fhir resource
print(medreqdataTransformer['reportedReference']) 

#PRACTIONERROLE
#pulling key value PRACTIONERROLE from medicationrequest.PractitionerRole fhir resource //R!  Desired processing ugency"
print(medreqdataTransformer['PractitionerRole'])

#MEDICATIONCODEABLECONCEPT
#pulling key value medicationCodeableConcept from medicationrequest.medicationCodeableConcept fhir resource //R!  Desired processing ugency"
print(medreqdataTransformer['medicationCodeableConcept'])

#MEDICATIONREFERENCE
#pulling key value medicationReference from medicationrequest.medicationReference fhir resource
print(medreqdataTransformer['medicationReference'])


#SUBJECT
#pulling key value subject CLAIM_TYPE from medicationrequest.subject value fhir resource
print(medreqdataTransformer['subject'])

#CARETEAM
#pulling key value status Provider_ID from medication request careTeam.sequence value fhir resource
print(medreqdataTransformer['careTeam'][0]['sequence'])
# pulling key value status Provider_ID from medication request careTeam.provider.reference value fhir resource
print(medreqdataTransformer['careTeam'][0]['provider'])  

#DIAGNOSIS
# pulling key value  from medication request diagnosis.sequence fhir resource
print(medreqdataTransformer['diagnosis'][0]['sequence'])
# pulling key DX_1 value from medication request diagnosis.sequence.diagnosisCodeableConcept.coding.code fhir resource
print(medreqdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding'][0]['code'])

# pulling key DX_2 value from medication request diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(medreqdataTransformer['diagnosis'][1]['diagnosisCodeableConcept']['coding'][0]['code'])

# pulling key DX_3 value from medication request diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(medreqdataTransformer['diagnosis'][2]['diagnosisCodeableConcept']['coding'][0]['code'])

#PROCEDURE
#pulling key value  "1"   from medication request procedure.sequence fhir resource
print(medreqdataTransformer['procedure'][0]['sequence']) 
#pulling key value  "primary" from medication request procedure.type.coding.code fhir resource
print(medreqdataTransformer['procedure'][0]['type'][0]['coding'][0]['code'])
#pulling key value ServiceFromDate from medication request.prodecure.date fhir resource

print(medreqdataTransformer['procedure'][0]['date'])
#pulling key value CPTCode_Primary from medication request fhir resource
print(medreqdataTransformer['procedure'][0]['procedureCodeableConcept']['coding'][0]['code'])

# pulling key value "2" from medication request procedure.sequence fhir resource
print(medreqdataTransformer['procedure'][1]['sequence']) 
#pulling key value ProcedureCode2 from medication request fhir resource
#pulling key value  "secondary" from medication request procedure.type.coding.code fhir resource
print(medreqdataTransformer['procedure'][1]['procedureCodeableConcept']['coding'][0]['code'])
#pulling key value ServiceFromDate from medication request.prodecure.date fhir resource
#print(medreqdataTransformer['procedure'][1]['date'])

#INSURANCE
# pulling key value "1" from medication request insurance.sequence fhir resource
print(medreqdataTransformer['insurance'][0]['sequence'])
# pulling key value "true" from medication request insurance.focal fhir resource
print(medreqdataTransformer['insurance'][0]['focal'])
# pulling key value  from medication request insurance.coverage.reference fhir resource
print(medreqdataTransformer['insurance'][0]['coverage']['reference']) 

#TOTAL
#pulling key vaalue BillAmount from medication requests total.value fhir resource
print(medreqdataTransformer['total']['value'])

