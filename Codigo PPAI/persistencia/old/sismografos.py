from data.cambiosEstado import cambios
from entidades.sismografo import Sismografo

sismografos = [
    Sismografo("S001", cambios[:3]),
    Sismografo("S002", cambios[3:])
]