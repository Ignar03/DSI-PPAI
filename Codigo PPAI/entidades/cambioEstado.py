from datetime import datetime

class CambioEstado:
    def __init__(self, FechaHoraInicio=None):
        self.FechaHoraInicio = FechaHoraInicio or datetime.now()
        self.FechaHoraFin = None

    def setFechaHoraFin(self):
        # Registra el momento de finalización del estado
        self.FechaHoraFin = datetime.now()

    def esEstadoActual(self):
        # True si este cambio de estado no tiene fecha de fin (es el estado vigente)
        return self.FechaHoraFin is None

    def sosActual(self):
        # Alias para esEstadoActual
        return self.esEstadoActual()
