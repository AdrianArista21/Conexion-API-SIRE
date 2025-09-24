import requests

from api_sire.config import *

class Token:
    def __init__(self, ruc = None, username = None, password = None, client_id = None, client_secret = None):
        self.url_base = TOKEN_BASE_URL
        self.ruc = ruc
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

    def generate_url(self):
        if(self.ruc == None or self.username == None or self.password == None or self.client_id == None or self.client_secret == None):
            print("Error en los parámetros al crear la url para obtener el token")
            exit(1)
        return TOKEN_BASE_URL.format(client_id = self.client_id)

    @staticmethod
    def get_headers():
        headers = {
            "Content-Type": TOKEN_CONTENT_TYPE
        }
        return headers

    def get_body(self):
        user = self.ruc + self.username
        body = {
            "grant_type": GRANT_TYPE,
            "scope": SCOPE,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": user,
            "password": self.password,
        }
        return body

    # Servicio 5.1
    def get_token(self):
        try:
            response = requests.post(self.generate_url(), headers=self.get_headers(), data=self.get_body())
            response.raise_for_status()

            return {
                "success": response.ok,
                "status_code": response.status_code,
                "error_msg": response.reason,
                "data": response.json(),
            }
        except requests.RequestException as e:
            return {
                "success": False,
                "status_code": getattr(e.response, "status_code", None),
                "error_msg": getattr(e.response, "reason", None),
                "data": None,
            }
'''        
    def validate_saved_token(self):
        route = Path(TOKEN_PATH)
        need_new_token = False

        if not route.exists():
            need_new_token = True
        else:
            token_data = self.read_token_data()
            need_new_token = (not token_data["success"] or int(token_data["data"]["date_diff"]) >= int(token_data["data"]["expires_in"]))

        if need_new_token:
            token_data = self.get_save_token()

        return token_data

    def get_save_token(self):
        response = self.get_token()
        if response["success"] == True:
            data = response["data"]
            data["generated_at"] = datetime.now().strftime(DATE_FORMAT)
            with open(TOKEN_PATH, "w") as file:
                json.dump(data, file)
            print("Se ha generado un nuevo token")

        return response

    @staticmethod
    def read_token_data():
        with open(TOKEN_PATH, "r") as file:
            token_data = json.load(file)

        if not token_data:
            return {
                "success": False,
                "status_code": 500,
                "data": "Error en la lectura del token",
            }
        else:
            saved_date = datetime.strptime(token_data["generated_at"], DATE_FORMAT)
            date_diff = int(datetime.now().timestamp()) - int(saved_date.timestamp())
            token_data["date_diff"] = date_diff
            return {
                "success": True,
                "status_code": 200,
                "data": token_data,
            }
'''