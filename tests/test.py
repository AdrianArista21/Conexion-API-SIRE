from api_sire.Token_Service import Token
from api_sire.Ticket_Service import Ticket
from api_sire.Ticket_Service import TicketState
from api_sire.Proposal_Download_Service import ProposalDownload
from api_sire.Sire_Services_Handlers import Sire_Services_Handlers
from api_sire.Sire_Services import Sire_Services
from api_sire.config import *

RAZON_SOCIAL = "Diproxer S.A.C."
RUC = "20258007370"
USERNAME = "N2ABXDSL"
PASS = "DIPROXER"
ID = "f4d8d782-ea0f-42f1-8c1b-49db4990092c"
SECRET = "V66zZIJwR1bFcB4TX5cN9g=="

PER_TRIBUTARIO = "202505"
COD_ARCHIVO = "0"

PER_INI = "202506"
PER_FIN = "202506"
PAGE = "1"
PER_PAGE = "20"
COD_LIBRO = "080000"
COD_ENVIO = "2"

def proposal_download_complete_test(razon_social, ruc, username, password, client_id, client_secret, perTributario, codTipoArchivo, perIni, perFin, page, perPage, codLibro, codOrigenEnvío, download_directory = None):
    servicios = Sire_Services()
    if download_directory is None:
        download_directory = Path(create_download_route(razon_social,codLibro,perTributario))
    resultado = servicios.proposal_download(razon_social, ruc, username, password, client_id, client_secret, perTributario, codTipoArchivo, perIni, perFin, page, perPage, codLibro, codOrigenEnvío, download_directory)
    if resultado:
        print("\nDescarga exitosa en ", download_directory)
    else:
        print("\nError en la descarga")

proposal_download_complete_test(RAZON_SOCIAL, RUC, USERNAME,PASS,ID, SECRET,PER_TRIBUTARIO,COD_ARCHIVO,PER_TRIBUTARIO,PER_TRIBUTARIO,PAGE, PER_PAGE,COD_LIBRO,COD_ENVIO)
