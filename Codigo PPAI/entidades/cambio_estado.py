
from datetime import datetime

class CambioEstado:
    def __init__(self, estado, fecha_hora, responsable):
        self.estado = estado
        self.fecha_hora = fecha_hora
        self.responsable = responsable

    def getEstado(self):
        return self.estado

    def getFechaHora(self):
        return self.fecha_hora

    def getResponsable(self):
        return self.responsable
