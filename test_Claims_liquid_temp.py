import unittest
import json

trans_claims_resource = '  "resourceType" : "Claim","identifier" : {"use": "official","value": "{{msg.ClaimNumber}}",},'

trans_claims_status = '"status" : "active",'

trans_claims_type = '"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type","code": "institutional"//Should this be institutional or professional}]},'

trans_claims_use = '"use" : "claim", '

trans_claims_patient =   '"patient" : {"reference": "Patient/{{msg.CenseoID}}"'

trans_claims_billablePeriod = '"billablePeriod": {"start": "{{msg.ServiceFromDate_Date_of_Service | date: "yyyy-MM-dd"}}","end": "{{msg.ServiceThruDate | date: "yyyy-MM-dd"}}"},'

trans_claims_created = '"created" : "{{msg.ClaimEntryDate | date: "yyyy-MM-dd"}}", '

trans_claims_enterer = '"enterer" : {"reference": "Practitioner/{{msg.Provider_ID}}"'

trans_claims_provider = '"provider" : {"reference": "Practitioner/{{msg.Provider_ID}}"},'

trans_claims_ = '"priority" : { "coding": [{"code": "normal"]},'

trans_claims_prescription = '"prescription" : { "reference": "MedicationRequest/{{msg.MedicationID}}"},"payee" : { "type": {"coding":[{"code": "provider","display": "{{msg.RenderingProviderNPI}}""}]}},'

trans_claims_payee = '"payee" : { "type": {"coding":[{"code": "provider","display": "{{msg.RenderingProviderNPI}}""}]}},'

trans_claims_facility = '"facility" : {"identifier":{"value": "{{msg.PlaceOfService}}"}'

trans_claims_careTeam = '"careTeam": [{"sequence": 1,"provider": {"reference": "Practitioner/{{msg.Provider_ID}}"}}],'

trans_claims_diagnosis = '"diagnosis" : [{ "sequence" : 1, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_1}}"}]}},{ "sequence" : 2, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_2}}"}]}},{ "sequence" : 3, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_3}}"}]}}],'

trans_claim_procedure = '"procedure": [{"sequence": 1,"type": [{"coding": [{"code": "primary"}]}],"date": "{{msg.ServiceFromDate /Date_of_Service | date: "yyyy-MM-dd"}}","procedureCodeableConcept": {"coding": [{"code": "{{msg.ProcedureCode /CPTCode_Primary}}"}]}},{"sequence": 2,"type": [{"coding": [{"code": "secondary"}]}],"date": "{{msg.ServiceFromDate /Date_of_Service | date: "yyyy-MM-dd"}}","procedureCodeableConcept": {"coding": [{"code": "{{msg.ProcedureCode2}}"}]}}],  '

trans_claims_insure =   '"insurance" : [{ /"sequence" : 1, "focal" : true, "coverage" : {"reference" : "Coverage/{{msg.CoverageID}}"} }],'

trans_claims_total = '"total" :{"value": "{{msg.BillAmount}}" }'

class TestliqTransform (unittest.TestCase):
        def test_liqclmsnum(self):
            print("identifier.value = ClaimNumber exists:")
            #Validating key ClaimNumber in liquid template
            if "ClaimNumber" in trans_claims_resource:
                print ("ClaimNumber" in trans_claims_resource)
            #Prints message if the test fails for comparison    
            self.assertEqual("ClaimNumber" in trans_claims_resource,True,"ClaimNumber not present in liquid template") 

        def test_liqclmspatientid(self):
            print("patient.reference = CenseoID exists:")
            #Validating key CenseoID in liquid template
            if "CenseoID" in trans_claims_patient:
                print ("CenseoID" in trans_claims_patient)
            #Prints message if the test fails for comparison    
            self.assertEqual("CenseoID" in trans_claims_patient,True,"CenseoID not present in liquid template") 

        def test_liqclmsbp1(self):
            print("billablePeriod.start = ServiceFromDate exists:")
            #Validating key ServiceFromDate_Date_of_Service in liquid template
            if "ServiceFromDate" in trans_claims_billablePeriod:
                print ("ServiceFromDate" in trans_claims_billablePeriod)
            #Prints message if the test fails for comparison    
            self.assertEqual("ServiceFromDate" in trans_claims_billablePeriod,True,"ServiceFromDate not present in liquid template") 

        def test_liqclmsbp2(self):
            print("billablePeriod.end = ServiceThruDate exists:")
            #Validating key ServiceThruDate in liquid template
            if "ServiceThruDate" in trans_claims_billablePeriod:
                print ("ServiceThruDate" in trans_claims_billablePeriod)
            #Prints message if the test fails for comparison    
            self.assertEqual("ServiceThruDate" in trans_claims_billablePeriod,True,"ServiceThruDate not present in liquid template") 




if __name__ == '__main__':
    unittest.main()