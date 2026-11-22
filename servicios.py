# aca van los 3 servicios del sistema, cada uno hereda de Servicio
# hecho por: Boris Julian Mateus Alba

from Estructura_clases import Servicio


# excepcion pa manejar errores de los servicios
class ServicioInvalidoError(Exception):
    pass


# servicio 1: reserva de salas
class ReservaSala(Servicio):

    # el iva en colombia es del 19%
    IVA = 0.19

    def __init__(self, id_servicio, nombre, precio_base, capacidad_maxima):
        super().__init__(id_servicio, nombre, precio_base)
        self.capacidad_maxima = capacidad_maxima

    def validar_parametros(self, horas):
        # las horas tienen que ser positivas
        if horas <= 0:
            raise ServicioInvalidoError("Las horas deben ser mayores a cero")
        # tampoco se puede reservar mas de 12 horas
        if horas > 12:
            raise ServicioInvalidoError("No se puede reservar por mas de 12 horas seguidas")

    def calcular_costo(self, horas, aplicar_iva=True, descuento=0):
        self.validar_parametros(horas)
        costo = self._precio_base * horas
        # si hay descuento lo resto primero
        if descuento > 0:
            costo = costo - (costo * descuento / 100)
        # despues aplico el iva si toca
        if aplicar_iva:
            costo = costo * (1 + self.IVA)
        return round(costo, 2)

    def describir(self):
        base = super().describir()
        return f"{base} | Tipo: Reserva de Sala | Capacidad: {self.capacidad_maxima} personas"

    def validar(self):
        if not super().validar():
            return False
        # la capacidad tiene que ser positiva tambien
        if self.capacidad_maxima <= 0:
            return False
        return True


# servicio 2: alquiler de equipos
class AlquilerEquipo(Servicio):

    IVA = 0.19

    def __init__(self, id_servicio, nombre, precio_base, tipo_equipo, cantidad_disponible):
        super().__init__(id_servicio, nombre, precio_base)
        self.tipo_equipo = tipo_equipo
        self.cantidad_disponible = cantidad_disponible

    def validar_parametros(self, horas):
        if horas <= 0:
            raise ServicioInvalidoError("Las horas de alquiler deben ser mayores a cero")
        # si no hay equipos disponibles no se puede alquilar
        if self.cantidad_disponible <= 0:
            raise ServicioInvalidoError(f"No hay unidades disponibles de '{self.tipo_equipo}'")

    def calcular_costo(self, horas, aplicar_iva=True, descuento=0):
        self.validar_parametros(horas)
        costo = self._precio_base * horas
        if descuento > 0:
            costo = costo - (costo * descuento / 100)
        if aplicar_iva:
            costo = costo * (1 + self.IVA)
        return round(costo, 2)

    def describir(self):
        base = super().describir()
        return (f"{base} | Tipo: Alquiler de Equipo | "
                f"Equipo: {self.tipo_equipo} | "
                f"Disponibles: {self.cantidad_disponible}")

    def validar(self):
        if not super().validar():
            return False
        # tiene que tener tipo de equipo si o si
        if not self.tipo_equipo:
            return False
        return True


# servicio 3: asesoria especializada
class AsesoriaEspecializada(Servicio):

    IVA = 0.19

    def __init__(self, id_servicio, nombre, precio_base, area_conocimiento, nivel):
        super().__init__(id_servicio, nombre, precio_base)
        self.area_conocimiento = area_conocimiento
        self.nivel = nivel  # puede ser basico, intermedio o avanzado

    def validar_parametros(self, horas):
        if horas <= 0:
            raise ServicioInvalidoError("Las horas de asesoria deben ser mayores a cero")
        # valido que el nivel sea uno de los 3 permitidos
        niveles_validos = ["basico", "intermedio", "avanzado"]
        if self.nivel.lower() not in niveles_validos:
            raise ServicioInvalidoError(f"Nivel invalido, use uno de estos: {niveles_validos}")

    def calcular_costo(self, horas, aplicar_iva=True, descuento=0):
        self.validar_parametros(horas)
        costo = self._precio_base * horas
        # si es avanzado le meto un 20% mas
        if self.nivel.lower() == "avanzado":
            costo = costo * 1.20
        if descuento > 0:
            costo = costo - (costo * descuento / 100)
        if aplicar_iva:
            costo = costo * (1 + self.IVA)
        return round(costo, 2)

    def describir(self):
        base = super().describir()
        return (f"{base} | Tipo: Asesoria | "
                f"Area: {self.area_conocimiento} | "
                f"Nivel: {self.nivel}")

    def validar(self):
        if not super().validar():
            return False
        # necesita tener area de conocimiento
        if not self.area_conocimiento:
            return False
        return True