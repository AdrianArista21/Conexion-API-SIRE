from api_sire.Sire_Services_Handlers import Sire_Services_Handlers
from api_sire.Token_Service import Token
from api_sire.Ticket_Service import Ticket
from api_sire.Ticket_Service import TicketState
from api_sire.Proposal_Download_Service import ProposalDownload
from api_sire.config import *

class Sire_Services:
    def __init__(self):
        self.handlers = Sire_Services_Handlers()

    #Servicio
    def proposal_download(self, razon_social, ruc, username, password, client_id, client_secret, perTributario, codTipoArchivo, perIni, perFin, page, perPage, codLibro, codOrigenEnvío, download_directory = None):
        token_ = Token(ruc, username, password, client_id, client_secret)
        print("Generando token...")
        access_token = self.handlers.sire_service_token_handler(token_)
        if access_token is None: return False

        ticket_ = Ticket(perTributario,codTipoArchivo, codLibro, codOrigenEnvío)
        print("Generando ticket...")
        ticket_number = self.handlers.sire_service_ticket_handler(access_token, ticket_, token_)
        if ticket_number is None: return False
        print("Consultando estado de ticket", end="")
        ticket_state_ = TicketState(perIni, perFin, page, perPage, codLibro, codOrigenEnvío)

        download_result = self.handlers.ticket_state_check_loop(ruc, access_token, codLibro,ticket_number, razon_social,token_, ticket_state_, download_directory)
        if download_result is None: return False

        return True