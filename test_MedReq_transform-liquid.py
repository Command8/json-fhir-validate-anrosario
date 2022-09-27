import unittest
import json

trans_medreq_resourceType = '{"resourceType": "MedicationRequest","id": "{{msg.id}}","text": {"status": "generated","div": "{{ msg.text.div | escape_special_chars }}"},"contained": [{"resourceType": "Medication","id": "{{msg.contained.id}}","code": {"coding": [{"system": "{{msg.code.coding.system}}","code": "{{msg.code.coding.code}}","display": "{{msg.code.coding.display}}"}]}],''
trans_medreq_identifier = '"identifier": [{"use": "{{msg.identifier.use}}","type": "{{msg.identifier.type}}","system": "{{msg.identifier.system}}","value": "{{msg.CENSEOID}}","period": "{{msg.identifier.period}}","assigner": {"display": "SignifyHealth"},}],{% if msg.DATE_OF_SERVICE == "" -%}"status": "inactive",{% else -%}"status": "active",{% endif -%},'
trans_medreq_statusReason = '"statusReason":{"coding": ["system": "http://hl7.org/fhir/ValueSet/medicationrequest-status-reason","code": "{{msg.statusReason.coding.code}}","display": "{{msg.statusReason.coding.display}}"},],},'
trans_medreq_intent = '"intent": "order",'
trans_medreq_category = '"category":[{"coding": [{"system": "http://hl7.org/fhir/ValueSet/medicationrequest-category","code": "{{msg.category.coding.code}}","display": "{{msg.category.coding.display}}"},],}],'
trans_medreq_priority = '"priority": "{{msg.priority}}",'
trans_medreq_doNotPerform = '"doNotPerform": "{{msg.doNotPerform}}",'
trans_medreq_reportedBoolean =  '"reportedBoolean": "{{msg.reportedBoolean}}",'
trans_medreq_reportReference =   '"reportedReference":{"reference": "Practitioner/{{msg.reportedReference.reference}}","display": "{{msg.reportedReference.display}}"},'
trans_medreq_medicationCodableConcept = '"medicationCodeableConcept": {"coding": [{% for code in msg.NDC_CODE -%}{% for desc in msg.NDC_DESCRIPTION -%}{"system": "http://hl7.org/fhir/sid/ndc","code": "{{code}}","display": "{{desc}}"},{% endfor -%}{% endfor -%}],},'
trans_medreq_medicationReference ="medicationReference": {"reference": "Medication/{{msg.medicationReference.reference}}","display": "{{msg.medicationReference.display}}"},
trans_medreq_subject = '"subject": {"reference": "Patient/{{msg.subject.reference}}","display": "{{msg.subject.display}}"},'
trans_medreq_encounter = '"encounter": {"reference": "Encounter/{{msg.encounter.reference}}","display": "{{msg.encounter.display}}"},'
trans_medreq_supportingInfo = '"supportingInformation": {"reference": "Resource/{{msg.supportingInformation.reference}}","display": "{{msg.supportingInformation.display}}"},'
trans_medreq_authoredOn = '"authoredOn": "{{msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}","requester": {"reference": "Practitioner/{{msg.requester.reference}}","display": "{{msg.requester.display}}"},'
trans_medreq_performer = '"performer": {"reference": "Practitioner/{{msg.performer.reference}}","display": "{{msg.performer.display}}"},'
trans_medreq_performerType = '"performerType": {"coding": ["system": "http://hl7.org/fhir/ValueSet/performer-role","code": "{{msg.performerType.coding.code}}","display": "{{msg.performerType.coding.display}}"},],},'
trans_medreq_recorder =  '"recorder": {"reference": "Practitioner/{{msg.recorder.reference}}","display": "{{msg.recorder.display}}"},'
trans_medreq_reasonCode = '"reasonCode": [{"coding": [{"system": "http://hl7.org/fhir/ValueSet/condition-code","code": "{{msg.reasonCode.coding.code}}","display": "{{msg.reasonCode.coding.display}}"},],}],'
  "reasonReference": {
    "reference": "Condition/{{msg.reasonReference.reference}}",
    "display": "{{msg.reasonReference.display}}"
  },
  "instantiatesCanonical":[
    {
      "value": "{{msg.instantiatesCanonical.value}}"
    }
  ],
  "instantiatesUri":[
    {
      "uri": "{{msg.instantiatesUri.uri}}"
    }
  ],
  "basedOn": [
    {
      "reference": "MedicationRequest/{{msg.basedOn.reference}}"
    }
  ],
  "groupIdentifier": {
      "use": "{{msg.groupIdentifier.use}}",
      "system": "{{msg.groupIdentifier.system}}",
      "value": "{{msg.groupIdentifier.value}}"
  },
  "courseOfTherapyType": {
      "coding": [
        {
          "system": "http://hl7.org/fhir/ValueSet/medicationrequest-course-of-therapy",
          "code": "{{msg.courseOfTherapyType.coding.code}}",
          "display": "{{msg.courseOfTherapyType.coding.display}}"
        }
      ],
  },
  "insurance": [
    {
      "reference": "Coverage/{{msg.insurance.reference}}"
    }
  ],
  "note": [
    {
      "text": "{{msg.note.text}}"
    }
  ],
  "dosageInstruction": [
      {
        "sequence": 1,
        "text": "{{msg.dosageInstruction.text}}",
        "timing": {
          "repeat": {
            "frequency": "{{msg.dosageInstruction.timing.repeat.frequency}}",
            "period": "{{msg.dosageInstruction.timing.repeat.period}}",
            "periodUnit": "{{msg.dosageInstruction.timing.repeat.periodUnit}}"
          },
        },
        "doseAndRate": [
          {
            "type": {
              "coding": [
                {
                  "system": "{{msg.dosageInstruction.doseAndRate.type.coding.system}}",
                  "code": "{{msg.dosageInstruction.doseAndRate.type.coding.code}}",
                  "display": "{{msg.dosageInstruction.doseAndRate.type.coding.display}}"
                }
              ],
            },
            "doseQuantity": {
              "value": {{msg.QUANTITY}},
              "unit": "{{msg.dosageInstruction.doseAndRate.doseQuantity.unit}}",
              "system": "{{msg.dosageInstruction.doseAndRate.doseQuantity.system}}",
              "code": "{{msg.dosageInstruction.doseAndRate.doseQuantity.code}}"
            }
          }
        ]
      },
  ],
  "dispenseRequest": {
     "initialFill": {
        "quantity": "{{msg.initialFill.quantity}}",
        "duration": "{{msg.initialFill.duration}}"
     },
     "dispenseInterval": "{{msg.dispenseInterval}}",
     {% for dr in msg.dispenseRequest -%}
      "validityPeriod": {
        "start": "{{dr.validityPeriod.start | date: "yyyy-MM-dd"}}",
        "end": "{{dr.validityPeriod.end | date: "yyyy-MM-dd"}}"
      },
      "numberOfRepeatsAllowed": {{dr.numberOfRepeatsAllowed}},
      "quantity": {
        "value": {{dr.quantity.value}},
        "unit": "{{dr.quantity.unit}}",
        "system": "{{dr.quantity.system}}",
        "code": "{{dr.quantity.code}}"
      },
      "expectedSupplyDuration": {
        "value": {{dr.expectedSupplyDuration.value}},
        "unit": "{{dr.expectedSupplyDuration.unit}}",
        "system": "{{dr.expectedSupplyDuration.system}}",
        "code": "{{dr.expectedSupplyDuration.code}}"
      }
    {% endfor -%}
  },
  "substitution": {
    "allowedBoolean" : "{{msg.substitution}}",
    "allowedCodeableConcept" : {
      "coding": [
          {
            "system": "http://terminology.hl7.org/ValueSet/v3-ActSubstanceAdminSubstitutionCode",
            "code": "{{msg.substitution.allowableCodeableConcept.coding.code}}",
            "display": "{{msg.substitution.allowableCodeableConcept.coding.display}}"
          }
      ],
    },
    "reason": {
      "coding": [
          {
            "system": "http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason",
            "code": "{{msg.reason.coding.code}}",
            "display": "{{msg.reason.coding.display}}"
          }
      ],
    }
  },
  "priorPrescription": {
    "reference": "Condition/{{msg.priorPrescription.reference}}",
    "display": "{{msg.priorPrescription.display}}"
  },
  "detectedIssue": {
    "reference": "Condition/{{msg.detectedIssue.reference}}",
    "display": "{{msg.detectedIssue.display}}"
  },
  "eventHistory": {
    "reference": "Provenance/{{msg.eventHistory.reference}}",
    "display": "{{msg.eventHistory.display}}"
  },
}

class TestliqTransform (unittest.TestCase):
    def test_liqclmsnum(self):
        print("identifier.value = ClaimNumber exists:")
        #Validating key ClaimNumber in liquid template
        if ("ClaimNumber" in trans_claims_resource) == True:
            print ("ClaimNumber exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ClaimNumber" in trans_claims_resource,True,"ClaimNumber not present in liquid template") 

    def test_liqclmsstatus(self):
        print("status = active exists:")
        #Validating key claim in liquid template
        if "active" in trans_claims_status:
            print ("active exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("active" in trans_claims_status,True,"active not present in liquid template") 

    def test_liqclmsuse(self):
        print("use = claim exists:")
        #Validating key claim in liquid template
        if "claim" in trans_claims_use:
            print ("claim exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("claim" in trans_claims_use,True,"claim not present in liquid template") 

    def test_liqclmspatientid(self):
        print("patient.reference = CenseoID exists:")
        #Validating key CenseoID in liquid template
        if "CenseoID" in trans_claims_patient:
            print ("CenseoID exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("CenseoID" in trans_claims_patient,True,"CenseoID not present in liquid template") 


    def test_liqclmsbp1(self):
        print("billablePeriod.start = ServiceFromDate_Date_of_Service exists:")
        #Validating key ServiceFromDate_Date_of_Service in liquid template
        if "ServiceFromDate_Date_of_Service" in trans_claims_billablePeriod:
            print ("ServiceFromDate_Date_of_Service exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate_Date_of_Service" in trans_claims_billablePeriod,True,"ServiceFromDate_Date_of_Service not present in liquid template") 

    def test_liqclmsbp2(self):
        print("billablePeriod.end = ServiceThruDate exists:")
        #Validating key ServiceThruDate in liquid template
        if ("ServiceThruDate" in trans_claims_billablePeriod) == True:
            print ("ServiceThruDate exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceThruDate" in trans_claims_billablePeriod,True,"ServiceThruDate not present in liquid template") 

    def test_liqclmscreated(self):
        print("created = ClaimEntryDate exists:")
        #Validating key ClaimEntryDate in liquid template
        if ("ClaimEntryDate" in trans_claims_created) == True:
            print ("ClaimEntryDate exists in liquid template" in trans_claims_created)
        #Prints message if the test fails for comparison    
        self.assertEqual("ClaimEntryDate" in trans_claims_created,True,"ClaimEntryDate not present in liquid template") 

    def test_liqclmenterer(self):
        print("enterer.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if ("Provider_ID" in trans_claims_enterer) == True:
            print ("Provider_ID exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_enterer,True,"Provider_ID not present in liquid template") 

    def test_liqclmsprvdr(self):
        print("provider.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if "Provider_ID" in trans_claims_provider:
            print ("Provider_ID" in trans_claims_provider)
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_provider,True,"Provider_ID not present in liquid template")             

    def test_liqclmspriority(self):
        print("priority.coding.code = normal exists:")
        #Validating key normal in liquid template
        if "normal" in trans_claims_priority:
            print ("normal" in trans_claims_priority)
        #Prints message if the test fails for comparison    
        self.assertEqual("normal" in trans_claims_priority,True,"normal not present in liquid template") 

    def test_liqclmsprscrpt(self):
        print("prescription.reference = MedicationID exists:")
        #Validating key MedicationID in liquid template
        if "MedicationID" in trans_claims_prescription:
            print ("MedicationID" in trans_claims_prescription)
        #Prints message if the test fails for comparison    
        self.assertEqual("MedicationID" in trans_claims_prescription,True,"MedicationID not present in liquid template") 

    def test_liqclmspayee1(self):
        print("payee.type.coding.code = provider exists:")
        #Validating key provider in liquid template
        if "provider" in trans_claims_payee:
            print ("provider" in trans_claims_payee)
        #Prints message if the test fails for comparison    
        self.assertEqual("provider" in trans_claims_payee,True,"provider not present in liquid template") 

    def test_liqclmspayee2(self):
        print("payee.type.coding.display = RenderingProviderNPI exists:")
        #Validating key RenderingProviderNPI in liquid template
        if "RenderingProviderNPI" in trans_claims_payee:
            print ("RenderingProviderNPI" in trans_claims_payee)
        #Prints message if the test fails for comparison    
        self.assertEqual("RenderingProviderNPI" in trans_claims_payee,True,"RenderingProviderNPI not present in liquid template") 

    def test_liqclmsfacility(self):
        print("facility.identifier.value = PlaceOfService exists:")
        #Validating key PlaceOfService in liquid template
        if "PlaceOfService" in trans_claims_facility:
            print ("PlaceOfService" in trans_claims_facility)
        #Prints message if the test fails for comparison    
        self.assertEqual("PlaceOfService" in trans_claims_facility,True,"PlaceOfService not present in liquid template") 

    
    def test_liqclmscareteam(self):
        print("careTeam.sequence.provider.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if "Provider_ID" in trans_claims_careTeam:
            print ("Provider_ID" in trans_claims_careTeam)
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_careTeam,True,"Provider_ID not present in liquid template") 

    def test_liqclmsdiagnosis1(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_1 exists:")
        #Validating key DX_1 in liquid template
        if "DX_1" in trans_claims_diagnosis:
            print ("DX_1" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_1" in trans_claims_diagnosis,True,"DX_1 not present in liquid template") 

    def test_liqclmsdiagnosis2(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_2 exists:")
        #Validating key DX_2 in liquid template
        if "DX_2" in trans_claims_diagnosis:
            print ("DX_2" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_2" in trans_claims_diagnosis,True,"DX_2 not present in liquid template") 

    def test_liqclmsdiagnosis3(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_3 exists:")
        #Validating key DX_2 in liquid template
        if "DX_3" in trans_claims_diagnosis:
            print ("DX_3" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_3" in trans_claims_diagnosis,True,"DX_2 not present in liquid template") 

    def test_liqclmsprocedure1(self):
        print("procedure.sequence.type.coding.code = primary exists:")
        #Validating key primary in liquid template
        if "primary" in trans_claim_procedure:
            print ("primary" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("primary" in trans_claim_procedure,True,"primary not present in liquid template") 

    def test_liqclmsprocedure2(self):
        print("procedure.date = ServiceFromDate exists:")
        #Validating key ServiceFromDate in liquid template
        if "ServiceFromDate" in trans_claim_procedure:
            print ("ServiceFromDate" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate" in trans_claim_procedure,True,"ServiceFromDate not present in liquid template")

    def test_liqclmsprocedure3(self):
        print("procedure.procedureCodeableConcept.coding.code = ProcedureCode exists:")
        #Validating key ProcedureCode in liquid template
        if "ProcedureCode" in trans_claim_procedure:
            print ("ProcedureCode" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ProcedureCode" in trans_claim_procedure,True,"ProcedureCode not present in liquid template")

    def test_liqclmsprocedure4(self):
        print("procedure.sequence.type.coding.code = secondary exists:")
        #Validating key secondary in liquid template
        if "secondary" in trans_claim_procedure:
            print ("secondary" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("secondary" in trans_claim_procedure,True,"secondary not present in liquid template") 

    def test_liqclmsprocedure5(self):
        print("procedure.date = ServiceFromDate exists:")
        #Validating key ServiceFromDate in liquid template
        if "ServiceFromDate" in trans_claim_procedure:
            print ("ServiceFromDate" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate" in trans_claim_procedure,True,"ServiceFromDate not present in liquid template")
    
    def test_liqclmsprocedure6(self):
        print("procedure.procedureCodeableConcept.coding.code = ProcedureCode2 exists:")
        #Validating key ProcedureCode2 in liquid template
        if "ProcedureCode2" in trans_claim_procedure:
            print ("ProcedureCode2" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ProcedureCode2" in trans_claim_procedure,True,"ProcedureCode2 not present in liquid template")

    def test_liqclmsinsurance1(self):
        print("insurance.sequence = 1 exists:")
        #Validating key 1 in liquid template
        if "1" in trans_claims_insure:
            print ("1" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("1" in trans_claims_insure,True,"1 not present in liquid template")

    def test_liqclmsinsurance2(self):
        print("insurance.focal = true exists:")
        #Validating key true in liquid template
        if "true" in trans_claims_insure:
            print ("true" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("true" in trans_claims_insure,True,"true not present in liquid template")

    def test_liqclmsinsurance3(self):
        print("insurance.coverage.reference = CoverageID exists:")
        #Validating key CoverageID in liquid template
        if "CoverageID" in trans_claims_insure:
            print ("CoverageID" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("CoverageID" in trans_claims_insure,True,"CoverageID not present in liquid template")

    def test_liqclmstotal(self):
        print("insurance.total.value = BillAmount exists:")
        #Validating key BillAmount in liquid template
        if "BillAmount" in trans_claims_total:
            print ("BillAmount" in trans_claims_total)
        #Prints message if the test fails for comparison    
        self.assertEqual("BillAmount" in trans_claims_total,True,"BillAmount not present in liquid template")       

if __name__ == '__main__':
    unittest.main()