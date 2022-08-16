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

auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL3NieC11c2MtZmhpci1hcGkuYXp1cmVoZWFsdGhjYXJlYXBpcy5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80YWQ4YWIxMy0yODU0LTRiOWEtYTc3MC1hZWNhYzk1OGRmNWYvIiwiaWF0IjoxNjYwMTU5MzMwLCJuYmYiOjE2NjAxNTkzMzAsImV4cCI6MTY2MDE2NDg4NSwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQTAvdUo5N2xPbTdyMTRrYnppTDN1Y053Q3VKdlNqZ0hGRSt2YUl6QzFhdTJkb0d3MU1FcjNCOHJDSzJoWWhyYmJQQXZPQXNUbG9hQ0VMK0hQMEJYTlk3WFBEQjExeTJzdnU4aE9UYkE0NURrPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwaWQiOiJkYjhmMjYxYS0zNjY1LTRlMTUtYmUwNC01NDZhMjAxMzJlYjAiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlJvc2FyaW8iLCJnaXZlbl9uYW1lIjoiQW5kcmVhIiwiaXBhZGRyIjoiNzEuNDcuMjQ4Ljk0IiwibmFtZSI6IkFuZHJlYSBSb3NhcmlvIiwib2lkIjoiMTNiOTgwMTUtMWJmMi00M2NmLWFhMDItNDYxYWRjNGE3ZDM4Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTM2NDU1MjEwMDctNDE2NDcxMTU5Ni0xMjk2NjczMDAtNDM1MzQiLCJwdWlkIjoiMTAwMzIwMDFGREVFQkJCRiIsInJoIjoiMC5BUnNBRTZ2WVNsUW9ta3VuY0s3S3lWamZYOWg0WjBfdld0eERvZi13YzNKTGxKVWJBS2suIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiR1cyQ3BCclc4bDE4WkFyZDN0aG14UDRzaTgxU1ljcElHaThVTVNiOUFXcyIsInRpZCI6IjRhZDhhYjEzLTI4NTQtNGI5YS1hNzcwLWFlY2FjOTU4ZGY1ZiIsInVuaXF1ZV9uYW1lIjoiYW5yb3NhcmlvQHNpZ25pZnloZWFsdGguY29tIiwidXBuIjoiYW5yb3NhcmlvQHNpZ25pZnloZWFsdGguY29tIiwidXRpIjoidW54YUdaMkkwa20tVzNXem9GV1dBQSIsInZlciI6IjEuMCJ9.Lre5O61xZ5MwqRUOw-oiym1bFSP5Cv42gRhvsdW4KYEVteb7s0XCBQ8WgtgDLmJiPs1mb9dvg_Cl6xge_IjyV_lE_nmQws23jKWmxFMCX6dWViypPLSvCfG3EkPMOty1xT5KVSHlbFRQnTSesCq2xVDvTeZJUeiRSLEEll3hIZGzjhUJgWtl5-aXBs1uR3ZUfpLO-AZxO2754bs_SnlklcVLXwBQ9B-VS6rvgyMrvKOyRw8nsAjGYBoOlrW6jkGlE9zhdKGf5zFuKGBy9zuSTYWz1SQJWubfDrkXoqnlsZr6lE3UUvBZz6OJclMiH3ezsx4zlA0FVlzVjwWZc18hNQ'