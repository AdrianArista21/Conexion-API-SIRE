
# Web Scraper de Tipo de Cambio (Perú) 

Implementación basada en:

    1. Manual de Usuario del Sistema Integrado Registro Electrónico-SIRE Compras v26
    (https://cpe.sunat.gob.pe/sites/default/files/inline-files/Manual%20de%20servicios%20Web%20Api%20-%20SIRE_Compras%20v26_0.pdf) 
    2. Manual de Usuario del Sistema Integrado Registro Electrónico-SIRE Ventas v25 
    (https://cpe.sunat.gob.pe/sites/default/files/inline-files/Manual%20de%20servicios%20Web%20Api%20-%20SIRE_Ventas%20v25.pdf)

El archivo .bat incluye todos los parámetros obligatorios para el funcionamiento de la descarga de la propuesta de la SUNAT para la empresa Diproxer SAC, del
periodo 2025-05 en formato .txt. La propuesta se descarga en la carpeta C:\\Sire\\Diproxer S.A.C.\\Compras\\2025-06, el árbol de carpetas se crea automáticamente
en caso de que todavía no exista. Es necesario ajustar la ruta absoluta del ejecutable __main__.exe para poder ejecutar el .bat. Para la correcta ejecución de 
la aplicación el archivo __main__.exe debe estar dentro de su respectiva carpeta "dist" siempre.

#Servicios

Hasta el momento implementa los siguientes servicios:

    1. Servicio API Seguridad......................................(Sección 5.1 del manual de compras, Sección 5.1 del manual de ventas)
    2. Servicio Web API Descargar Propuesta........................(Sección 5.34 del manual de compras, Sección 5.18 del manual de ventas)
    3. Servicio Web Api Consultar Estado de Envío de Ticket........(Sección 5.31 del manual de compras, Sección 5.16 del manual de ventas)
    4. Servicio Web Api Descargar Archivo..........................(Sección 5.32 del manual de compras, Sección 5.17 del manual de ventas)

# Parámetros

Los parámetros que recibe la aplicación son los siguientes, se recomienda utilizar los valores predeterminados cuando se mencionan:

    1. razon_social
    2. ruc
    3. clave_sol (o contraseña)
    4. client_id
    5. client_secret
    6. periodo_tributario 		#Periodo del que se va a solicitar la descarga, 
                                el año y el mes van juntos (ej. "202506")
    7. tipo_archivo 		    #Tipo de archivo a descargar "0": txt, "1": csv. El contenido 
                                del txt tiene los valores separados por el caracter "|"
    8. periodo_inicio   		#La aplicación todavía no soporta la descarga de varios     
                                periodos, este parámetro debe tener el mismo valor que  
                                periodo_tributario 
    9. periodo_fin			    #La aplicación todavía no soporta la descarga de varios 
                                periodos, este parámetro debe tener el mismo valor que 
                                periodo_tributario
    10. page			        #Indica que página de los registros generados se va a 
                                descargar, valor predeterminado: "1"
    11. per_page			    #Indica la cantidad de registros por cada página, valor 
                                predeterminado: "1"
    12. codigo_libro		    #Indica si se va a descargar la propuesta del libro de compras o ventas. 
                                "140000" para ventas, "080000" para compras
    13. codigo_origen_envio		#Origen de la propuesta. Valor predeterminado "2", origen web.
    14. directorio_descarga		#Parámetro opcional, indica una ruta de descarga personalizada. 
                                En caso de estar vacío la aplicación utiliza una ruta predeterminada
                                (C:\\Sire\\razon_social\\tipo_libro\\periodo\\archivo_descargado)

    