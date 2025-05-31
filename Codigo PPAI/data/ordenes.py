from entidades.orden_inspeccion import OrdenDeInspeccion
from entidades.estado import Estado
from entidades.estacion_sismologica import EstacionSismologica
from entidades.empleado import Empleado
from entidades.sismografo import Sismografo

ordenes = [
    OrdenDeInspeccion(
        100,
        Estado("Cerrada"),
        Empleado(1, "Juan Perez"),
        EstacionSismologica("ES03", "Estación Norte", Sismografo("S02"))
    ),
    OrdenDeInspeccion(
        101,
        Estado("Finalizada"),
        Empleado(1, "María López"),
        EstacionSismologica("ES01", "Estación Central", Sismografo("S01"))
    ),
    OrdenDeInspeccion(
        102,
        Estado("Finalizada"),
        Empleado(1, "María López"),
        EstacionSismologica("ES02", "Estación Norte", Sismografo("S02"))
    ),
    OrdenDeInspeccion(
        103,
        Estado("Cerrada"),
        Empleado(1, "María López"),
        EstacionSismologica("ES02", "Estación Norte", Sismografo("S02"))
    ),
    OrdenDeInspeccion(
        104,
        Estado("Finalizada"),
        Empleado(1, "Juan Perez"),
        EstacionSismologica("ES03", "Estación Norte", Sismografo("S02"))
    ),
]