# modelos_base.py
# clases principales del proyecto Software FJ
# hecho por: Boris Julian Mateus Alba

from abc import ABC, abstractmethod
from datetime import datetime


# esta es la clase padre de todo, de aqui heredan clientes, servicios y reservas
class EntidadBase(ABC):

    def __init__(self, id_entidad):
        self.__id = id_entidad
        self.__fecha_creacion = datetime.now()  # guardo cuando se creo

    @property
    def id(self):
        return self.__id

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # cada hijo tiene que definir su propio describir()
    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar(self):
        pass

    def __str__(self):
        # formateo la fecha pa que se vea bonito
        fecha = self.__fecha_creacion.strftime("%Y-%m-%d %H:%M")
        return f"[{type(self).__name__}] ID: {self.__id} | Creado: {fecha}"


# los servicios del sistema heredan de aqui
class Servicio(EntidadBase):

    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)  # llamo al padre
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    # esto cambia dependiendo del tipo de servicio por eso es abstracto
    @abstractmethod
    def calcular_costo(self, horas, aplicar_iva=True, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, horas):
        pass

    def describir(self):
        return f"Servicio: {self._nombre} - Precio base/hora: ${self._precio_base:,.0f}"

    def validar(self):
        # valido que el nombre no este vacio y que el precio sea positivo
        if self._nombre == "" or self._nombre is None:
            return False
        if self._precio_base <= 0:
            return False
        return True  # si pasa todo esta bien