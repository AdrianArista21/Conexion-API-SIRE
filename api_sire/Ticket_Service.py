from api_sire.config import *

class Ticket:
    def __init__(self, perTributario = None, codTipoArchivo = None, codLibro = None, codOrigenEnvio = None, mtoTotalDesde = None, mtoTotalHasta = None, fecDocumentoDesde = None, fecDocumentoHasta = None, numRucAdquiriente = None, numCarSunat = None, codTipoCDP = None, codTipoInconsistencia = None):
        self.base_url = TICKET_BASE_URL
        self.perTributario = perTributario
        self.codTipoArchivo = codTipoArchivo
        self.mtoTotalDesde = mtoTotalDesde
        self.mtoTotalHasta = mtoTotalHasta
        self.fecDocumentoDesde = fecDocumentoDesde
        self.fecDocumentoHasta = fecDocumentoHasta
        self.numRucAdquiriente = numRucAdquiriente
        self.numCarSunat = numCarSunat
        self.codTipoCDP = codTipoCDP
        self.codTipoInconsistencia = codTipoInconsistencia
        self.response = None
        self.error_code = None
        self.codLibro = codLibro
        self.codOrigenEnvio = codOrigenEnvio

    def get_url(self):
        if self.codLibro == "080000":
            return TICKET_BASE_URL.format(tipo_comprobante = "rce", perTributario = self.perTributario, end_url = TICKET_RCE_END_URL)
        if self.codLibro == "140000":
            return TICKET_BASE_URL.format(tipo_comprobante = "rvie", perTributario = self.perTributario, end_url = TICKET_RVIE_END_URL)

    def get_parameters(self):
        parametros = {
            "mtoTotalDesde": self.mtoTotalDesde,
            "mtoTotalHasta": self.mtoTotalHasta,
            "fecDocumentoDesde": self.fecDocumentoDesde,
            "fecDocumentoHasta": self.fecDocumentoHasta,
            "numRucAdquiriente": self.numRucAdquiriente,
            "numCarSunat": self.numCarSunat,
            "codTipoCDP": self.codTipoCDP,
            "codTipoInconsistencia": self.codTipoInconsistencia,
            "codTipoArchivo": self.codTipoArchivo,
        }
        if self.codLibro == "080000":
            parametros["codOrigenEnvio"] = self.codOrigenEnvio
        return parametros

    @staticmethod
    def get_headers(token):
        auth = "Bearer " + token
        header = {
            "Content-Type": TICKET_CONTENT_TYPE,
            "Accept": TICKET_ACCEPT,
            "Authorization": auth
        }
        return header

    # Servicio 5.18
    def get_ticket(self, token):
        try:
            response = requests.get(self.get_url(), params=self.get_parameters(), headers=self.get_headers(token))
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

class TicketState:
    def __init__(self, perIni = None, perFin = None, page = None, perPage = None, codLibro = None, codOrigenEnvio = None):
        self.base_url = TICKET_STATE_BASE_URL
        self.perIni = perIni
        self.perFin = perFin
        self.page = page
        self.perPage = perPage
        self.codLibro = codLibro
        self.codOrigenEnvio = codOrigenEnvio

    def get_parameters(self, numTicket):
        parameters = {
            "perIni": self.perIni,
            "perFin": self.perFin,
            "page": self.page,
            "perPage": self.perPage,
            "numTicket": numTicket,
            "codLibro": self.codLibro,
            "codOrigenEnvio": self.codOrigenEnvio
        }
        return parameters

    @staticmethod
    def get_headers(token):
        auth = "Bearer " + token
        header = {
            "Content-Type": TICKET_CONTENT_TYPE,
            "Accept": TICKET_ACCEPT,
            "Authorization": auth
        }
        return header

    # Servicio 5.16
    def get_ticket_state(self, token, numTicket):
        try:
            response = requests.get(self.base_url, params=self.get_parameters(numTicket), headers=self.get_headers(token))
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