
from datetime import datetime
from .cambio_estado import CambioEstado

class OrdenDeInspeccion:
    def __init__(self, id, estado, empleado, estacion, fechaFinalizacion):
        self.id = id
        self.estado = estado
        self.empleado = empleado
        self.estacion = estacion
        self.observacion = ""
        self.motivosCierre = []
        self.fechaFinalizacion = fechaFinalizacion
        self.fechaCierre = None
        
    def sosDeEmpleado(self, legajo):
        return self.empleado.getLegajo() == legajo
    
    def obtenerNumeroDeOrden(self):
        return self.id

    def obtenerFechaFinalizacion(self):
        return self.fechaFinalizacion
    
    def obtenerEstacionSismologica(self):
        return self.estacion.getNombre()
    
    def obtenerIdentificadorSismografo(self):
        return self.estacion.obtenerIdentificadorSismografo()

    def sosCompletamenteRealizada(self):
        return self.estado.getNombre() == "Completamente Realizada"

    def esCerrada(self):
        return self.estado.esCerrada()

    def cerrarOrden(self, fechaCierre, estado):
        self.fechaCierre = fechaCierre
        self.estado = estado

    def cambiarEstadoCerrado(self, responsable):
        self.estado.nombre = "Cerrada"
        self.crearCambioEstado("Cerrada", responsable)

    def setFechaHoraCierre(self):
        self.fechaCierre = datetime.now()

    def crearCambioEstado(self, nombreEstado, responsable):
        # cambio = CambioEstado(nombreEstado, datetime.now(), responsable)
        # self.historialEstados.append(cambio)
        pass

    def ponerSismografoFueraDeServicio(self, fechaHoraActual, estadoSismografo, empleadoLogueado, motivos):
        self.estacion.ponerSismografoFueraDeServicio(fechaHoraActual, estadoSismografo, empleadoLogueado, motivos)