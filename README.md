# Software FJ - Sistema de Gestion de Clientes y Reservas
### Programacion Orientada a Objetos | Curso 213023 | UNAD

----------------------------------------------------------------------------------

## ¿De que trata?

Sistema hecho en Python para manejar clientes, servicios y reservas
de la empresa Software FJ. No usa base de datos, todo se maneja con
clases y los eventos se guardan en un archivo de log.

Lo hice para la fase 4 del curso, aplicando herencia, encapsulamiento,
clases abstractas y manejo de excepciones.

----------------------------------------------------------------------------------
## Archivos del proyecto

```
Fase 4/
│
├── modelos_base.py   # clases abstractas base (EntidadBase, Servicio)
├── cliente.py        # clase Cliente con validaciones en los setters
├── servicios.py      # ReservaSala, AlquilerEquipo, AsesoriaEspecializada
├── reserva.py        # clase Reserva con sus estados y excepciones
├── excepciones.py    # todas las excepciones personalizadas del sistema
├── logger.py         # guarda eventos y errores en un .log
├── main.py           # simulacion de 10 operaciones con casos validos e invalidos
└── sistema_fj.log    # se genera automaticamente al correr el main
```

----------------------------------------------------------------------------------

## Como correrlo

1. Clonar o descargar la carpeta del proyecto
2. Entrar a la carpeta `Fase 4/`
3. Ejecutar:

```bash
python main.py
```

El archivo `sistema_fj.log` se crea solo la primera vez que se corre.

----------------------------------------------------------------------------------

## Que hace cada parte

- **modelos_base.py** → clases padre de todo el sistema, usan ABC pa obligar
  a las clases hijas a implementar sus propios metodos
- **cliente.py** → maneja los datos del cliente con validaciones en cada setter
  (nombre, email, telefono, documento)
- **servicios.py** → tres tipos de servicio, cada uno calcula su costo distinto.
  La asesoria avanzada tiene un recargo del 20%
- **reserva.py** → conecta cliente con servicio, maneja los estados:
  pendiente → confirmada → procesada (o cancelada)
- **excepciones.py** → excepciones propias pa no mezclar errores del sistema
  con los de Python
- **logger.py** → escribe en `sistema_fj.log` cada evento o error que pase
- **main.py** → simula 10 operaciones, unas correctas y otras con errores
  a proposito pa demostrar que las excepciones funcionan

----------------------------------------------------------------------------------
## Conceptos que aplique

- Herencia y clases abstractas (`ABC`, `abstractmethod`)
- Encapsulamiento con name mangling (`__atributo`)
- Properties y setters con validacion
- Excepciones personalizadas y encadenadas (`raise ... from e`)
- Manejo de flujo con `try / except / else / finally`
- Escritura de archivos de log con manejo de errores

----------------------------------------------------------------------------------

## Autor

Boris Julian Mateus Alba  
Curso Programacion Orientada a Objetos — 213023  
UNAD — 2026