# cliente.py
# clase para manejar los clientes del sistema
# hecho por: Boris Julian Mateus Alba

import re
from Estructura_clases import EntidadBase


# cree esta excepcion para manejar los errores del cliente aparte
class ClienteInvalidoError(Exception):
    pass


class Cliente(EntidadBase):

    def __init__(self, id_cliente, nombre, email, telefono, documento):
        super().__init__(id_cliente)  # llamo al constructor del padre
        # uso los setters directamente pa que validen desde el principio
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento = documento

    # getters y setters de cada atributo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # minimo 3 letras, si no lanza error
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres")
        self.__nombre = valor.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        # use regex pa validar que el email tenga el formato correcto
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(patron, valor):
            raise ClienteInvalidoError(f"El email '{valor}' no es valido")
        self.__email = valor.lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        # solo digitos y que tenga minimo 7
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise ClienteInvalidoError("El telefono solo puede tener digitos y minimo 7")
        self.__telefono = str(valor)

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        # lo mismo pero pa el documento, minimo 6 digitos
        if not str(valor).isdigit() or len(str(valor)) < 6:
            raise ClienteInvalidoError("El documento tiene que ser numerico, minimo 6 digitos")
        self.__documento = str(valor)

    def describir(self):
        # armo el string con los datos del cliente
        return (f"Cliente: {self.__nombre} | "
                f"Doc: {self.__documento} | "
                f"Email: {self.__email} | "
                f"Tel: {self.__telefono}")

    def validar(self):
        # si llego hasta aca es porque todo lo validaron los setters
        return True

    def __str__(self):
        return self.describir()