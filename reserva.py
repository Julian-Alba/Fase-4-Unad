# clase que conecta el cliente con el servicio y maneja todo el flujo
# hecho por: Boris Julian Mateus Alba

from datetime import datetime
from Estructura_clases import EntidadBase


# excepcion pa los errores de reserva
class ReservaError(Exception):
    pass


# los 4 estados que puede tener una reserva
ESTADO_PENDIENTE  = "pendiente"
ESTADO_CONFIRMADA = "confirmada"
ESTADO_CANCELADA  = "cancelada"
ESTADO_PROCESADA  = "procesada"


class Reserva(EntidadBase):

    def __init__(self, id_reserva, cliente, servicio, horas):
        super().__init__(id_reserva)
        self.__cliente     = cliente
        self.__servicio    = servicio
        self.__horas       = horas
        self.__estado      = ESTADO_PENDIENTE  # arranca siempre en pendiente
        self.__costo_total = 0.0
        self.__fecha_proceso = None  # se llena cuando se procesa

    @property
    def estado(self):
        return self.__estado

    @property
    def costo_total(self):
        return self.__costo_total

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    def confirmar(self):
        # solo se puede confirmar si esta pendiente, si no toca error
        if self.__estado != ESTADO_PENDIENTE:
            raise ReservaError(
                f"No se puede confirmar una reserva en estado '{self.__estado}'"
            )
        try:
            # le pregunto al servicio si las horas estan bien
            self.__servicio.validar_parametros(self.__horas)
            self.__estado = ESTADO_CONFIRMADA
            print(f"  ✔ Reserva {self.id} confirmada")
        except Exception as e:
            # encadeno el error pa no perder lo que paso
            raise ReservaError(f"Error al confirmar reserva {self.id}") from e

    def cancelar(self):
        # no se puede cancelar si ya se proceso o ya estaba cancelada
        if self.__estado == ESTADO_PROCESADA:
            raise ReservaError("No se puede cancelar una reserva ya procesada")
        if self.__estado == ESTADO_CANCELADA:
            raise ReservaError("La reserva ya estaba cancelada")
        self.__estado = ESTADO_CANCELADA
        print(f"  ✔ Reserva {self.id} cancelada")

    def procesar(self, aplicar_iva=True, descuento=0):
        # solo proceso si esta confirmada
        if self.__estado != ESTADO_CONFIRMADA:
            raise ReservaError(
                f"La reserva tiene que estar confirmada pa procesarla. Estado actual: '{self.__estado}'"
            )
        try:
            # calculo el costo con el servicio
            self.__costo_total = self.__servicio.calcular_costo(
                self.__horas,
                aplicar_iva=aplicar_iva,
                descuento=descuento
            )
            self.__estado = ESTADO_PROCESADA
            self.__fecha_proceso = datetime.now()  # guardo cuando se proceso
            print(f"  ✔ Reserva {self.id} procesada | Costo: ${self.__costo_total:,.2f}")
        except Exception as e:
            raise ReservaError(f"Error al procesar reserva {self.id}") from e

    def describir(self):
        # armo el resumen de la reserva
        return (f"Reserva {self.id} | "
                f"Cliente: {self.__cliente.nombre} | "
                f"Servicio: {self.__servicio.nombre} | "
                f"Horas: {self.__horas} | "
                f"Estado: {self.__estado} | "
                f"Costo: ${self.__costo_total:,.2f}")

    def validar(self):
        # valido horas, cliente y servicio
        if self.__horas <= 0:
            return False
        if not self.__cliente.validar():
            return False
        if not self.__servicio.validar():
            return False
        return True

    def __str__(self):
        return self.describir()