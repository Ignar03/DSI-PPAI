from datetime import datetime

class OrdenDeInspeccion:
    def __init__(self, numeroOrden, fechaHoraInicio=None, fechaHoraFinalizacion=None,
                 fechaHoraCierre=None, observacionCierre=""):
        self.fechaHoraCierre = fechaHoraCierre         # Fecha/hora en la que se cierra la orden
        self.fechaHoraFinalizacion = fechaHoraFinalizacion   # Fecha/hora de finalización
        self.fechaHoraInicio = fechaHoraInicio         # Fecha/hora de inicio
        self.numeroOrden = numeroOrden                 # Número identificador de la orden
        self.observacionCierre = observacionCierre     # Observación del cierre

    def getFechaFinalizacion(self):
        return self.fechaHoraFinalizacion

    def getNumeroOrden(self):
        return self.numeroOrden

    def setEstado(self, estado):
        self.estado = estado

    def setFechaHoraCierre(self, fecha=None):
        # Permite setear la fecha de cierre (por default ahora)
        self.fechaHoraCierre = fecha or datetime.now()

    def sosDeRi(self, legajo):
        # Método de identificación de responsable (implementación sugerida, adaptala a tu dominio)
        return hasattr(self, "responsableInspeccion") and self.responsableInspeccion.legajo == legajo

    def estaCompletamenteRealizada(self):
        # Devuelve True si la orden está finalizada
        return self.fechaHoraFinalizacion is not None

    def guardarObservacionCierre(self, observacion):
        self.observacionCierre = observacion

    def setFechaHoraCierre(self, fecha=None):
        # Agregado para utilidad, aunque el diagrama no lo pide explícito
        self.fechaHoraCierre = fecha or datetime.now()

    def esFinalizada(self):
        return hasattr(self, "estado") and self.estado is not None and hasattr(self.estado,"nombreEstado") and self.estado.nombreEstado.lower() == "finalizada"


