# aca centralizo todas las excepciones del proyecto Software
# hecho por: Boris Julian Mateus Alba

# error cuando los datos del cliente estan mal
class ClienteInvalidoError(Exception):
    pass

# error cuando el servicio tiene algo raro o no esta disponible
class ServicioInvalidoError(Exception):
    pass

# error pa los problemas que pasan en el flujo de una reserva
class ReservaError(Exception):
    pass

# error cuando faltan datos que son obligatorios
class DatosFaltantesError(Exception):
    pass

# error cuando se intenta hacer algo que no esta permitido segun el estado
class OperacionNoPermitidaError(Exception):
    pass