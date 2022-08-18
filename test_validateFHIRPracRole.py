from pickle import FALSE
import unittest
import json
from ComparePracRole import prdataTransformer,dataPracRoleInput


class TestTransform (unittest.TestCase):  
    
 #Validation of PractitionerRole - PROVIDER_ROLE_ID value between input json and transformed PractitionerRole JSON    
    def test_providerroleid(self):
        if dataPracRoleInput['PROVIDER_ROLE_ID'] == prdataTransformer['identifier'][0]['value']:
            print(dataPracRoleInput['PROVIDER_ROLE_ID'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ROLE_ID'],prdataTransformer['identifier'][0]['value'],"PROVIDER_ROLE_ID not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ACTIVE'] == prdataTransformer['active']:
            print(dataPracRoleInput['PROVIDER_ACTIVE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE'],prdataTransformer['active'],"PROVIDER_ACTIVE not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE_START value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ACTIVE_START'] == prdataTransformer['period'][0]['start']:
            print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE_START'],prdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE_START not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE_END value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ACTIVE_END'] == prdataTransformer['period'][0]['start']:
            print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE_START'],prdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE not present in liquid template") 

#Validation of PractitionerRole - PRACTITIONER value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PRACTITIONER'] == print(prdataTransformer['practitioner'][0]['reference']) :
            print(dataPracRoleInput['PRACTITIONER'])
        self.assertEqual(dataPracRoleInput['PRACTITIONER'], prdataTransformer['practitioner'][0]['reference'] ,"PRACTITIONER not present in liquid template") 

#Validation of PractitionerRole - PRACTITIONER value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PRACTITIONER'] == print(prdataTransformer['practitioner'][0]['display']) :
            print(dataPracRoleInput['PRACTITIONER'])
        self.assertEqual(dataPracRoleInput['PRACTITIONER'], prdataTransformer['practitioner'][0]['display'] ,"PRACTITIONER not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ORGANIZATION value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ORGANIZATION'] == print(prdataTransformer['organization']['reference']) :
            print(dataPracRoleInput['PROVIDER_ORGANIZATION'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ORGANIZATION'], prdataTransformer['organization']['reference'] ,"PRACTITIONER not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ORGANIZATION value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ROLE_CODE'] == print(prdataTransformer['code'][0]['coding'][0]['code']) :
            print(dataPracRoleInput['PROVIDER_ROLE_CODE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ROLE_CODE'], prdataTransformer['code'][0]['coding'][0]['code'],"PRACTITIONER not present in liquid template") 




if __name__ == '__main__':
    unittest.main()