from entidades.orden_inspeccion import OrdenDeInspeccion
from data.empleados import empleados
from data.estados import estados
from data.estacionesSismologicas import estaciones
import datetime

# Por ahora lo hard-codeamos a falta de una base de datos
ordenes = [
    OrdenDeInspeccion(
        100,
        estados[2],
        empleados[0],
        estaciones[0],
        datetime.datetime(2025, 3, 15)
    ),
    OrdenDeInspeccion(
        101,
        estados[0],
        empleados[1],
        estaciones[1],
        datetime.datetime(2025, 5, 15)

    ),
    OrdenDeInspeccion(
        102,
        estados[0],
        empleados[1],
        estaciones[0],
        datetime.datetime(2025, 4, 5)
    ),
    OrdenDeInspeccion(
        103,
        estados[0],
        empleados[1],
        estaciones[0],
        datetime.datetime(2024, 12, 1)
    ),
    OrdenDeInspeccion(
        104,
        estados[2],
        empleados[1],
        estaciones[1],
        datetime.datetime(2025, 5, 26)
    ),
]