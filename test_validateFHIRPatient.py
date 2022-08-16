
import unittest
import json
from Comparison import dataTransformer,line,input_memgender

class TestTransform (unittest.TestCase):    
    
    #Validation of Member last name between snowflake csv and transformed patient JSON    
    def test_patientlname(self):
        if line['MEMBER_LAST_NAME'] == dataTransformer['name'][0]['family']:

            print('Member Last name Matched')
        else:
            print('Member Last name didnot match')      
    #Validation of Member first name between snowflake csv and transformed patient JSON
    def test_patientfname(self):
        if line['MEMBER_FIRST_NAME'] == dataTransformer['name'][0]['given'][0]:
            print('Member first name Matched')
        else:
            print('Member first name didnot match')
    #Validation of Member last name between snowflake csv and transformed patient JSON
    def test_patientmname(self):
        #if line['MEMBER_MIDDLE_NAME'] == '*****':
            if line['MEMBER_MIDDLE_NAME'] == dataTransformer['name'][0]['given'][1]:
                print('Member middle name Matched')
            else:
                print('Member middle name didnot match')
    #Validation of Member censeoid between snowflake csv and transformed patient JSON
    def test_patientcenseoid(self):
        if line['CENSEOID'] == dataTransformer['identifier'][0]['value']:
            print('Member censoid Matched')
        else:
            print('Member censoid didnot match')  
    #Validation of Member censeoid between snowflake csv and transformed patient JSON
    def test_patientadd1(self):
        if line['MEMBER_ADDRESS1'] == dataTransformer['address'][0]['line'].split(',')[0]:
            print('Member address 1 Matched')
        else:
            print('Member address 1 didnot match')  
    #Validation of Member address 2 between snowflake csv and transformed patient JSON
    def test_patientadd2(self):
        if line['MEMBER_ADDRESS2'] == dataTransformer['address'][0]['line'].split(',')[1].strip():
            print('Member address 2 Matched')
        else:
            print('Member address 2 didnot match')
    #Validation of Member city between snowflake csv and transformed patient JSON
    def test_patientcity(self):
        if line['MEMBER_CITY'] == dataTransformer['address'][0]['city']:
            print('Member city Matched')
        else:
            print('Member city didnot match') 
    #Validation of Member state between snowflake csv and transformed patient JSON
    def test_patientstate(self):
        if line['MEMBER_STATE'] == dataTransformer['address'][0]['state']:
            print('Member state Matched')
        else:
            print('Member state didnot match') 
    #Validation of Member DOB between snowflake csv and transformed patient JSON
    def test_patientdob(self):
        if line['MEMBER_DATE_OF_BIRTH'] == dataTransformer['birthDate']:
            print('Member DOB Matched')
        else:
            print('Member DOB didnot match')
    #Validation of Member GENDER between snowflake csv and transformed patient JSON
    def test_patientgender(self):
        if input_memgender == dataTransformer['gender']:
            print('Member GENDER Matched')
        else:
            print('Member GENDER didnot match')
    #Validation of PCP_ID between snowflake csv and transformed patient JSON
#    def test_pcpid(self):
#        if line['PCP_ID'] == dataTransformer['generalPractitioner'][0]['reference'].split('/')[1]:
#            print('PCP_ID Matched')
#        else:
#            print('PCP_ID didnot match')
    #Validation of PCP_Firstname between snowflake csv and transformed patient JSON
    def test_pcpfirstname(self):
        if line['PCP_FIRSTNAME'] == dataTransformer['generalPractitioner'][0]['display'].split(' ')[0]:
            print('PCP Firstname Matched')
        else:
            print('PCP Firstname didnot match')
    #Validation of PCP_Lastname between snowflake csv and transformed patient JSON
    def test_pcplastname(self):
        if line['PCP_LASTNAME'] == dataTransformer['generalPractitioner'][0]['display'].split(' ')[1]:
            print('PCP Lastname Matched')
        else:
            print('PCP Lastname didnot match')
    
if __name__ == '__main__':
    unittest.main()

