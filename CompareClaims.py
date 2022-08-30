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

print("////////////////////////////SNOWFLAKE(INPUT) JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'ClaimsSampleData.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
ClaimsDataInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation    
print(ClaimsDataInput['Provider_ID']) 
print(ClaimsDataInput['RenderingProviderID'])
print(ClaimsDataInput['RenderingProviderNPI'])
print(ClaimsDataInput['AdmissionDate'])
print(ClaimsDataInput['AdmitDiag']) 
print(ClaimsDataInput['AdmitSource']) 
print(ClaimsDataInput['AdmitType'])
print(ClaimsDataInput['BillAmount']) 
print(ClaimsDataInput['BillingProvideID'])
print(ClaimsDataInput['BillingProviderNPI'])
print(ClaimsDataInput['BillType'])
print(ClaimsDataInput['CarePlan'])
print(ClaimsDataInput['CenseoID'])
print(ClaimsDataInput['ClaimEntryDate'])
print(ClaimsDataInput['ClaimLineNumber'])
print(ClaimsDataInput['ClaimNumber'])
print(ClaimsDataInput['ClaimPaymentStatus'])
print(ClaimsDataInput['DiagnosisCode'])
print(ClaimsDataInput['DiagnosisCodeDecimal'])
print(ClaimsDataInput['DiagnosisFilter'])
print(ClaimsDataInput['DiagnosisFullDescription'])
print(ClaimsDataInput['DiagnosisLongDescription'])
print(ClaimsDataInput['DiagnosisShortDescription'])
print(ClaimsDataInput['DiagnosisIndicator'])
print(ClaimsDataInput['DiagnosisVersionCode'])
print(ClaimsDataInput['DiagnosisVersionDescription'])
print(ClaimsDataInput['DimDiagnosisKey'])
print(ClaimsDataInput['DischargeDate'])
print(ClaimsDataInput['DRG'])
print(ClaimsDataInput['DX_1'])
print(ClaimsDataInput['DX_2'])
print(ClaimsDataInput['DX_3'])
print(ClaimsDataInput['EvaluationKey'])
print(ClaimsDataInput['Exception'])
print(ClaimsDataInput['HasInvalidResult'])
print(ClaimsDataInput['HICN'])
print(ClaimsDataInput['ICDVersion'])
print(ClaimsDataInput['IsBillable'])
print(ClaimsDataInput['lab_results'])
print(ClaimsDataInput['LabResultsDateReceived'])
print(ClaimsDataInput['LeftSeverity'])
print(ClaimsDataInput['Medicare_Adjusted'])
print(ClaimsDataInput['Medicare_Unadjusted'])
print(ClaimsDataInput['Member_Number'])
print(ClaimsDataInput['Modifier'])
print(ClaimsDataInput['NPI'])
print(ClaimsDataInput['ODSAnswerID'])
print(ClaimsDataInput['ODSDiagnosisID'])
print(ClaimsDataInput['ODSEvaluationID'])
print(ClaimsDataInput['ODSEvaluationResponseID'])
print(ClaimsDataInput['ODSQuestionID'])
print(ClaimsDataInput['PaidAmount'])
print(ClaimsDataInput['PaidDate'])
print(ClaimsDataInput['PatientPayPortion'])
print(ClaimsDataInput['PlaceOfService'])
print(ClaimsDataInput['ProcedureCode /CPTCode_Primary'])
print(ClaimsDataInput['ProcedureCode2'])
print(ClaimsDataInput['ProductKey'])
print(ClaimsDataInput['RenderingProviderSpecialty'])
print(ClaimsDataInput['ResponseValue'])
print(ClaimsDataInput['RevenueCode'])
print(ClaimsDataInput['RightSeverity'])
print(ClaimsDataInput['ServiceCategory'])
print(ClaimsDataInput['ServiceFromDate /Date_of_Service'])
print(ClaimsDataInput['ServiceThruDate'])
print(ClaimsDataInput['Specialty_Code'])
print(ClaimsDataInput['Specialty_Name'])
        
print("////////////////////////////Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load json input file into function
clmsfileoutput = ('cures-fhir-sig-claims-converter.json')
#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'Transformedclmsac.json'
#Loading transformed JSON using function
clmsdataTransformer= getResourceFile(clmsfileoutput)

#RESOURCETYPE
# pulling key value RESOURCE_TYPE from claim fhir resource
print(clmsdataTransformer['resourcesType'])

#IDENTIFIER
# pulling key value CLAIM_NUMBER from claim identifier.use fhir resource
print(clmsdataTransformer['identifier'][0]['use'])
# pulling key value CLAIM_NUMBER from claim identifier.value fhir resource
print(clmsdataTransformer['identifier'][0]['value'])

#STATUS
#pulling key value ClaimPaymentStatus from claim.status  fhir resource // R!  active | cancelled | draft | entered-in-error
print(clmsdataTransformer['status'])

#PATIENT
# pulling key value CENSEO_ID identifer.use Claim patient.reference fhir resource
print(clmsdataTransformer['patient'][0]['reference'])

#BILLABLEPERIOD
# pulling key value BILLABLE_PERIOD CLAIM from claim.billablePeriod.start fhir resource
#ServiceFromDate_Date_of_Service
print(clmsdataTransformer['billablePeriod'][0]['start']) 
# pulling key value BILLABLE_PERIOD CLAIM ServiceThruDate from claim.billablePeriod.end fhir resource
print(clmsdataTransformer['billablePeriod'][0]['end']) 

#CREATED
# pulling key value status ClaimEntryDate from claim fhir resource
print(clmsdataTransformer['created']) 

#ENTERER
# pulling key value status Provider_ID from claim enterer.reference fhir resource
print(clmsdataTransformer['enterer']) 

#PROVIDER
# pulling key value status Provider_ID from claim provider.reference fhir resource
print(clmsdataTransformer['provider']) 

#PRIORITY
# pulling key value RenderingProviderNPI from claim priority.coding.code fhir resource //R!  Desired processing ugency"
print(clmsdataTransformer['priority'][0]['coding'][0]['code'])

#PRESCRIPTION
# pulling key value prescription.reference from claim prescription.reference fhir resource //R!  Desired processing ugency"
print(clmsdataTransformer['prescription'][0]['reference'])

#FACILITY
#pulling key PlaceOfServicevalue CLAIM_TYPE from claim facility.identifier.value fhir resource
print(clmsdataTransformer['facility'][0]['identifier'][0]['value'])

#CARETEAM
#pulling key value status Provider_ID from claim careTeam.sequence value fhir resource
print(clmsdataTransformer['careTeam'][0]['sequence'])
# pulling key value status Provider_ID from claim careTeam.provider.reference value fhir resource
print(clmsdataTransformer['careTeam'][0]['provider'])  

#DIAGNOSIS
# pulling key value  from claim diagnosis.sequence fhir resource
print(clmsdataTransformer['diagnosis'][0]['sequence'])
# pulling key DX_1 value from claim diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code'])
print(clmsdataTransformer['diagnosis'][0]['sequence'])
# pulling key DX_2 value from claim diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code'])
print(clmsdataTransformer['diagnosis'][0]['sequence'])
# pulling key DX_3 value from claim diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code'])

#PROCEDURE
#pulling key value  "1"   from claim procedure.sequence fhir resource
print(clmsdataTransformer['prodecure'][0]['sequence']) 
#pulling key value  "primary" from claim procedure.type.coding.code fhir resource
print(clmsdataTransformer['procedure'][0]['type']['coding']['code'])
#pulling key value ServiceFromDate from claim.prodecure.date fhir resource
print(clmsdataTransformer['procedure'][0]['date'])
#pulling key value CPTCode_Primary from claim fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding']['code'])

# pulling key value "2" from claim procedure.sequence fhir resource
print(clmsdataTransformer['prodecure'][0]['sequence']) 
#pulling key value  "secondary" from claim procedure.type.coding.code fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding']['code'])
#pulling key value ServiceFromDate from claim.prodecure.date fhir resource
print(clmsdataTransformer['procedure'][0]['date'])
#pulling key value ProcedureCode2 from claim fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding']['code'])

#INSURANCE
# pulling key value "1" from claim insurance.sequence fhir resource
print(clmsdataTransformer['insurance'][0]['sequence'])
# pulling key value "true" from claim insurance.focal fhir resource
print(clmsdataTransformer['insurance'][0]['focal'])
# pulling key value  from claim insurance.coverage.reference fhir resource
print(clmsdataTransformer['insurance'][0]['coverage']['reference']) 

#TOTAL
#pulling key vaalue BillAmount from claims total.value fhir resource
print(clmsdataTransformer['total'][0]['value'])

