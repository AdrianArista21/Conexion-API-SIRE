import os
import io
import sys
import time
import json
import zipfile
import requests
from pathlib import Path
from datetime import datetime

DEFAULT_DOWNLOAD_DIRECTORY = "C:\\Sire\\{razon_social}\\{tipo_libro}\\{periodo}"
def create_download_route(razon_social, codLibro, perTributario):
    if codLibro == "140000":
        tipo_libro = "Ventas"
    if codLibro == "080000":
        tipo_libro = "Compras"

    return DEFAULT_DOWNLOAD_DIRECTORY.format(razon_social=razon_social,tipo_libro = tipo_libro,periodo=perTributario[:4] + "-" + perTributario[4:])

PROPOSAL_FILE_NAME = "{ruc}-{periodo}-{tipo_libro}-{num_ticket}.txt"
def get_proposal_file_name(ruc, periodo, tipo_libro, num_ticket):
    return  PROPOSAL_FILE_NAME.format(ruc=ruc, periodo=periodo, tipo_libro=tipo_libro, num_ticket=num_ticket)

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).resolve().parent
    else:
        return Path(__file__).resolve().parent.parent
BASE_PATH = get_base_path()

#General constants
MAX_ATEMPTS = 10 #to renew the token
MAX_DOWNLOAD_ATTEMPTS = 8
INITIAL_WAIT_TIME = 30 #In seconds
WAIT_TIME_INCREMENT = 30 #In seconds
MAX_WAIT_TIME = 1200 #In seconds
TOKEN_FILE = "token.json"
TOKEN_PATH = BASE_PATH / TOKEN_FILE
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
INVALID_TOKEN_ERROR_CODE = 401
NON_CRITIAL_ERROR_CODES = [408, 429, 500, 502, 503, 504]




#Parameters for URLs and headers
#For the token
TOKEN_BASE_URL = "https://api-seguridad.sunat.gob.pe/v1/clientessol/{client_id}/oauth2/token/"
GRANT_TYPE = "password"
TOKEN_CONTENT_TYPE = "application/x-www-form-urlencoded"
SCOPE = "https://api-sire.sunat.gob.pe"


#For the ticket
TICKET_BASE_URL = "https://api-sire.sunat.gob.pe/v1/contribuyente/migeigv/libros/{tipo_comprobante}/propuesta/web/propuesta/{perTributario}/{end_url}?"
TICKET_RCE_END_URL = "exportacioncomprobantepropuesta"
TICKET_RVIE_END_URL = "exportapropuesta"
TICKET_STATE_BASE_URL = "https://api-sire.sunat.gob.pe/v1/contribuyente/migeigv/libros/rvierce/gestionprocesosmasivos/web/masivo/consultaestadotickets?"
TICKET_CONTENT_TYPE = "application/json"
TICKET_ACCEPT = "application/json"

#For the proposal download
PROPOSAL_DOWNLOAD_BASE_URL = "https://api-sire.sunat.gob.pe/v1/contribuyente/migeigv/libros/rvierce/gestionprocesosmasivos/web/masivo/archivoreporte?"
DOWNLOAD_CONTENT_TYPE = "application/json"
DOWNLOAD_ACCEPT = "application/json"

#Validation codes
VALID_STATE_CODES = ["03","04","06"]
PROC_WITH_ERRORS_CODE = "03"
PROC_WITHOUT_ERRORS_CODE = "04"
FINISHED_CODE = "03"



