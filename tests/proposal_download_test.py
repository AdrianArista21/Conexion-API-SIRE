from api_sire.Sire_Services_Handlers import SIRE_services
from api_sire.Token_Service import Token
from api_sire.Proposal_Download_Service import ProposalDownload
from api_sire.config import *

RUC = "20258007370"
USERNAME = "N2ABXDSL"
PASS = "DIPROXER"
ID = "f4d8d782-ea0f-42f1-8c1b-49db4990092c"
SECRET = "V66zZIJwR1bFcB4TX5cN9g=="

TICKET_STATE =  {'paginacion': {'page': 1, 'perPage': 20, 'totalRegistros': 1}, 'registros': [{'showReporteDescarga': '1', 'perTributario': '202506', 'numTicket': '20250300000054', 'fecCargaImportacion': None, 'fecInicioProceso': '2025-08-15', 'codProceso': '10', 'desProceso': 'Generar archivo exportar propuesta', 'codEstadoProceso': '06', 'desEstadoProceso': 'Terminado', 'nomArchivoImportacion': None, 'detalleTicket': {'numTicket': '20250300000054', 'fecCargaImportacion': '2025-08-15', 'horaCargaImportacion': '13:23:00', 'codEstadoEnvio': '06', 'desEstadoEnvio': 'Terminado', 'nomArchivoReporte': None, 'cntFilasvalidada': 0, 'cntCPError': 0, 'cntCPInformados': 0}, 'archivoReporte': [{'codTipoAchivoReporte': '00', 'nomArchivoReporte': 'LE2025800737020250810014040001EXP2.zip', 'nomArchivoContenido': 'LE202580073702025080014040001EXP2.csv'}], 'subProcesos': [{'codTipoSubProceso': '', 'desTipoSubProceso': '', 'codEstado': '1', 'numIntentos': 1}]}]}
TOKEN_INVALIDO = "eyJraWQiOiJhcGkuc3VuYXQuZ29iLnBlLmtpZDAwMSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyMDI1ODAwNzM3MCIsImF1ZCI6Ilt7XCJhcGlcIjpcImh0dHBzOlwvXC9hcGktY3BlLnN1bmF0LmdvYi5wZVwiLFwicmVjdXJzb1wiOlt7XCJpZFwiOlwiXC92MVwvY29udHJpYnV5ZW50ZVwvY29udHJvbGNwZVwiLFwiaW5kaWNhZG9yXCI6XCIxXCIsXCJndFwiOlwiMTAwMDAwXCJ9LHtcImlkXCI6XCJcL3YxXC9jb250cmlidXllbnRlXC9nZW1cIixcImluZGljYWRvclwiOlwiMVwiLFwiZ3RcIjpcIjEwMDAwMFwifSx7XCJpZFwiOlwiXC92MVwvY29udHJpYnV5ZW50ZVwvY29udHJvbG1zZ1wiLFwiaW5kaWNhZG9yXCI6XCIxXCIsXCJndFwiOlwiMTAwMDAwXCJ9XX0se1wiYXBpXCI6XCJodHRwczpcL1wvYXBpLXNpcmUuc3VuYXQuZ29iLnBlXCIsXCJyZWN1cnNvXCI6W3tcImlkXCI6XCJcL3YxXC9jb250cmlidXllbnRlXC9taWdlaWd2XCIsXCJpbmRpY2Fkb3JcIjpcIjFcIixcImd0XCI6XCIxMDAwMDBcIn1dfV0iLCJ1c2VyZGF0YSI6eyJudW1SVUMiOiIyMDI1ODAwNzM3MCIsInRpY2tldCI6IjEyMjUxMjQwNDU2NDQiLCJucm9SZWdpc3RybyI6IiIsImFwZU1hdGVybm8iOiIiLCJsb2dpbiI6IjIwMjU4MDA3MzcwTjJBQlhEU0wiLCJub21icmVDb21wbGV0byI6IkRJUFJPWEVSIFMuQS5DIiwibm9tYnJlcyI6IkRJUFJPWEVSIFMuQS5DIiwiY29kRGVwZW5kIjoiMDAyMyIsImNvZFRPcGVDb21lciI6IiIsImNvZENhdGUiOiIiLCJuaXZlbFVPIjowLCJjb2RVTyI6IiIsImNvcnJlbyI6IiIsInVzdWFyaW9TT0wiOiJOMkFCWERTTCIsImlkIjoiIiwiZGVzVU8iOiIiLCJkZXNDYXRlIjoiIiwiYXBlUGF0ZXJubyI6IiIsImlkQ2VsdWxhciI6bnVsbCwibWFwIjp7ImlzQ2xvbiI6ZmFsc2UsImRkcERhdGEiOnsiZGRwX251bXJ1YyI6IjIwMjU4MDA3MzcwIiwiZGRwX251bXJlZyI6IjAwMjMiLCJkZHBfZXN0YWRvIjoiMDAiLCJkZHBfZmxhZzIyIjoiMDAiLCJkZHBfdWJpZ2VvIjoiMTUwMTE2IiwiZGRwX3RhbWFubyI6IjAyIiwiZGRwX3Rwb2VtcCI6IjM5IiwiZGRwX2NpaXUiOiI1MjM5MSJ9LCJpZE1lbnUiOiIxMjI1MTI0MDQ1NjQ0Iiwiam5kaVBvb2wiOiJwMDAyMyIsInRpcFVzdWFyaW8iOiIwIiwidGlwT3JpZ2VuIjoiSVQiLCJwcmltZXJBY2Nlc28iOmZhbHNlfX0sIm5iZiI6MTc1NTEwNjg0NSwiY2xpZW50SWQiOiJmNGQ4ZDc4Mi1lYTBmLTQyZjEtOGMxYi00OWRiNDk5MDA5MmMiLCJpc3MiOiJodHRwczpcL1wvYXBpLXNlZ3VyaWRhZC5zdW5hdC5nb2IucGVcL3YxXC9jbGllbnRlc3NvbFwvZjRkOGQ3ODItZWEwZi00MmYxLThjMWItNDlkYjQ5OTAwOTJjXC9vYXV0aDJcL3Rva2VuXC8iLCJleHAiOjE3NTUxMTA0NDUsImdyYW50VHlwZSI6InBhc3N3b3JkIiwiaWF0IjoxNzU1MTA2ODQ1fQ.b3arUMYhj5b3vzdLhG5Id3FyNsN7J5iDf8muhJOy1-MJPThYamP6ldgc_sZf03faJouCcvef1OKSK5Tk0CpIE3H1Fzl368hr9wdBRTmr6IqqmF-c9HtLP7SX2bK8RFaXXlAL-RWe8N4SOmWDep4T-l3MdwEth-1zmJi64ynnhiAJ9MfV3nYVI59YXw0lPfgu1OimsKnlLHYgTCfP4P3TYQz6jG_dq-hNE6R8Pslg7GSdkE2SpI9RPszqqd1-w4ZXj8U8nBeOThASTyHcPq47G8OQEr6eQ5H37IkryHzXXWW2NfixArwnOvYCcUaGedDwQZcS3bJhqMiwSiS1EDU_hQ"
TICKET_VALIDO1 = "20250300000054"
COD_LIBRO = "140000"
DOWNLOAD_DIRECTORY = "C:\\Users\\USER\\Desktop\\"

service = SIRE_services()
token_ = Token(RUC, USERNAME, PASS, ID, SECRET)

def invalid_token_test():
    si = 0
def invalid_ticket_test():
    si = 0
def no_download_directort_test():
    si = 0
def complete_test():
    ticket_state_json = TICKET_STATE


complete_test()