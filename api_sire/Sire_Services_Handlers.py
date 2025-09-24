from api_sire.Token_Service import Token
from api_sire.Ticket_Service import Ticket
from api_sire.Ticket_Service import TicketState
from api_sire.Proposal_Download_Service import ProposalDownload
from api_sire.config import *


class Sire_Services_Handlers:
    def __init__(self):
        self.token = Token()
        self.ticket = Ticket()
        self.ticket_state = TicketState()
        self.proposal_download = ProposalDownload()

    def sire_service_token_handler(self, token_):
        self.token.__dict__.update(token_.__dict__)

        response = self.token.get_token()
        if not response or response["success"] == False:
            if response:
                print(f'Error {response["status_code"]} en la obtencion del token: {response["error_msg"]}')
            return None
        else:
            token_value = response["data"]["access_token"]
            return token_value

    def sire_service_ticket_handler(self, access_token, ticket_, token_):
        self.ticket.__dict__.update(ticket_.__dict__)

        response = self.sire_service_generic_loop_handler( self.ticket, "get_ticket", [access_token], token_)

        if response is None:
            return None
        else:
            return response["numTicket"]

    def sire_service_ticket_state_handler(self, access_token, numTicket, ticket_state_, token_):
        self.ticket_state.__dict__.update(ticket_state_.__dict__)

        response = self.sire_service_generic_loop_handler(self.ticket_state, "get_ticket_state", [access_token, numTicket], token_)

        if response is None:
            return None
        else:
            return response

    def sire_service_download_handler(self, ruc, access_token, numTicket, proposal_download_, token_, download_directory = None):
        self.proposal_download.__dict__.update(proposal_download_.__dict__)

        response = self.sire_service_generic_loop_handler(self.proposal_download,"get_download", [ruc, access_token, numTicket, download_directory], token_)
        if response is None:
            return None
        else:
            return response

    def sire_service_generic_loop_handler(self, object, method_name, method_args, token_):

        for attempt in range(MAX_ATEMPTS):
            method = getattr(object, method_name)
            response = method(*method_args)
            if  response is None: return None

            if not response["success"]:
                if response["status_code"] == INVALID_TOKEN_ERROR_CODE:
                    time.sleep(1)
                    new_token_response = self.sire_service_token_handler(token_)
                    if not new_token_response: return None
                    method_args[0] = new_token_response
                elif response["status_code"] in NON_CRITIAL_ERROR_CODES:
                    print(f"Advertencia {response["status_code"]}: {response['data']} — reintentando ({attempt + 1}/{MAX_ATEMPTS})")
                    time.sleep(WAIT_TIME_INCREMENT)
                    continue
                else:
                    print(
                        f"Error {response['status_code']} en la operacion {method_name}: {response['data']}")
                    return None
            else:
                return response["data"]

        print("Tiempo agotado para la operacion")
        return None

    def ticket_state_check_loop(self, ruc, access_token, codLibro, numTicket, razon_social, token_, ticket_state_, download_directory = None):
        download = ProposalDownload()

        start_time = time.time()
        current_interval = INITIAL_WAIT_TIME

        for attempt in range(MAX_DOWNLOAD_ATTEMPTS):

            ticket_state_json = self.sire_service_ticket_state_handler(access_token, numTicket, ticket_state_, token_)
            if not ticket_state_json: return None

            if "registros" not in ticket_state_json or not ticket_state_json["registros"]:
                print("Error en el formato de estado de ticket obtenido")
                return
            registers = ticket_state_json["registros"][0]
            state_code = registers.get("codEstadoProceso", "")

            if state_code in VALID_STATE_CODES:
                if "archivoReporte" not in registers or not registers["archivoReporte"]:
                    print("Error en el formato de estado de registro obtenido")
                    return

                download.nomArchivoReporte = registers["archivoReporte"][0]["nomArchivoReporte"]
                download.codTipoArchivoReporte = registers["archivoReporte"][0]["codTipoAchivoReporte"]
                download.codLibro = codLibro
                download.perTributario = registers["perTributario"]
                download.codProceso = registers["codProceso"]
                download.razon_social = razon_social
                ticket_num = registers["detalleTicket"]["numTicket"]

                download_response = self.sire_service_download_handler(ruc, access_token, ticket_num, download, token_,
                                                                         download_directory)
                if not download_response is None:
                    return download_response
                else:
                    return None

            print(".",  end="")
            time.sleep(current_interval)
            current_interval += WAIT_TIME_INCREMENT

        print("Tiempo agotado para la operacion")
        return None