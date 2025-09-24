from api_sire.config import *

class ProposalDownload:
    def __init__(self, nomArchivoReporte = None, codTipoArchivoReporte = None, codLibro = None, perTributario = None, codProceso = None, razon_social = None):
        self.base_url = PROPOSAL_DOWNLOAD_BASE_URL
        self.nomArchivoReporte = nomArchivoReporte
        self.codTipoArchivoReporte = codTipoArchivoReporte
        self.codLibro = codLibro
        self.perTributario = perTributario
        self.codProceso = codProceso
        self.razon_social = razon_social

    def get_parameters(self, ticket):
        param = {
            "nomArchivoReporte": self.nomArchivoReporte,
            "codTipoArchivoReporte": self.codTipoArchivoReporte,
            "codLibro": self.codLibro,
            "perTributario": self.perTributario,
            "codProceso": self.codProceso,
            "numTicket": ticket,
        }
        return param

    @staticmethod
    def get_headers(token):
        auth = "Bearer " + token
        header = {
            "Content-Type": DOWNLOAD_CONTENT_TYPE,
            "Accept": DOWNLOAD_ACCEPT,
            "Authorization": auth
        }
        return header

    #Servicio 5.17
    def get_download(self, ruc, token, ticket, download_directory=None):
        autorizacion = "Bearer " + token
        header = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": autorizacion}
        try:
            response = requests.get(self.base_url, params = self.get_parameters(ticket), headers = self.get_headers(token))
            response.raise_for_status()

            if response.status_code == 200:
                download_directory.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(io.BytesIO(response.content)) as file:
                    file.extractall(path = download_directory, members = file.namelist())
                for name in file.namelist():
                    file_name = Path(download_directory / name)
                os.rename(file_name.with_suffix(".txt"), download_directory / get_proposal_file_name(ruc, self.perTributario, self.codLibro, ticket))

            return {
                "success": True,
                "status_code": response.status_code,
                "error_msg": response.reason,
                "data": download_directory
            }
        except requests.RequestException as e:
            return {
                "success": False,
                "status_code": getattr(e.response, "status_code", None),
                "error_msg": getattr(e.response, "reason", None),
                "data": None,
            }
