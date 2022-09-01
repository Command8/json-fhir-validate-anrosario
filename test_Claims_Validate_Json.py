from pickle import FALSE
import unittest
import json
from CompareClaims import clmsdataTransformer,ClaimsDataInput


class TestTransform (unittest.TestCase):  
    
 #Validation of Claims - ClaimNumber value between input json and transformed Claims JSON    
    def test_claimclaimnum(self):
        if ClaimsDataInput['ClaimNumber'] == clmsdataTransformer['identifier'][0]['value']:
            print(ClaimsDataInput['ClaimNumber'])
        self.assertEqual(ClaimsDataInput['ClaimNumber'],clmsdataTransformer['identifier'][0]['value'],"ClaimNumber not present in the fhir resource") 


##########################################################################################
#Validation of Claims - ClaimPaymentStatus value between input json and transformed Claims JSON    
    def test_claimstatus(self):
        if ClaimsDataInput['ClaimPaymentStatus'] == clmsdataTransformer['period'][0]['start']:
            print(ClaimsDataInput['ClaimPaymentStatus'])
        self.assertEqual(ClaimsDataInput['ClaimPaymentStatus'],clmsdataTransformer['period'][0]['start'],"ClaimPaymentStatus not present in the fhir resource") 

#Validation of Claim - CenseoID value between input json and transformed Claims JSON    
    def test_claimpatientid(self):
        if ClaimsDataInput['CenseoID'] == clmsdataTransformer['patient'][0]['reference']:
            print(ClaimsDataInput['CenseoID'])
        self.assertEqual(ClaimsDataInput['CenseoID'],clmsdataTransformer['active'],"claim not present in the fhir resource") 

#Validation of Claims - ServiceFromDate_Date_of_Service value between input json and transformed Claims JSON    
    def test_claimbillablstart(self):
        if ClaimsDataInput['ServiceFromDate_Date_of_Service'] == clmsdataTransformer['billablePeriod'][0]['start']:
            print(ClaimsDataInput['ServiceFromDate_Date_of_Service'])
        self.assertEqual(ClaimsDataInput['ServiceFromDate_Date_of_Service'],clmsdataTransformer['billablePeriod'][0]['start'],"ServiceFromDate_Date_of_Service not present in the fhir resource") 

#Validation of Claims - ServiceThruDate value between input json and transformed Claims JSON    
    def test_claimbillableend(self):
        if ClaimsDataInput['ServiceThruDate'] == clmsdataTransformer['billablePeriod'][0]['end']:
            print(ClaimsDataInput['ServiceThruDate'])
        self.assertEqual(ClaimsDataInput['ServiceThruDate'],clmsdataTransformer['billablePeriod'][0]['end'],"ServiceThruDate not present in the fhir resource") 

#Validation of Claims - ClaimEntryDate value between input json and transformed Claims JSON    
    def test_claimcreated(self):
        if ClaimsDataInput['ClaimEntryDate'] == print(clmsdataTransformer['created'][0]) :
            print(ClaimsDataInput['ClaimEntryDate'])
        self.assertEqual(ClaimsDataInput['ClaimEntryDate'], clmsdataTransformer['created'][0] ,"ClaimEntryDate not present in the fhir resource") 

#Validation of Claims - Provider_ID value between input json and transformed Claims JSON    
    def test_claimeenterer(self):
        if ClaimsDataInput['Provider_ID'] == print(clmsdataTransformer['enterer'][0]['reference'].split('/')[1].strip()) :
            print(ClaimsDataInput['Provider_ID'])
        self.assertEqual(ClaimsDataInput['Provider_ID'], clmsdataTransformer['enterer'][0]['reference'].split('/')[1].strip() ,"Provider_ID not present in the fhir resource") 

#Validation of Claims - RenderingProviderNPI value between input json and transformed Claims JSON    
    def test_claimspayee(self):
        if ClaimsDataInput['RenderingProviderNPI'] == print(clmsdataTransformer['payee'][0]['type']['coding'][0]['display']) :
            print(ClaimsDataInput['RenderingProviderNPI'])
        self.assertEqual(ClaimsDataInput['RenderingProviderNPI'], clmsdataTransformer['code'][0]['coding'][0]['code'],"RenderingProviderNPI not present in the fhir resource") 

#Validation of Claims - PlaceOfService value between input json and transformed Claims JSON    
    def test_claimfacility(self):
        if ClaimsDataInput['PlaceOfService'] == print(clmsdataTransformer['facility'][0]['identifier']['value']) :
            print(ClaimsDataInput['PlaceOfService'])
        self.assertEqual(ClaimsDataInput['PlaceOfService'], clmsdataTransformer['facility'][0]['identifier']['value'],"PlaceOfService not present in the fhir resource") 

#Validation of Claims - Provider_ID value between input json and transformed Claims JSON    
    def test_providerroleprvdspcltycd(self):
        if ClaimsDataInput['Provider_ID'] == print(clmsdataTransformer['specialty'][0]['coding'][0]['code']) :
            print(ClaimsDataInput['Provider_ID'])
        self.assertEqual(ClaimsDataInput['Provider_ID'], clmsdataTransformer['specialty'][0]['coding'][0]['code'],"Provider_ID not present in the fhir resource") 

#Validation of Claims - careTeam value between input json and transformed Claims JSON    
    def test_claimcareteamref(self):
        if ClaimsDataInput['Provider_ID'] == print(clmsdataTransformer['careTeam'][0]['provider']['reference'].split('/')[1].strip()) :
            print(ClaimsDataInput['Provider_ID'])
        self.assertEqual(ClaimsDataInput['Provider_ID'], clmsdataTransformer['careTeam'][0]['provider']['reference'].split('/')[1].strip(),"Provider_ID not present in the fhir resource") 

#Validation of Claims - DX_1 value between input json and transformed Claims JSON    
    def test_claimdiagnosis1(self):
        if ClaimsDataInput['DX_1'] == print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code']) :
            print(ClaimsDataInput['DX_1'])
        self.assertEqual(ClaimsDataInput['DX_1'], clmsdataTransformer['location']['reference'].split('/')[1].strip(),"DX_1 not present in the fhir resource") 
#Validation of Claims - DX_2 value between input json and transformed Claims JSON    
    def test_claimdiagnosis2(self):
        if ClaimsDataInput['DX_2'] == print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code']) :
            print(ClaimsDataInput['DX_2'])
        self.assertEqual(ClaimsDataInput['DX_2'], clmsdataTransformer['location']['reference'].split('/')[1].strip(),"DX_2 not present in the fhir resource") 
#Validation of Claims - DX_3 value between input json and transformed Claims JSON    
    def test_claimdiagnosis3(self):
        if ClaimsDataInput['DX_3'] == print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding']['code']) :
            print(ClaimsDataInput['DX_3'])
        self.assertEqual(ClaimsDataInput['DX_3'], clmsdataTransformer['location']['reference'].split('/')[1].strip(),"DX_3 not present in the fhir resource") 

#Validation of Claims - ServiceFromDate value between input json and transformed Claims JSON    
    def test_claimsprocedurestart(self):
        if ClaimsDataInput['ServiceFromDate'] == print(clmsdataTransformer['procedure'][0]['date']) :
            print(ClaimsDataInput['ServiceFromDate'])
        self.assertEqual(ClaimsDataInput['ServiceFromDate'],clmsdataTransformer['procedure'][0]['date'],"ServiceFromDate not present in the fhir resource") 
#Validation of Claims - CPTCode_Primary value between input json and transformed Claims JSON    
    def test_claimsprocedurestart(self):
        if ClaimsDataInput['CPTCode_Primary'] == print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding']['code'].split('/')[1].strip()):
            print(ClaimsDataInput['CPTCode_Primary'])
        self.assertEqual(ClaimsDataInput['CPTCode_Primary'],clmsdataTransformer[0]['procedureCodeableConcept']['coding']['code'].split('/')[1].strip(),"CPTCode_Primary not present in the fhir resource") 

#Validation of Claims - BillAmount value between input json and transformed Claims JSON    
    def test_claimstotal(self):
        if ClaimsDataInput['BillAmount'] == print(clmsdataTransformer['total'][0]['value']):
            print(ClaimsDataInput['BillAmount'])
        self.assertEqual(ClaimsDataInput['BillAmount'],clmsdataTransformer['total'][0]['value'],"BillAmount not present in the fhir resource") 



if __name__ == '__main__':
    unittest.main()