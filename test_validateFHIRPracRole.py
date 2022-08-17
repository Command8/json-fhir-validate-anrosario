import unittest
import json
from ComparePracRole import prdataTransformer,dataPracRoleInput


class TestTransform (unittest.TestCase):  

 #Validation of Member last name between input json and transformed patient JSON    
    def test_patientlname(self):
        if dataPracRoleInput['PROVIDER_ROLE_ID'] == prdataTransformer['identifier'][0]['value']:
            print('PROVIDER_ROLE_ID Matched')
        self.assertEqual("PROVIDER_ROLE_ID" in prdataTransformer,True,"PROVIDER_ROLE_ID not present in liquid template") 


if __name__ == '__main__':
    unittest.main()