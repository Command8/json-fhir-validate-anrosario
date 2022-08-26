from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
import json
from ntpath import join  
from turtle import pd
import claim_fhir_spec_comments
from pprint import pprint

#import pathlib - Other library that can be used to reference directories

# Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Functions.fhir_functions import getResourceFile

#Using os, Import filepath of directory that file resides in
import os
dir_path = os.path.dirname((__file__))

print("////////////////////////////SNOWFLAKE(INPUT) JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
#fileinputtemp = (dir_path + '/' +'cures-fhir-sig-claims-template.txt')
#fileinputspecs = ('fhir_Specs.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
#fhirSpecsInput = getResourceFile(fileinputspecs)



with open("fhir_spec.json", 'r') as (fhirSpecsInput):
  fhirSpecsResource = json.load(fhirSpecsInput)    


for item, keys in fhirSpecsResource.items():
    #print(fhirSpecsResource.items())
    print(item, ":", keys) 

    
    
    
    

