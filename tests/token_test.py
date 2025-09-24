from api_sire.Token_Service import Token
from api_sire.Sire_Services_Handlers import SIRE_services

RUC = "20258007370"
USERNAME = "N2ABXDSL"
PASS = "DIPROXER"
ID = "f4d8d782-ea0f-42f1-8c1b-49db4990092c"
SECRET = "V66zZIJwR1bFcB4TX5cN9g=="

service = SIRE_services()
token = Token(RUC, USERNAME, PASS, ID, SECRET)
token_ = service.API_service_token_handler(token)
print(token_)