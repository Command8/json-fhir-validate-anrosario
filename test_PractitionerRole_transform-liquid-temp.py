import unittest
import json


trans_pracrole_resource = '"resourceType": "PractitionerRole","id":"example","text": {"status": "generated","div": "   "div": "{{msg.text.div | escape_special_chars }}"},'

trans_pracrole_active = '"active": "true"'

trans_pracrole_period = '"period": [{"start": "{{ msg.PROVIDER_ACTIVE_START | date: "yyyy-MM-dd"}}","end": "{{msg.PROVIDER_ACTIVE_END | date: "yyyy-MM-dd"}}",}],'

trans_pracrole_pract = '"practitioner": [{"reference": "Practitioner/id","display": "{{msg.PRACTITIONER}}"}],'

trans_pracrole_org = '"organization": {"reference": "Organization/{{msg.PROVIDER_ORGANIZATION}}","display": "{{msg.PROVIDER_ORGANIZATION}}"},'

trans_pracrole_code = '"code":[{ "coding":[{"system":"http://terminology.hl7.org/CodeSystem/v2-0286","code": "CP","display": "PROVIDER_SPECIALITY_CODE"}],'

trans_pracrole_speclty = '"specialty":[{"coding"{"system":"http://hl7.org/fhir/practitioner-specialty","code": "cardio"}],"text": "{{msg.specialty_Code}}"},],'

trans_pracrole_loc = '"location":   {"reference": "Location/{{msg.PROVIDER_LOCATION}}","display": "{{msg.PROVIDER_LOCATION}}"},'

trans_pracrole_loc = '"healthcareService":   {"reference": "healthcareService/{{msg.PROVIDER_HEALTHCARE_SERVICE}}","display": "{{msg.PROVIDER_HEALTHCARE_SERVICE}}"},'

class TestliqTransform (unittest.TestCase):
    def test_liqpraroleid(self):
        print("resource_type")
         #Validating key PROVIDER_ROLE_ID in liquid template
        if "PROVIDER_ROLE_ID" in trans_pracrole_resource:
            print ("PROVIDER_ROLE_ID" in trans_pracrole_resource)
        #Prints message if the test fails for comparison    
        self.assertEqual("PROVIDER_ROLE_ID" in trans_pracrole_resource,True,"PROVIDER_ROLE_ID not present in liquid template") 

    def test_liqpracroleactive(self):
        print("active")
        #Validating key PROVIDER_ACTIVE in liquid template
        if "PROVIDER_ACTIVE" in trans_pracrole_active:
            print("PROVIDER_ACTIVE" in trans_pracrole_active)
        #Prints message if the test fails for comparison        
        self.assertEqual("PROVIDER_ACTIVE" in trans_pracrole_active,True,"PROVIDER_ACTIVE not present in liquid template") 

    def test_liqpracroleperiodsrt(self):
        print("period")
        #Validating key PROVIDER_ACTIVE_START in liquid template
        if "PROVIDER_ACTIVE_START" in trans_pracrole_period:
            print("PROVIDER_ACTIVE_START" in trans_pracrole_period)
        #Prints message if the test fails for comparison        
        self.assertEqual("PROVIDER_ACTIVE_START" in trans_pracrole_period,True,"PROVIDER_ACTIVE_START not present in liquid template") 

    def test_liqpracroleperiodend(self):
            print("period")
            #Validating key PROVIDER_ACTIVE_END in liquid template
            if "PROVIDER_ACTIVE_END" in trans_pracrole_period:
                print("PROVIDER_ACTIVE_END" in trans_pracrole_period)
            #Prints message if the test fails for comparison        
            self.assertEqual("PROVIDER_ACTIVE_END" in trans_pracrole_period,True,"PROVIDER_ACTIVE_END not present in liquid template") 

    def test_liqpracrolepract(self):
            print("practitioner")
            #Validating key PRACTITIONER in liquid template
            if "PRACTITIONER" in trans_pracrole_pract:
                print("PRACTITIONER" in trans_pracrole_pract)
            #Prints message if the test fails for comparison        
            self.assertEqual("PRACTITIONER" in trans_pracrole_pract,True,"PRACTITIONER not present in liquid template")

    def test_liqpracroleorg(self):
            print("organization")
            #Validating key PROVIDER_ORGANIZATION in liquid template
            if "PROVIDER_ORGANIZATION" in trans_pracrole_org:
                print("PROVIDER_ORGANIZATION" in trans_pracrole_org)
            #Prints message if the test fails for comparison        
            self.assertEqual("PROVIDER_ORGANIZATION" in trans_pracrole_org,True,"PROVIDER_ORGANIZATION not present in liquid template")

    def test_liqpracrolecode(self):
            print("code")
            #Validating key PROVIDER_SPECIALITY_CODE in liquid template
            if "PROVIDER_SPECIALITY_CODE" in trans_pracrole_code:
                print("PROVIDER_SPECIALITY_CODE" in trans_pracrole_code)
            #Prints message if the test fails for comparison        
            self.assertEqual("PROVIDER_SPECIALITY_CODE" in trans_pracrole_code,True,"PROVIDER_SPECIALITY_CODE not present in liquid template")

    def test_liqpracrolespeclty(self):
            print("specialty")
            #Validating key specialty_Code in liquid template
            if "specialty_Code" in trans_pracrole_speclty:
                print("specialty_Code" in trans_pracrole_speclty)
            #Prints message if the test fails for comparison        
            self.assertEqual("specialty_Code" in trans_pracrole_speclty,True,"specialty_Code not present in liquid template")

    def test_liqpracroleloc(self):
            print("location")
            #Validating key PROVIDER_LOCATION in liquid template
            if "PROVIDER_LOCATION" in trans_pracrole_speclty:
                print("PROVIDER_LOCATION" in trans_pracrole_speclty)
            #Prints message if the test fails for comparison        
            self.assertEqual("PROVIDER_LOCATION" in trans_pracrole_speclty,True,"PROVIDER_LOCATION not present in liquid template")

    def test_liqpracroleloc(self):
            print("location")
            #Validating key PROVIDER_LOCATION in liquid template
            if "PROVIDER_LOCATION" in trans_pracrole_speclty:
                print("PROVIDER_LOCATION" in trans_pracrole_speclty)
            #Prints message if the test fails for comparison        
            self.assertEqual("PROVIDER_LOCATION" in trans_pracrole_speclty,True,"PROVIDER_LOCATION not present in liquid template")   


    def test_liqpracroletel(self):
        print("telecom")
     



if __name__ == '__main__':
    unittest.main()