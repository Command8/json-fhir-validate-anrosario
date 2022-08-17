from lib2to3.pgen2 import token
from typing import get_args
from wsgiref import headers
import requests
#from crypt import methods
import pprint
import json
from Functions.fhir_functions import getResourceType
import secret
import extract



headers = {'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Bearer {}' .format(secret.auth_token),'Content-Length': '1300', 'Content-Type': 'application/json; charset=utf-8'}



#Gets the json of the transformed fhir resources and loads it into a variable




transformed_fhir_patient = getResourceType('CreatePatientResource.json', 'Patient')[0]



payload = transformed_fhir_patient
#print(payload)
response_post = requests.post('https://sbx-usc-fhir-api.azurehealthcareapis.com/Patient/', headers=headers,json=payload)
#print(payload)
#print(response_post.request.headers)
print (response_post.text)
response_load = json.loads(response_post.text)
print(response_load['id'])
print (response_post.status_code)  
patientid = response_load['id'] 