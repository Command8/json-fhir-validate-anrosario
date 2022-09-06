from fileinput import filename
import json

fileName = ''   # Variable for Input JSON file
fhirResource = '' # variable for Resourcefile
fhirResourceType = '' # variable for ResourceType

#Function for passing Input JSON as parameter
def getResourceFile (fileName):
    with open(fileName,'r') as (fhirResourceFile):
        fhirResource = json.load(fhirResourceFile)       
        values = (fhirResource)
        return values

#Function for passing Input JSON, field value as parameters
def getResourceType (fileName,fhirResourceType):
    with open((fileName),'r') as (fhirResourceFile):
        fhirResource = json.load(fhirResourceFile)       
        fhirResourceType = fhirResource['resourceType']
        print (fhirResourceType)
        values = (fhirResource,fhirResourceType)
        return values  


def getlines(filename):
    #try and catch feature to capture if file is unavailable
    try:
        #Read the file and read individual lines
        file = open(filename,"r")
        readfl = file.readlines()
        file.close()
        #Run a for loop to print each line from HL7 JSON
        for sentence in readfl:
            print (sentence)
    except FileExistsError:
        print ("File is not there")
       


#getResourceType(fileName,fhirResource)



