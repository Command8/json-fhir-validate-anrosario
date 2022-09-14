import unittest
from Functions.fhir_functions import openTxtfile


from HCS_Reader import csvValidate

variables = []

HCS_Data = csvValidate('HCS_CombinedData.csv', 'Claims')
#print(HCS_Data)

variables = openTxtfile('Output.txt')
#print(variables)





class Testvalidatehcs (unittest.TestCase):

    #open liquid template text file
    #if HCS_Data in TemplateVariables

        #print dataelement is visible in liquid template





 if __name__ == '__main__':
    unittest.main()   