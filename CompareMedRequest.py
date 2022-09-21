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
#pulling key value MEDICATIONCODEABLECONCEPT from medicationrequest.medicationCodeableConcept fhir resource //R!  Desired processing ugency"
print(medreqdataTransformer['medicationCodeableConcept'])

#MEDICATIONREFERENCE
#pulling key value MEDICATIONREFERENCE from medicationrequest.medicationReference fhir resource
print(medreqdataTransformer['medicationReference'])


#SUBJECT
#pulling key value SUBJECT from medicationrequest.subject value fhir resource
print(medreqdataTransformer['subject'])

#ENCOUNTER
#pulling key value ENCOUNTER from medicationrequest.encounter value fhir resource
print(medreqdataTransformer['encounter'])

#SUPPORTINGINFORMATION
# pulling key value SUPPORTINGINFORMATION from medication request.supportingInformation value fhir resource
print(medreqdataTransformer['supportingInformation'])  

#AUTHOREDON
# pulling key value AUTHOREDON from medicationrequest.authoredOn fhir resource
print(medreqdataTransformer['authoredOn'])

#REQUESTER
# pulling key REQUESTER value from medication request.requester fhir resource
print(medreqdataTransformer['requester'])

#PERFORMER
#pulling key PERFORMER value from medication request.performer fhir resource
print(medreqdataTransformer['performer'])

#PRACTITIONERROLE
#pulling key PRACTITIONERROLE value from medication request.PractitionerRole fhir resource
print(medreqdataTransformer['PractitionerRole'])

#PERFORMERTYPE
#pulling key PERFORMERTYPE value from medicationrequest.performerType fhir resource
print(medreqdataTransformer['performerType']) 

#RECORDER
#pulling key RECORDER value from medicationrequest.recorder fhir resource
print(medreqdataTransformer['recorder'])

#REASONCODE
#pulling key REASONCODE value from medicationrequest.reasonCode fhir resource
print(medreqdataTransformer['reasonCode'])

#REASONREFERENCE
#pulling key REASONREFERENCE value from medicationrequest.reasonReference fhir resource
print(medreqdataTransformer['reasonReference'])

#INSTANTIATESCANONICAL
# pulling key INSTANTIATESCANONICAL value from medication request.instantiatesCanonical fhir resource
print(medreqdataTransformer['instantiatesCanonical']) 

#INSTANTIATESURI
#pulling key INSTANTIATESURI value from medication request.instantiatesUri fhir resource
print(medreqdataTransformer['instantiatesUri'])

#BASEDON
#pulling key BASEDON value from medicationrequest.basedOn fhir resource
print(medreqdataTransformer['basedOn'])

#GROUPIDENTIFIER
#pulling key GROUPIDENTIFIER value from medicationrequest.groupIdentifier fhir resource
print(medreqdataTransformer['groupIdentifier'])

#COURSEOFTHERAPYTYPE
#pulling key COURSEOFTHERAPYTYPE value from medication request.courseOfTherapyType fhir resource
print(medreqdataTransformer['courseOfTherapyType'])

#INSURANCE
#pulling key INSURANCE value from medication request.insurance fhir resource
print(medreqdataTransformer['insurance']) 

#NOTE
#pulling key NOTE value  from medicationrequests.note fhir resource
print(medreqdataTransformer['note'])

#DOSAGEINSTRUCTION
#pulling key DOSAGEINSTRUCTION value from medicationrequests.dosageInstruction fhir resource
print(medreqdataTransformer['dosageInstruction'])

#DISPENSEREQUEST
#pulling key value DISPENSEREQUEST from medication requests.dispenseRequest fhir resource
print(medreqdataTransformer['dispenseRequest'])

#DISPENSEREQUEST.INITIALFILL
#pulling key INITIALFILL value  from medication requests.dispenseRequest.initialFill fhir resource
print(medreqdataTransformer['dispenseRequest']['initialFill'])

#DISPENSEREQUEST.INITIALFILL.QUANTITY
#pulling key QUANTITY value  from medication requests.dispenseRequest.initialFill.quantity fhir resource
print(medreqdataTransformer['dispenseRequest']['initialFill']['quantity'])

#DISPENSEREQUEST.INITIALFILL.DURATION
#pulling key DURATION value  from medication requests.dispenseRequest.initialFill.duration fhir resource
print(medreqdataTransformer['dispenseRequest']['initialFill']['duration'])

#DISPENSEREQUEST.DISPENSEINTERVAL
#pulling key dispenseInterval value  from medication requests.dispenseRequest.dispenseInterval fhir resource
print(medreqdataTransformer['dispenseRequest']['dispenseInterval'])

#DISPENSEREQUEST.VALIDITYPERIOD
#pulling key VALIDITYPERIOD value  from medication requests.dispenseRequest.validityPeriod fhir resource
print(medreqdataTransformer['dispenseRequest']['validityPeriod'])

#DISPENSEREQUEST.NUMBEROFREPEATSALLOWED
#pulling key NUMBEROFREPEATSALLOWED value  from medication requests.dispenseRequest.numberOfRepeatsAllowed fhir resource
print(medreqdataTransformer['dispenseRequest']['numberOfRepeatsAllowed'])

#DISPENSEREQUEST.QUANTITY
#pulling key QUANTITY value  from medication requests.dispenseRequest.quantity fhir resource
print(medreqdataTransformer['dispenseRequest']['quantity'])

#DISPENSEREQUEST.EXPECTEDSUPPLYDURATION
#pulling key EXPECTEDSUPPLYDURATION value  from medication requests.dispenseRequest.expectedSupplyDuration fhir resource
print(medreqdataTransformer['dispenseRequest']['expectedSupplyDuration'])

#DISPENSEREQUEST.PERFORMER
#pulling key PERFORMER value  from medication requests.dispenseRequest.performer fhir resource
print(medreqdataTransformer['dispenseRequest']['performer'])

#SUBSTITUTION.ALLOWEDBOOLEANALLOWEDBOOLEAN
#pulling key ALLOWEDBOOLEAN value  from medicationrequests.substitution.allowedBoolean fhir resource
print(medreqdataTransformer['substitution']['allowedBoolean'])

#SUBSTITUTION.ALLOWEDCODEABLECONCEPT
#pulling key ALLOWEDCODEABLECONCEPT value  from medicationrequests.substitution.allowedCodeableConcept fhir resource
print(medreqdataTransformer['substitution']['allowedCodeableConcept'])

#SUBSTITUTION.REASON
#pulling key REASON value  from medicationrequests.substitution.reason fhir resource
print(medreqdataTransformer['substitution']['reason'])

#PRIORPRESCRIPTION
#pulling key PRIORPRESCRIPTION value from medicationrequests.priorPrescription fhir resource
print(medreqdataTransformer['priorPrescription'])

#DETECTEDISSUE
#pulling key DETECTEDISSUE value from medicationrequests.detectedIssue fhir resource
print(medreqdataTransformer['detectedIssue'])

#EVENTHISTORY
#pulling key EVENTHISTORY value  from medicationrequests.eventHistory fhir resource
print(medreqdataTransformer['eventHistory'])

