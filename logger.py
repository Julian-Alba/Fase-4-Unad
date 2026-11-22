# modulo pa guardar los eventos y errores del sistema en un archivo
# hecho por: Boris Julian Mateus Alba

import os
from datetime import datetime

ARCHIVO_LOG = "sistema_fj.log"


# escribe una linea en el log con la fecha y el nivel
def registrar_evento(mensaje, nivel="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] [{nivel}] {mensaje}\n"
    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
            f.write(linea)
    except IOError as e:
        # si no se puede escribir al menos lo muestro en consola
        print(f"No se pudo escribir en el log: {e}")


# pa registrar errores, con o sin detalle de la excepcion
def registrar_error(mensaje, excepcion=None):
    detalle = f" | Detalle: {str(excepcion)}" if excepcion else ""
    registrar_evento(f"ERROR - {mensaje}{detalle}", nivel="ERROR")


# pa registrar mensajes normales
def registrar_info(mensaje):
    registrar_evento(mensaje, nivel="INFO")


# pa registrar advertencias
def registrar_advertencia(mensaje):
    registrar_evento(mensaje, nivel="ADVERTENCIA")