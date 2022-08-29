from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
import json
from ntpath import join  
from turtle import pd
import claim_fhir_spec_comments
from pprint import pprint
#from extract import json_extract

#import pathlib - Other library that can be used to reference directories

# Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Functions.fhir_functions import getResourceFile

#Using os, Import filepath of directory that file resides in
import os
dir_path = os.path.dirname((__file__))

print("////////////////////////////FHIR JSON Data///////////////////////////////////////////")

arr = []

with open("Claim_fhir_spec.json", 'r') as (fhirSpecsInput):
  fhirSpecsResource = json.load(fhirSpecsInput)
  for obj, keys,in fhirSpecsResource.items():
    print(obj, ":", keys)



 

 


    
   

      

    
    
    
    

