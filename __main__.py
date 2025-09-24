from api_sire.Sire_Services import Sire_Services
from api_sire.config import *

def main(razon_social, ruc, username, password, client_id, client_secret, perTributario, codTipoArchivo, perIni, perFin, page, perPage, codLibro, codOrigenEnvío, download_directory = None):

    print("===== Iniciando aplicación =====")
    print("Utilizando credenciales:")
    print("Razon Social:", razon_social)
    print("Ruc:", ruc)
    print("Username:", username)
    print("Password:", password)
    print("Client ID:", client_id)
    print("Client Secret:", client_secret)
    if download_directory is None:
        download_directory = Path(create_download_route(razon_social,codLibro,perTributario))
    services = Sire_Services()
    res = services.proposal_download(razon_social, ruc, username, password, client_id, client_secret, perTributario, codTipoArchivo, perIni, perFin, page, perPage, codLibro, codOrigenEnvío, download_directory)
    if res is True:
        print("\nDescarga exitosa en ", download_directory)
    else:
        print("\nError en la descarga")


if __name__ == "__main__":
    main(*sys.argv[1:])