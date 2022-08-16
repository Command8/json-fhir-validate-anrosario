
import unittest
import json
from typing_extensions import Self

    
trans_practitioner_resource = '"resourceType": "Practitioner","id": "example","text":{"status": "generated","div": "{{msg.text.div | escape_special_chars }}},'"identifier": [{"use": "official","value": "{{msg.PCP_ID }}"},{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "NPI","display" : "National provider identifier"}]},"value": "{{ msg.PROVIDER_NPI }}"},{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "UPIN","display" : "PHYSICIAN IDENTIFICATION NUMBER"}]},"value": "{{ msg.PROVIDER_PIN }}"},{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "TAX"}]},"value": "{{ msg.PROVIDER_TAXID}}"},{"use": "official","value": "{{msg.IPA }}"},{"use": "official","value": "{{msg.IPA_IDENTIFIER }}"},{"use": "official","value": "{{msg.LPO }}"}{"use": "official","value": "{{ msg.LPO_IDENTIFIER }}""use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "SN","display" : "SUBSCIBER identifier"}]},"value": "{{ msg.SUBSCRIBER_ID }}"},{"use": "official","value": "{{ msg.PCP_PROVIDER_ID }}"},{"use": "official","value": "{{ msg.PROVIDER_ID }}"},{"use": "official","type": {"coding": [{"system": "http://hl7.org/fhir/ValueSet/provider-taxonomy","code": "103G00000X","display" : "PROVIDER_TAXONOMY_CODE ",}]},"value": "{{msg.PROVIDER_TAXONOMY_CODE }}"},{"use": "official","type":{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203"},"code": "BSNR","display" : "PROVIDER_LOCATION_ID"[{"value": "{{msg.PROVIDER_LOCATION_ID }}"}],"active": true,"name":[{"family": "{{ msg.PROVIDER_LASTNAME }}","given": ["{{ msg.PROVIDER_FIRSTNAME }}","{{ msg.PROVIDER_MIDDLE_INITIAL}}"],"prefix":[{{ msg.PROVIDER_PREFIX}}"]"text": "{{ msg.OFFICE_CONTACT_NAME }}"},'

class TestliqTransform (unittest.TestCase):
    print("resource_type")
    print("identifier")
    
    def test_liqpracid(self):
        if "PCP_ID" in trans_prac_resource:
            print("PCP_ID is Visible in ")
            #Prints message if the test fails for comparison
        self.assertEqual("PCP_ID" in trans_prac_resource,True,"PCP_ID not present in liquid template")

        #Validating key PROVIDER_NPI in liquid template
    def test_liqpracnpi(self):
        if ("PROVIDER_NPI" in trans_practitioner_id) == True:
            print ("PROVIDER_NPI presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_NPI" in trans_practitioner_id,True,"PROVIDER_NPI not present in liquid template")

    def test_liqpracnpin(self):
        if ("PROVIDER_PIN" in trans_practitioner_id) == True:
            print ("PROVIDER_PIN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_PIN" in trans_practitioner_id,True,"PROVIDER_PIN not present in liquid template")
    

    
    #Validating key PROVIDER_FIRSTNAME in liquid template

    print("telecom")
    trans_telecom = '    "telecom": [{"system": "phone","value": "{{msg.PROVIDER_PHONE}}",},{"system": "fax","value": "{{msg.PROVIDER_FAX}}",}{"system": "email","value": "{{msg.PROVIDER_EMAIL}}",},], 



    if "PROVIDER_CELL" in trans_telecom:
        print("PROVIDER_CELL" in trans_telecom)
    if "PROVIDER_EMAIL" in trans_telecom:
        print("PROVIDER_EMAIL" in trans_telecom)

    print("gender")
    trans_gender = '"gender":{% if msg.PROVIDER_GENDER =="1" -%}"male",{% elsif msg.PROVIDER_GENDER == "2" -%}"female",{% elsif msg.PROVIDER_GENDER == "3" -%}"unknown",{% elsif code -%}"other",{% else %}"",{% endif -%}'
    if "PROVIDER_GENDER" in trans_gender:
        print("PROVIDER_GENDER" in trans_gender)

    print("dob")
    trans_dob = '"birthDate": "{{ msg.PROVIDER_DATE_OF_BIRTH  }}"'
    if "PROVIDER_DATE_OF_BIRTH" in trans_dob:
        print("PROVIDER_DATE_OF_BIRTH" in trans_dob)

    print("deceasedBoolean")
    trans_deceased = '"deceasedBoolean": "{{msg.DeceasedBoolean}}"'
    if 'DeceasedBoolean' in trans_deceased:
        print("DeceasedBoolean" in trans_deceased)

    print("address")
    trans_address =  '"address": [{"use": "billing","type": "physical","line": "{{msg.PROVIDER_ADDRESS1}}, {{msg.PROVIDER_ADDRESS2}},{{msg.PROVIDER_ADDRESS3}}","city": "{{msg.PROVIDER_CITY}}","state":"{{msg.PROVIDER_STATE}}","district": "{{msg.PROVIDER_COUNTY}}","postalCode": "{{msg.PROVIDER_ZIPCode}}"},'
    if "PROVIDER_ADDRESS1" in trans_address:
        print("PROVIDER_ADDRESS1" in trans_address)

    if "PROVIDER_ADDRESS2" in trans_address:
        print("PROVIDER_ADDRESS2" in trans_address)

    if "PROVIDER_CITY"in trans_address:
        print("PROVIDER_CITY" in trans_address)

    if "PROVIDER_COUNTY" in trans_address:
        print("PROVIDER_COUNTY" in trans_address)

    if "PROVIDER_STATE"in trans_address:
        print("PROVIDER_STATE" in trans_address)

    if "PROVIDER_ZIP" in trans_address:
        print("PROVIDER_ZIP" in trans_address)

    if "country" in trans_address:
        print("country" in trans_address)


    if "MEMBER_MAIL_ADDRESS1"in trans_address:
        print("MEMBER_MAIL_ADDRESS1" in trans_address)

    if "MEMBER_MAIL_ADDRESS2"in trans_address:
        print("MEMBER_MAIL_ADDRESS2" in trans_address)

    if "MEMBER_MAIL_CITY"in trans_address:
        print("MEMBER_MAIL_CITY" in trans_address)

    if "MEMBER_MAIL_STATE"in trans_address:
        print("MEMBER_MAIL_STATE" in trans_address)

    if "MEMBER_MAIL_ZIP"in trans_address:
        print("MEMBER_MAIL_ZIP" in trans_address)


    #no snowflake reference
    print("MaritaStatus")
    trans_maritalStatus =  '"maritalStatus":{"valueCodeableConcept":"coding":[{"system":"http://terminology.hl7.org/CodeSystem/v3-MaritalStatus","code": "{{msg.MaritalStatusCode}}","display":"{{msg.MaritalStatus}}", }],"text": "{{msg.MaritalStatus}}"}},'
    if "MaritalStatusCode"in trans_maritalStatus:
        print("MaritalStatusCode" in trans_maritalStatus)
    if "MaritalStatus" in trans_maritalStatus:
        print("MaritalStatus" in trans_maritalStatus)

    #no snowflake reference
    print("multipleBirthBoolean")
    trans_multibirth = '"multipleBirthBoolean": "{{msg.MultipleBirth}}"'
    if "MaritalStatusCode"in trans_multibirth:
        print("MaritalStatusCode" in trans_multibirth)


    print("gender")
    trans_gender = '"gender":[{% if msg.MEMBER_GENDER == "1" -%}"male"{% elsif msg.MEMBER_GENDER == "2" -%} "female",{% elsif msg.MEMBER_GENDER == "3" -%} "unknown",{% elsif code -%}"other",{% else %}"",{% endif -%}]}'
    if 'MEMBER_GENDER == "1"'in trans_gender:
        print('MEMBER_GENDER == "1"' in trans_gender)
    if 'MEMBER_GENDER == "2"'in trans_gender:
        print('MEMBER_GENDER == "2"' in trans_gender)
    if 'MEMBER_GENDER == "3"'in trans_gender:
        print('MEMBER_GENDER == "3"' in trans_gender)
    if "unknown" in trans_gender:
        print("unknown" in trans_gender)
    if "other" in trans_gender:
        print("other" in trans_gender)


    print("contact")
    trans_contact = '"Contact": [{{% for p in msg["Contact"] -%}"system": "http://hl7.org/fhir/ValueSet/patient-contactrelationship","value": "{{ p.relationship }}","name": {"family": "{{ p.KinName.lastname }}","given": ["{{ p.KinName.firstname }}"]},"gender": "{{p.kinGender}}","organization": {"reference": "Organization/{{p.contOrgId}}","display": "{{p.organization}}"},"period":{"start": "{{ p.startDate | add_hyphens_date }}","end": "{{ p.endDate | add_hyphens_date }}",},"telecom": [{"system": "home","value": "{{msg.MEMBER_SECONDARY_CONTACT_PHONE}}",}],"address":{"use": "{{ p.KinAddress.type}}","line": "{{p.KinAddress.Street}}","city": "{{p.KinAddress.City}}","postalCode": "{{p.KinAddress.ZipCode}}",},{% endfor -%}}],'
    if "MEMBER_SECONDARY_CONTACT_PHONE" in trans_contact:
        print("MEMBER_SECONDARY_CONTACT_PHONE" in trans_contact)

    print("managingOrganization")
    trans_mangOrg = '"managingOrganization": {"reference": "Organization/{{msg.CLIENTID}}","display": "{{msg.CLIENTNAME}}"},'
    if "CLIENTID" in trans_mangOrg:
        print("CLIENTID" in trans_mangOrg)

    if "CLIENTNAME" in trans_mangOrg:
        print("CLIENTNAME" in trans_mangOrg)

    print("generalPractitioner")
    trans_pcp = '"generalPractitioner": [{"reference": "Practioner/{{msg.PCP_ID}}","display": "{{msg.PCP_FIRSTNAME}} {{msg.PCP_LASTNAME}}"},],"extension":[{"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity","extension": [{"url": "text","valueString":"{{msg.ETHNICITY}}"}]}'
    if "PCP_ID" in trans_pcp:
        print("PCP_ID" in trans_pcp)

    if "PCP_FIRSTNAME" in trans_pcp:
        print("PCP_FIRSTNAME" in trans_pcp)

    if "PCP_LASTNAME" in trans_pcp:
        print("PCP_LASTNAME" in trans_pcp)

    if "ETHNICITY"in trans_pcp:
        print("ETHNICITY" in trans_pcp)

    print("communications")
    trans_comm = '"communication":[{"language":{"valueCodeableConcept":{"coding":[{"system":"http://hl7.org/fhir/ValueSet/languages","code": "en","display":"{{msg.PREFERREDSPOKENLANGUAGE}}",}],"text": "{{msg.PREFERREDSPOKENLANGUAGE}}"}}],'
    if "PREFERREDSPOKENLANGUAGE"in trans_comm:
        print("PREFERREDSPOKENLANGUAGE" in trans_comm)

            '"qualification": [{"identifier": [{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0360","code": "MD","display" : "Doctor of Medicine"}]"value": "{{ msg.PROVIDER_QUALIFICATION}}"},],}],}

if __name__ == '__main__':
    unittest.main()