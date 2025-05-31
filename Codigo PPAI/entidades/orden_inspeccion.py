
from datetime import datetime
from .cambio_estado import CambioEstado

class OrdenDeInspeccion:
    def __init__(self, id, estado, empleado, estacion):
        self.id = id
        self.estado = estado
        self.empleado = empleado
        self.estacion = estacion
        self.observacion = ""
        self.motivosCierre = []
        self.fechaFinalizacion = None
        self.fechaCierre = None
        self.historialEstados = []

    def sosDeRI(self, legajo):
        return self.empleado.legajo == legajo

    def esFinalizada(self):
        return self.estado.getNombre() == "Finalizada"

    def esCerrada(self):
        return self.estado.esCerrada()

    def cambiarEstadoCerrado(self, responsable):
        self.estado.nombre = "Cerrada"
        self.crearCambioEstado("Cerrada", responsable)

    def setFechaHoraCierre(self):
        self.fechaCierre = datetime.now()

    def crearCambioEstado(self, estado_nombre, responsable):
        cambio = CambioEstado(estado_nombre, datetime.now(), responsable)
        self.historialEstados.append(cambio)
