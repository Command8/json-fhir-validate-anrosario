from pickle import FALSE
import unittest
import json
from CompareClaims import clmsdataTransformer,ClaimsDataInput


class TestTransform (unittest.TestCase):  
    
 #Validation of Claims - ClaimNumber value between input json and transformed Claims JSON    
    def test_claimsclaimnum(self):
        if ClaimsDataInput['ClaimNumber'] == clmsdataTransformer['identifier'][0]['value']:
            print(ClaimsDataInput['ClaimNumber'])
        self.assertEqual(ClaimsDataInput['ClaimNumber'],clmsdataTransformer['identifier'][0]['value'],"ClaimNumber not present in liquid template") 

#Validation of Claims - CenseoID value between input json and transformed Claims JSON    
    def test_claimspatientid(self):
        if ClaimsDataInput['CenseoID'] == clmsdataTransformer['patient'][0]['reference']:
            print(ClaimsDataInput['CenseoID'])
        self.assertEqual(ClaimsDataInput['CenseoID'],clmsdataTransformer['active'],"claim not present in liquid template") 
##########################################################################################
#Validation of Claims - PROVIDER_ACTIVE_START value between input json and transformed Claims JSON    
    def test_providerroleprvdactvstr(self):
        if ClaimsDataInput['PROVIDER_ACTIVE_START'] == clmsdataTransformer['period'][0]['start']:
            print(ClaimsDataInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(ClaimsDataInput['PROVIDER_ACTIVE_START'],clmsdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE_START not present in liquid template") 

#Validation of Claims - PROVIDER_ACTIVE_END value between input json and transformed Claims JSON    
    def test_providerroleprvdactvend(self):
        if ClaimsDataInput['PROVIDER_ACTIVE_END'] == clmsdataTransformer['period'][0]['start']:
            print(ClaimsDataInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(ClaimsDataInput['PROVIDER_ACTIVE_START'],clmsdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE not present in liquid template") 

#Validation of Claims - PRACTITIONER value between input json and transformed Claims JSON    
    def test_providerroleprvdprctdis(self):
        if ClaimsDataInput['PRACTITIONER'] == print(clmsdataTransformer['practitioner'][0]['display']) :
            print(ClaimsDataInput['PRACTITIONER'])
        self.assertEqual(ClaimsDataInput['PRACTITIONER'], clmsdataTransformer['practitioner'][0]['display'] ,"PRACTITIONER not present in liquid template") 

#Validation of Claims - PROVIDER_ORGANIZATION value between input json and transformed Claims JSON    
    def test_providerroleprvdorg(self):
        if ClaimsDataInput['PROVIDER_ORGANIZATION'] == print(clmsdataTransformer['organization']['reference']) :
            print(ClaimsDataInput['PROVIDER_ORGANIZATION'])
        self.assertEqual(ClaimsDataInput['PROVIDER_ORGANIZATION'], clmsdataTransformer['organization']['reference'].split('/')[1].strip() ,"PROVIDER_ORGANIZATION not present in liquid template") 

#Validation of Claims - PROVIDER_ROLE_CODE value between input json and transformed Claims JSON    
    def test_providerroleprvdrlcode(self):
        if ClaimsDataInput['PROVIDER_ROLE_CODE'] == print(clmsdataTransformer['code'][0]['coding'][0]['code']) :
            print(ClaimsDataInput['PROVIDER_ROLE_CODE'])
        self.assertEqual(ClaimsDataInput['PROVIDER_ROLE_CODE'], clmsdataTransformer['code'][0]['coding'][0]['code'],"PROVIDER_ROLE_CODE not present in liquid template") 

#Validation of Claims - PROVIDER_ROLE_CODE_DESC value between input json and transformed Claims JSON    
    def test_providerroleprvdrlcodedesc(self):
        if ClaimsDataInput['PROVIDER_ROLE_CODE_DESC'] == print(clmsdataTransformer['code'][0]['text']) :
            print(ClaimsDataInput['PROVIDER_ROLE_CODE_DESC'])
        self.assertEqual(ClaimsDataInput['PROVIDER_ROLE_CODE_DESC'], clmsdataTransformer['code'][0]['text'],"PROVIDER_ROLE_CODE_DESC not present in liquid template") 

#Validation of Claims - PROVIDER_SPECIALITY_CODE value between input json and transformed Claims JSON    
    def test_providerroleprvdspcltycd(self):
        if ClaimsDataInput['PROVIDER_SPECIALITY_CODE'] == print(clmsdataTransformer['specialty'][0]['coding'][0]['code']) :
            print(ClaimsDataInput['PROVIDER_SPECIALITY_CODE'])
        self.assertEqual(ClaimsDataInput['PROVIDER_SPECIALITY_CODE'], clmsdataTransformer['specialty'][0]['coding'][0]['code'],"PROVIDER_SPECIALITY_CODE not present in liquid template") 

#Validation of Claims - PROVIDER_SPECIALITY_DESC value between input json and transformed Claims JSON    
    def test_providerroleprvdspcltycddesc(self):
        if ClaimsDataInput['PROVIDER_SPECIALITY_DESC'] == print(clmsdataTransformer['specialty'][0]['text']) :
            print(ClaimsDataInput['PROVIDER_SPECIALITY_DESC'])
        self.assertEqual(ClaimsDataInput['PROVIDER_SPECIALITY_DESC'], clmsdataTransformer['specialty'][0]['text'],"PROVIDER_SPECIALITY_DESC not present in liquid template") 

#Validation of Claims - PROVIDER_LOCATION value between input json and transformed Claims JSON    
    def test_providerroleprvdloc1(self):
        if ClaimsDataInput['PROVIDER_LOCATION'] == print(clmsdataTransformer['location']['reference']) :
            print(ClaimsDataInput['PROVIDER_LOCATION'])
        self.assertEqual(ClaimsDataInput['PROVIDER_LOCATION'], clmsdataTransformer['location']['reference'].split('/')[1].strip(),"PROVIDER_LOCATION not present in liquid template") 

#Validation of Claims - PROVIDER_LOCATION value between input json and transformed Claims JSON    
    def test_providerroleprvdloc2(self):
        if ClaimsDataInput['PROVIDER_LOCATION'] == print(clmsdataTransformer['location']['display']) :
            print(ClaimsDataInput['PROVIDER_LOCATION'])
        self.assertEqual(ClaimsDataInput['PROVIDER_LOCATION'],clmsdataTransformer['location']['display'],"PROVIDER_LOCATION not present in liquid template") 

#Validation of Claims - PROVIDER_HEALTHCARE_SERVICE value between input json and transformed Claims JSON    
    def test_providerroleprvdhcs(self):
        if ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'] == print(clmsdataTransformer['healthcareService']['reference']) :
            print(ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'])
        self.assertEqual(ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'],clmsdataTransformer['healthcareService']['reference'].split('/')[1].strip(),"PROVIDER_HEALTHCARE_SERVICE not present in liquid template") 

#Validation of Claims - PROVIDER_HEALTHCARE_SERVICE display value between input json and transformed Claims JSON    
    def test_providerroleprvdhcsdsply(self):
        if ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'] == print(clmsdataTransformer['healthcareService']['display']) :
            print(ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'])
        self.assertEqual(ClaimsDataInput['PROVIDER_HEALTHCARE_SERVICE'],clmsdataTransformer['healthcareService']['display'],"PROVIDER_HEALTHCARE_SERVICE Display not present in liquid template") 


#Validation of Claims - PROVIDER_PHONEPRIMARY  value between input json and transformed Claims JSON    
    def test_providerroleprvdph1(self):
        if ClaimsDataInput['PROVIDER_PHONEPRIMARY'] == print(clmsdataTransformer['telecom'][0]['value']) :
            print(ClaimsDataInput['PROVIDER_PHONEPRIMARY'])
        self.assertEqual(ClaimsDataInput['PROVIDER_PHONEPRIMARY'],clmsdataTransformer['telecom'][0]['value'],"PROVIDER_PHONEPRIMARY not present in liquid template") 

#Validation of Claims - PROVIDER_PHONESECONDARY  value between input json and transformed Claims JSON    
    def test_providerroleprvdph2(self):
        if ClaimsDataInput['PROVIDER_PHONESECONDARY'] == print(clmsdataTransformer['telecom'][1]['value']) :
            print(ClaimsDataInput['PROVIDER_PHONESECONDARY'])
        self.assertEqual(ClaimsDataInput['PROVIDER_PHONESECONDARY'],clmsdataTransformer['telecom'][1]['value'],"PROVIDER_PHONESECONDARY not present in liquid template") 

#Validation of Claims - PROVIDER_CONTACT  value between input json and transformed Claims JSON    
    def test_providerroleprvdph3(self):
        if ClaimsDataInput['PROVIDER_CONTACT'] == print(clmsdataTransformer['telecom'][2]['value']) :
            print(ClaimsDataInput['PROVIDER_CONTACT'])
        self.assertEqual(ClaimsDataInput['PROVIDER_CONTACT'],clmsdataTransformer['telecom'][2]['value'],"PROVIDER_CONTACT not present in liquid template") 

#Validation of Claims - PROVIDER_FAX  value between input json and transformed Claims JSON    
    def test_providerroleprvdph4(self):
        if ClaimsDataInput['PROVIDER_FAX'] == print(clmsdataTransformer['telecom'][3]['value']) :
            print(ClaimsDataInput['PROVIDER_FAX'])
        self.assertEqual(ClaimsDataInput['PROVIDER_FAX'],clmsdataTransformer['telecom'][3]['value'],"PROVIDER_FAX not present in liquid template") 

#Validation of Claims - PROVIDER_AVAILABLE_STARTTIME  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlstr(self):
        if ClaimsDataInput['PROVIDER_AVAILABLE_STARTTIME'] == print(clmsdataTransformer['availableTime'][0]['availableStartTime']) :
            print(ClaimsDataInput['PROVIDER_AVAILABLE_STARTTIME'])
        self.assertEqual(ClaimsDataInput['PROVIDER_AVAILABLE_STARTTIME'],clmsdataTransformer['availableTime'][0]['availableStartTime'],"PROVIDER_AVAILABLE_STARTTIME not present in liquid template") 

#Validation of Claims - PROVIDER_AVAILABLE_ENDTIME  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlend(self):
        if ClaimsDataInput['PROVIDER_AVAILABLE_ENDTIME'] == print(clmsdataTransformer['availableTime'][0]['availableStartTime']) :
            print(ClaimsDataInput['PROVIDER_AVAILABLE_ENDTIME'])
        self.assertEqual(ClaimsDataInput['PROVIDER_AVAILABLE_ENDTIME'],clmsdataTransformer['availableTime'][0]['availableStartTime'],"PROVIDER_AVAILABLE_ENDTIME not present in liquid template") 

#Validation of Claims - PROVIDER_SERVICE_NOT_AVAILABLE_FROM  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlend(self):
        if ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'] == print(clmsdataTransformer['notAvailable'][0]['during']['start']) :
            print(ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'])
        self.assertEqual(ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'],clmsdataTransformer['notAvailable'][0]['during']['start'],"PROVIDER_SERVICE_NOT_AVAILABLE_FROM not present in liquid template") 

#Validation of Claims - PROVIDER_SERVICE_NOT_AVAILABLE_TO  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlend(self):
        if ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'] == print(clmsdataTransformer['notAvailable'][0]['during']['end']) :
            print(ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'])
        self.assertEqual(ClaimsDataInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'],clmsdataTransformer['notAvailable'][0]['during']['end'],"PROVIDER_SERVICE_NOT_AVAILABLE_TO not present in liquid template") 

#Validation of Claims - AVAILABILIY_EXCEPTION  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlexcpt(self):
        if ClaimsDataInput['AVAILABILIY_EXCEPTION'] == print(clmsdataTransformer['availabilityExceptions']) :
            print(ClaimsDataInput['AVAILABILIY_EXCEPTION'])
        self.assertEqual(ClaimsDataInput['AVAILABILIY_EXCEPTION'],clmsdataTransformer['availabilityExceptions'],"AVAILABILIY_EXCEPTION not present in liquid template") 

#Validation of Claims - ENDPOINT_ACCESS reference  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlend1(self):
        if ClaimsDataInput['ENDPOINT_ACCESS'] == print(clmsdataTransformer['endpoint'][0]['reference']) :
            print(ClaimsDataInput['ENDPOINT_ACCESS'])
        self.assertEqual(ClaimsDataInput['ENDPOINT_ACCESS'],clmsdataTransformer['endpoint'][0]['reference'].split('/')[1].strip(),"ENDPOINT_ACCESS reference not present in liquid template") 

#Validation of Claims - ENDPOINT_ACCESS display  value between input json and transformed Claims JSON    
    def test_providerroleprvdavlend2(self):
        if ClaimsDataInput['ENDPOINT_ACCESS'] == print(clmsdataTransformer['endpoint'][0]['display']) :
            print(ClaimsDataInput['ENDPOINT_ACCESS'])
        self.assertEqual(ClaimsDataInput['ENDPOINT_ACCESS'],clmsdataTransformer['endpoint'][0]['display'],"ENDPOINT_ACCESS reference not present in liquid template") 



if __name__ == '__main__':
    unittest.main()