# simulacion de 10 operaciones del sistema Software FJ
# tiene casos buenos y malos pa probar las excepciones
# hecho por: Boris Julian Mateus Alba

from cliente import Cliente, ClienteInvalidoError
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada, ServicioInvalidoError
from reserva import Reserva, ReservaError
from logger import registrar_info, registrar_error, registrar_advertencia


# funcion pa imprimir el separador entre operaciones
def separador(numero, titulo):
    print(f"\n{'='*55}")
    print(f"  OPERACION {numero}: {titulo}")
    print(f"{'='*55}")


def main():

    registrar_info("=== Sistema Software FJ iniciado ===")
    print("\nIniciando simulacion del sistema Software FJ\n")

    # operacion 1: cliente valido
    separador(1, "Registro de cliente valido")
    try:
        c1 = Cliente("C001", "Carlos Mendoza", "carlos@email.com", "3101234567", "1023456789")
        print(f"{c1.describir()}")
        registrar_info(f"Cliente creado: {c1.nombre}")
    except ClienteInvalidoError as e:
        print(f"Error: {e}")
        registrar_error("Fallo al crear cliente C001", e)

    # operacion 2: email malo, tiene que fallar
    separador(2, "Registro de cliente con email invalido")
    try:
        c2 = Cliente("C002", "Ana Torres", "emailmalformado", "3209876543", "987654321")
        print(f"   {c2.describir()}")
    except ClienteInvalidoError as e:
        print(f"   ClienteInvalidoError capturada: {e}")
        registrar_error("Email invalido al crear cliente C002", e)
    finally:
        # esto siempre se ejecuta
        registrar_advertencia("Operacion 2 finalizada (cliente invalido esperado)")

    # operacion 3: nombre muy corto, tambien tiene que fallar
    separador(3, "Registro de cliente con nombre muy corto")
    try:
        c3 = Cliente("C003", "Al", "al@correo.com", "3001112233", "111222333")
        print(f"   {c3.describir()}")
    except ClienteInvalidoError as e:
        print(f"   ClienteInvalidoError capturada: {e}")
        registrar_error("Nombre invalido al crear cliente C003", e)

    # operacion 4: creo una sala valida
    separador(4, "Creacion de servicio ReservaSala")
    try:
        sala1 = ReservaSala("S001", "Sala de Conferencias A", 50000, 20)
        if sala1.validar():
            print(f"   {sala1.describir()}")
            registrar_info(f"Servicio creado: {sala1.nombre}")
        else:
            print("   El servicio no paso la validacion")
    except ServicioInvalidoError as e:
        print(f"   Error: {e}")
        registrar_error("Fallo al crear sala1", e)

    # operacion 5: precio negativo, no deberia pasar la validacion
    separador(5, "Creacion de servicio con precio negativo")
    try:
        sala_mala = ReservaSala("S002", "Sala Error", -1000, 10)
        if not sala_mala.validar():
            raise ServicioInvalidoError("El precio base no puede ser negativo o cero")
        print(f"   {sala_mala.describir()}")
    except ServicioInvalidoError as e:
        print(f"   ServicioInvalidoError capturada: {e}")
        registrar_error("Precio invalido en servicio S002", e)

    # operacion 6: reserva completa, confirmo y proceso
    separador(6, "Reserva exitosa - confirmar y procesar")
    try:
        equipo1 = AlquilerEquipo("S003", "Proyector HD", 30000, "Proyector", 5)
        r1 = Reserva("R001", c1, equipo1, 3)
        r1.confirmar()
        r1.procesar(aplicar_iva=True, descuento=10)
        registrar_info(f"Reserva R001 procesada. Costo: ${r1.costo_total:,.2f}")
    except (ReservaError, ServicioInvalidoError) as e:
        print(f"   Error en reserva: {e}")
        registrar_error("Fallo en reserva R001", e)

    # operacion 7: le meto 0 horas a ver que pasa
    separador(7, "Reserva con horas invalidas (0 horas)")
    try:
        asesoria1 = AsesoriaEspecializada("S004", "Asesoria Python", 80000, "Programacion", "intermedio")
        r2 = Reserva("R002", c1, asesoria1, 0)
        r2.confirmar()
    except ReservaError as e:
        print(f"   ReservaError capturada: {e}")
        # muestro la causa original si existe
        if e.__cause__:
            print(f"     Causa original: {e.__cause__}")
        registrar_error("Horas invalidas en reserva R002", e)

    # operacion 8: intento procesar sin confirmar primero
    separador(8, "Intentar procesar reserva sin confirmar antes")
    try:
        sala2 = ReservaSala("S005", "Sala VIP", 120000, 50)
        r3 = Reserva("R003", c1, sala2, 2)
        r3.procesar()  # me salto el confirmar a proposito
    except ReservaError as e:
        print(f"   ReservaError capturada: {e}")
        registrar_error("Intento de procesar sin confirmar - R003", e)

    # operacion 9: confirmo y cancelo
    separador(9, "Cancelar una reserva confirmada")
    try:
        asesoria2 = AsesoriaEspecializada("S006", "Asesoria Redes", 90000, "Redes", "avanzado")
        r4 = Reserva("R004", c1, asesoria2, 4)
        r4.confirmar()
        r4.cancelar()
        registrar_info(f"Reserva R004 cancelada correctamente")
    except ReservaError as e:
        print(f"   Error: {e}")
        registrar_error("Fallo al cancelar R004", e)
    else:
        # esto solo corre si no hubo ningun error
        print("   Cancelacion completada sin errores")

    # operacion 10: reservo mas de 12 horas, tiene que fallar
    separador(10, "Sala reservada por mas de 12 horas (limite)")
    try:
        sala3 = ReservaSala("S007", "Sala Capacitacion", 45000, 30)
        r5 = Reserva("R005", c1, sala3, 15)
        r5.confirmar()
        r5.procesar()
    except ReservaError as e:
        print(f"   ReservaError capturada: {e}")
        if e.__cause__:
            print(f"     Causa original: {e.__cause__}")
        registrar_error("Limite de horas superado en reserva R005", e)
    finally:
        registrar_info("Operacion 10 finalizada")
        print("  → Bloque finally ejecutado: log actualizado")

    print(f"\n{'='*55}")
    print("  Simulacion completada. Revisa 'sistema_fj.log'")
    print(f"{'='*55}\n")
    registrar_info("=== Sistema Software FJ finalizado ===")


if __name__ == "__main__":
    main()