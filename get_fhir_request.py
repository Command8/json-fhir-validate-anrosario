from lib2to3.pgen2 import token
from typing import get_args
from wsgiref import headers
from post_fhir_request import patientid




import requests
#from crypt import methods
import pprint
import json
import secret

from Functions.fhir_functions import getResourceType , fileName , fhirResource, fhirResourceType


#THIS SCRIPT REQUIRES A TOKEN BE GENERATED IN POSTMAN BEFORE RUNNING. 
#Would like to make the script generate it's own token before runtime. 

getResourceType ('CreatePatientResource.json', 'Patient')
patientid = 'ABCD00012'
fhirResourceType = getResourceType ('CreatePatientResource.json', 'Patient')
get_metadata_endpoint = 'metadata'
#get_patient_endpoint = fhirResourceType +'/', patientid
#get_patient_endpoint = fhirResourceType+'/', patientid
#print('end point is: '+ fhirResourceType)
#post_patient_endpoint = fhirResource 




#Headers


#To get the headers for the request use print(response_get.request.headers)
#Token is of data type "tuple" it must be formatted using the: 
#Code: 'Authorization': 'Bearer {}' .format(auth_token)
headers = {'Authorization': 'Bearer {}' .format(secret.auth_token),'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}



#Cannot concatenate "tuple" and str error occurs when trying to send the request with an arg or concatenated strings and datatype truple.  


#get request for Patient using the Patient id number in the url

#response_get = requests.get('https://sbx-usc-fhir-api.azurehealthcareapis.com/Patient?identifier='+ patientid, headers=headers)

response_get = requests.get('https://sbx-usc-fhir-api.azurehealthcareapis.com/Patient?identifier=ABCD00012', headers=headers)


#response_get = requests.get('https://sbx-usc-fhir-api.azurehealthcareapis.com/metadata')#, headers=headers) #, 'Auth URL:', auth_url, 'Access Token URL:', str(authtoken_url), 'Client ID:' , client_id})

#***********************************************************************************************

#the print line below gets the correct headers with the exception of Authorization 
#use: 'Authorization': 'Bearer {}' .format(auth_token) and add it to the headers

#************************USE THIS CODE TO DEBUG HEADERS*****************************************
#print(response_get.request.headers)
#***********************************************************************************************
load_get = json.loads(response_get.text)
print(load_get)
#print(load_get['name'][0]['family'][0])
resource = load_get['entry'][0]['resource']['resourceType']
print(resource)
patientfhirid = load_get['entry'][0]['resource']['id']
print(patientfhirid)
primaryBundleId = load_get['id']
print(primaryBundleId)
responseCode = response_get.status_code
print(responseCode)

