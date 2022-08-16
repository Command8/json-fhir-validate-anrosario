from fileinput import filename
import json
import extract
#Common functions for the project


fileName = ''#'CreatePatientResource.json'
fhirResource = ''
fhirResourceType = ''
#with open('CreatePatientResource.json','r') as (fhirResourceFile):
#    fhirResource = json.load(fhirResourceFile)

#   print(fhirResource)

def getResourceType (fileName,fhirResourceType):
    with open(fileName,'r') as (fhirResourceFile):
        fhirResource = json.load(fhirResourceFile)
        fhirResourceType = fhirResource['resourceType']
        print (fhirResourceType)
        values = (fhirResource,fhirResourceType)
        return values
       



#getResourceType(fileName,fhirResource)



