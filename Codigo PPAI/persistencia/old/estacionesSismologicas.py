from entidades.estacion_sismologica import EstacionSismologica
from data.old.sismografos import sismografos

estaciones = [
    EstacionSismologica("ES01", "Estación Central", sismografos[0]),
    EstacionSismologica("ES02", "Estación Norte", sismografos[1]),
]