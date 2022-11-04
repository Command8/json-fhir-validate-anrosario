#logic for getting a valid token at runtime
#*************************************************** 
import secrets

# THESE ARE NOT NECESSARY ONCE THE TOKEN IS GENERATED BUT WE MAY NEED THIS IN FUTURE TO GENERATE A TOKEN FROM THE SCRIPT
#tokenName =  'SBX-FHIR-TOKEN'
#callback_url = 'https://www/.getpostman.com/oauth2/callback'
#auth_url = ('https://login.microsoftonline.com/', tenantId, '/oauth2/?resource=https://' , fhirServerName ,'.azurehealthcareapis.com')
#authtoken_url = ('https://login.microsoftonline.com/', tenantId, '/oauth2/token')
#OAuth 2.0 - uses  Specify if you want to pass the auth details in the request URL or headers. - we seem to be passing authorization via request url


#**************************************************

tenantId = '4ad8ab13-2854-4b9a-a770-aecac958df5f'
fhirServerName = 'sbx-usc-fhir-api'
client_id = 'db8f261a-3665-4e15-be04-546a20132eb0'
fhir_base_url = 'https://sbx-usc-fhir-api.azurehealthcareapis.com/'

auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL3NieC11c2MtZmhpci1hcGkuYXp1cmVoZWFsdGhjYXJlYXBpcy5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80YWQ4YWIxMy0yODU0LTRiOWEtYTc3MC1hZWNhYzk1OGRmNWYvIiwiaWF0IjoxNjY3NTgyMTI1LCJuYmYiOjE2Njc1ODIxMjUsImV4cCI6MTY2NzU4NzI0MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQWI3VVArdC9aa3Jyb0tsOHo1NUFmeWc0Umo3dUgzVDNpbTRtVm0wekk0dDBpNjVQaS9XbU9DK1BVWHRDdnRPcURLNVNNbXI2bFhDVUZOaEdQTm5EcWxPNWlqb2svNFZQSjhXdjlFMGg3TnRBPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwaWQiOiJkYjhmMjYxYS0zNjY1LTRlMTUtYmUwNC01NDZhMjAxMzJlYjAiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlJvc2FyaW8iLCJnaXZlbl9uYW1lIjoiQW5kcmVhIiwiaXBhZGRyIjoiNzEuNDcuMjQ4Ljk0IiwibmFtZSI6IkFuZHJlYSBSb3NhcmlvIiwib2lkIjoiMTNiOTgwMTUtMWJmMi00M2NmLWFhMDItNDYxYWRjNGE3ZDM4Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTM2NDU1MjEwMDctNDE2NDcxMTU5Ni0xMjk2NjczMDAtNDM1MzQiLCJwdWlkIjoiMTAwMzIwMDFGREVFQkJCRiIsInJoIjoiMC5BUnNBRTZ2WVNsUW9ta3VuY0s3S3lWamZYOWg0WjBfdld0eERvZi13YzNKTGxKVWJBS2suIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiR1cyQ3BCclc4bDE4WkFyZDN0aG14UDRzaTgxU1ljcElHaThVTVNiOUFXcyIsInRpZCI6IjRhZDhhYjEzLTI4NTQtNGI5YS1hNzcwLWFlY2FjOTU4ZGY1ZiIsInVuaXF1ZV9uYW1lIjoiYW5yb3NhcmlvQHNpZ25pZnloZWFsdGguY29tIiwidXBuIjoiYW5yb3NhcmlvQHNpZ25pZnloZWFsdGguY29tIiwidXRpIjoiYlNjU2ZOd0RSVWlGU0JQUVpmaHRBQSIsInZlciI6IjEuMCJ9.Qsa0MiOk_YuLNAZ538y3V1gCsKXdcW46YRijXehvUT1XLcA-R7LgT2m3t6itmLRoN_GApMyHzGrGIOjzfGJI026YLnG63K0d2y9why9yeGLcPcfDu-DDwLfWB-lbTjr3rGumNG441pukyNMiNOsnv2d_txg9lrgkmHs84kXWo740Gva7kseGlnOL91W4YJpDyBXc2YqOeE9XVvY3cVCBJumxHqoh-FObodl666fwhk-RV7ry38JfejGHuquQfF3Ik0A_HDUnVfrhiqBfVv6cnmSViKrIdAnaGUW9DMKGRvXdY6keNsyQ6Aej2gXAbnPHG9GOU0-s_iu2pnu9uQMjeA'