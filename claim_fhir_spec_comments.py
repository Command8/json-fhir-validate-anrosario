
resource_type_info = 'from Resource= id, meta, implicitRules, and language from DomainResource: text, contained, extension, and modifierExtension'
identifier_info = 'active | cancelled | draft | entered-in-error'
type_info = '// R!  Category or discipline'
subType_info = '// More granular claim type'
use_info = '// R!  claim | preauthorization | predetermination'
patient_info = '// R!  The recipient of the products and services'
billablePeriod_info = '// Relevant time frame for the claim'
created_info = '// R!  Resource creation date'
entered_info = ' // Author of the claim'
insurer_info = '// Target'
provider_info = '// R!  Party responsible for the claim'
priority_info = 'CodeableConcept }, // R!  Desired processing ugency'
fundsReserve_info = '{ CodeableConcept }, // For whom to reserve funds'
related_info = '[{ // Prior or corollary claims'
relatedclaim_info = '{ Reference(Claim) }, // Reference to the related claim'
relatedrelationship_info = '{ CodeableConcept }, // How the reference claim is related'
relatedreference_info = '{ Identifier } // File or case reference'

prescription_info = '{ Reference(DeviceRequest|MedicationRequest|VisionPrescription }, // Prescription authorizing services and products'
originalPrescription_info = '{ Reference(DeviceRequest|MedicationRequest|VisionPrescription) }, // Original prescription if superseded by fulfiller'
prescript_payee_info = '{ // Recipient of benefits payable'
payee_type_info = '{ CodeableConcept }, // R!  Category of recipient'
payee_party_info = '{ Reference(Organization|Patient|Practitioner|PractitionerRole|RelatedPerson) } // Recipient reference'

referral_info = '{ Reference(ServiceRequest) }, // Treatment referral'
facility = '{ Reference(Location) }, // Servicing facility'

careTeam_info = '[{ // Members of the care team'
careTeam_sequence_info = '<positiveInt>, // R!  Order of care team'
careTeam_provider_info = '{ Reference(Organization|Practitioner|PractitionerRole) }, // R!  Practitioner or organization'
careTeam_responsible_info = '<boolean>, // Indicator of the lead practitioner'
careTeam_role_info = '{ CodeableConcept }, // Function within the team'
careTeam_qualification_info = '{ CodeableConcept } // Practitioner credential or specialization'

supportingInfo = '[{ // Supporting information'
supportingInfo_sequence_info = '<positiveInt>, // R!  Information instance identifier'
supportingInfo_category_info = '{ CodeableConcept }, // R!  Classification of the supplied information'
supportingInfo_code_info = '{ CodeableConcept }, // Type of information// timing[x]= When it occurred. One of these 2='
supportingInfo_timingDate_info = '<date>,'
supportingInfo_timingPeriod_info = '{ Period },// value[x]= Data to be provided. One of these 5='
supportingInfo_valueBoolean_info = '<boolean>,'
supportingInfo_valueString_info = '<string>,'
supportingInfo_valueQuantity_info = '{ Quantity },'
supportingInfo_valueAttachment_info = '{ Attachment },'
supportingInfo_valueReference_info = '{ Reference(Any) },'
supportingInfo_eason_info = '{ CodeableConcept } // Explanation for the information}]'

diagnosis_info = '[{ // Pertinent diagnosis information'
diagnosis_sequence_info = '"<positiveInt>", // R!  Diagnosis instance identifier// diagnosis[x]= Nature of illness or problem. One of these 2='
diagnosis_diagnosisCodeableConcept_info = '{ CodeableConcept },'
diagnosis_diagnosisReference_info = '{ Reference(Condition) },'
diagnosis_type_info = '[{ CodeableConcept }], // Timing or nature of the diagnosis'
diagnosis_onAdmission_info = '{ CodeableConcept }, // Present on admission'
diagnosis_packageCode_info = '{ CodeableConcept } // Package billing code}]'

procedure_info = '[{ // Clinical procedures performed'
procedure_sequence_info = '"<positiveInt>", // R!  Procedure instance identifier'
procedure_type_info = '[{ CodeableConcept }], // Category of Procedure'
procedure_date_info = '"<dateTime>", // When the procedure was performed// procedure[x]: Specific clinical procedure. One of these 2:'
procedureCodeableConcept_info = '{ CodeableConcept },'
procedureReference_info = '{ Reference(Procedure) },'
procedure_udi_info = '[{ Reference(Device) }] // Unique device identifier}],'

insurance_info = '[{ // R!  Patient insurance information'
insurance_sequence_info = '"<positiveInt>", // R!  Insurance instance identifier'
insurance_focal_info = '<boolean>, // R!  Coverage to be used for adjudication'
insurance_identifier_info = '{ Identifier }, // Pre-assigned Claim number'
insurance_coverage_info = '{ Reference(Coverage) }, // R!  Insurance information'
insurance_businessArrangement_info = '"<string>", // Additional provider contract number'
insurance_preAuthRef_info = '["<string>"], // Prior authorization reference number'
insurance_claimResponse_info = '{ Reference(ClaimResponse) } // Adjudication results'

accident_info = '{ // Details of the event'
accident_date_info = '"<date>", // R!  When the incident occurred'
accident_type_info = '{ CodeableConcept }, // The nature of the accident // location[x]= Where the event occurred. One of these 2='
accident_locationAddress = '{ Address }'
accident_locationReference = '{ Reference(Location) }},'

item_info = '[{ // Product or service provided'
item_sequence_info = '"<positiveInt>", // R!  Item instance identifier'
item_careTeamSequence_info = '[<positiveInt>], // Applicable careTeam members'
item_diagnosisSequence_info = '[<positiveInt>], // Applicable diagnoses'
item_procedureSequence_info = '[<positiveInt>], // Applicable procedures'
item_informationSequence_info = '[<positiveInt>], // Applicable exception and supporting information'
item_revenue_info = '{ CodeableConcept }, // Revenue or cost center code'
item_category_info = '{ CodeableConcept }, // Benefit classification'
item_productOrService_info = '{ CodeableConcept }, // R!  Billing, service, product, or drug code'
item_modifier_info = '[{ CodeableConcept }], // Product or service billing modifiers'
item_programCode_info = '[{ CodeableConcept }], // Program the product or service is provided under// serviced[x]= Date or dates of service or product delivery. One of these 2='
item_servicedDate_info = '<date>,'
item_servicedPeriod_info = '{ Period },// location[x]= Place of service or where product was supplied. One of these 3='
item_locationCodeableConcept_info = '{ CodeableConcept },'
item_locationAddress_info = '{ Address },'
item_locationReference_info = '{ Reference(Location) },'
item_quantity_info = '{Quantity(SimpleQuantity) }, // Count of products or services'
item_unitPrice_info = '{ Money }, // Fee, charge or cost per item'
item_factor_info = '<decimal>, // Price scaling factor'
item_net_info = '{ Money }, // Total item cost'
item_udi_info = '[{ Reference(Device) }], // Unique device identifier'
item_bodySite_info = '{ CodeableConcept }, // Anatomical location'
item_subSite_info = '[{ CodeableConcept }], // Anatomical sub-location'
item_encounter_info = '[{ Reference(Encounter) }], // Encounters related to this billed item'
item_detail_info = '[{ // Product or service provided'
item_detail_sequence_info =' <positiveInt>, // R!  Item instance identifier'
item_detail_revenue_info = '{ CodeableConcept }, // Revenue or cost center code'
item_detail_category_info = '{ CodeableConcept }, // Benefit classification'
item_detail_productOrService_info = '{ CodeableConcept }, // R!  Billing, service, product, or drug code'
item_detail_modifier_info = '[{ CodeableConcept }], // Service/Product billing modifiers'
item_detail_programCode_info = '[{ CodeableConcept }], // Program the product or service is provided under'
item_detail_quantity_info = '{ Quantity(SimpleQuantity) }, // Count of products or services'
item_detail_unitPrice_info = '{ Money }, // Fee, charge or cost per item'
item_detail_factor_info = '<decimal>, // Price scaling factor'
item_detail_net_info = '{ Money }, // Total item cost'
item_detail_udi_info = '[{ Reference(Device) }], // Unique device identifier'
item_subDetail_info = '[{ // Product or service provided'
item_subDetail_sequence_info = '<positiveInt>, // R!  Item instance identifier'
item_subDetail_revenue_info = '{ CodeableConcept }, // Revenue or cost center code'
item_subDetail_category_info = '{ CodeableConcept }, // Benefit classification'
item_subDetail_productOrService_info = '{ CodeableConcept }, // R!  Billing, service, product, or drug code'
item_subDetail_modifier_info = '[{ CodeableConcept }], // Service/Product billing modifiers'
item_subDetail_programCode_info = '[{ CodeableConcept }], // Program the product or service is provided under'
item_subDetail_quantity_info = '{ Quantity(SimpleQuantity) }, // Count of products or services'
item_subDetail_unitPrice_info = '{ Money }, // Fee, charge or cost per item'
item_subDetail_factor_info = '<decimal>, // Price scaling factor'
item_subDetail_net_info = '{ Money }, // Total item cost'
item_subDetail_udi_info = '[{ Reference(Device) }] // Unique device identifier'
total_info = '{ Money } // Total claim cost'