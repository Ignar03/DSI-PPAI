from entidades.orden_inspeccion import OrdenDeInspeccion
from entidades.estado import Estado
from entidades.estacion_sismologica import EstacionSismologica
from data.empleados import empleados
from entidades.sismografo import Sismografo
import datetime

# Por ahora lo hard-codeamos a falta de una base de datos
ordenes = [
    OrdenDeInspeccion(
        100,
        Estado("Pendiente Realización"),
        empleados[0],
        EstacionSismologica("ES03", "Estación Norte", Sismografo("S02")),
        datetime.datetime(2025, 3, 15)
    ),
    OrdenDeInspeccion(
        101,
        Estado("Completamente Realizada"),
        empleados[1],
        EstacionSismologica("ES01", "Estación Central", Sismografo("S01")),
        datetime.datetime(2025, 5, 15)

    ),
    OrdenDeInspeccion(
        102,
        Estado("Completamente Realizada"),
        empleados[1],
        EstacionSismologica("ES02", "Estación Norte", Sismografo("S02")),
        datetime.datetime(2025, 4, 5)
    ),
    OrdenDeInspeccion(
        103,
        Estado("Completamente Realizada"),
        empleados[1],
        EstacionSismologica("ES02", "Estación Norte", Sismografo("S02")),
        datetime.datetime(2024, 12, 1)
    ),
    OrdenDeInspeccion(
        104,
        Estado("Pendiente Realización"),
        empleados[1],
        EstacionSismologica("ES03", "Estación Norte", Sismografo("S02")),
        datetime.datetime(2025, 5, 26)
    ),
]