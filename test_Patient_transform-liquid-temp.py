import json

print("resource_type")
trans_pat_resource = '"resourceType": "Patient","id": "{{ msg.PatientId | to_json_string | generate_uuid }}","identifier": [{"use": "usual","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "MR"},"value": "{{ msg.CENSEOID }}"}{"use": "usual","type": {"coding": [}"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "SS"}"value": "{{ msg.MEMBER_SSN }}"}],"active": true,"name": [{"family": "{{ msg.MEMBER_LAST_NAME }}","given": ["{{ msg.MEMBER_FIRST_NAME }}"],"suffix": ["{{ msg.SUFFIX }}"],}],'

if "CENSEOID" in trans_pat_resource:
    print ("CENSEOID" in trans_pat_resource)
if "MEMBER_SSN" in trans_pat_resource:
    print ("MEMBER_SSN" in trans_pat_resource)
if "MEMBER_LAST_NAME" in trans_pat_resource:
    print ("MEMBER_LAST_NAME" in trans_pat_resource)
if "MEMBER_FIRST_NAME" in trans_pat_resource:
    print ("MEMBER_FIRST_NAME" in trans_pat_resource)
if "SUFFIX" in trans_pat_resource:
    print ("SUFFIX" in trans_pat_resource)

print("telecom")
trans_telecom = '"telecom": [{"system": "home","value": "{{msg.}}",},{"system": "email","value": "{{msg.MEMBER_EMAIL}}",},'
if "MEMBER_CELL" in trans_telecom:
    print("MEMBER_CELL" in trans_telecom)
if "MEMBER_EMAIL" in trans_telecom:
    print("MEMBER_EMAIL" in trans_telecom)

print("gender")
trans_gender = '"gender":{% if msg.MEMBER_GENDER =="1" -%}"male",{% elsif msg.MEMBER_GENDER == "2" -%}"female",{% elsif msg.MEMBER_GENDER == "3" -%}"unknown",{% elsif code -%}"other",{% else %}"",{% endif -%}'
if "MEMBER_GENDER" in trans_gender:
    print("MEMBER_GENDER" in trans_gender)

print("dob")
trans_dob = '"birthDate": "{{ msg.MEMBER_DATE_OF_BIRTH  }}"'
if "MEMBER_DATE_OF_BIRTH" in trans_dob:
    print("MEMBER_DATE_OF_BIRTH" in trans_dob)

print("deceasedBoolean")
trans_deceased = '"deceasedBoolean": "{{msg.DeceasedBoolean}}"'
if 'DeceasedBoolean' in trans_deceased:
    print("DeceasedBoolean" in trans_deceased)

print("address")
trans_address = '"address": [{"use": "home","line": "{{msg.MEMBER_ADDRESS1}}, {{msg.MEMBER_ADDRESS2}}","city": "{{msg.MEMBER_CITY}}","state":"{{msg.MEMBER_STATE}}","postalCode": "{{msg.MEMBER_ZIP}}","district": "{{msg.MEMBER_COUNTY}}","country": "USA",},{"use": "work","line": "{{msg.MEMBER_MAIL_ADDRESS1}}, {{msg.MEMBER_MAIL_ADDRESS2}}","city": "{{msg.MEMBER_MAIL_CITY}}","state":"{{msg.MEMBER_MAIL_STATE}}","postalCode": "{{msg.MEMBER_MAIL_ZIP}}"},],'
if "MEMBER_ADDRESS1" in trans_address:
    print("MEMBER_ADDRESS1" in trans_address)

if "MEMBER_ADDRESS2" in trans_address:
    print("MEMBER_ADDRESS2" in trans_address)

if "MEMBER_CITY"in trans_address:
    print("MEMBER_CITY" in trans_address)

if "MEMBER_COUNTY" in trans_address:
    print("MEMBER_COUNTY" in trans_address)

if "MEMBER_STATE"in trans_address:
    print("MEMBER_STATE" in trans_address)

if "MEMBER_ZIP" in trans_address:
    print("MEMBER_ZIP" in trans_address)

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

