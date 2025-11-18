from datetime import datetime

class OrdenDeInspeccion:
    def __init__(self, numeroOrden, fechaHoraInicio, fechaHoraCierre, fechaHoraFinalizacion, observacionCierre, estado, empleado, estacion):
        self.id = numeroOrden
        self.fechaInicio = fechaHoraInicio
        self.fechaCierre = fechaHoraCierre
        self.fechaFinalizacion = fechaHoraFinalizacion
        self.observacionCierre = observacionCierre
        self.estado = estado
        self.empleado = empleado
        self.estacion = estacion
        
    def sosDeEmpleado(self, legajo):
        return self.empleado.getLegajo() == legajo
    
    def obtenerNumeroDeOrden(self):
        return self.id

    def obtenerFechaFinalizacion(self):
        return self.fechaFinalizacion
    
    def obtenerEstacionSismologica(self):
        return self.estacion.getNombre()
    
    def obtenerIdentificadorSismografo(self, sismografos):
        return self.estacion.obtenerIdentificadorSismografo(sismografos)

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

    def ponerSismografoFueraDeServicio(self, fechaHoraActual, estadoSismografo, usuario, motivos, motivosSeleccionados, sismografos):
        self.estacion.ponerSismografoFueraDeServicio(fechaHoraActual, estadoSismografo, usuario, motivos, motivosSeleccionados, sismografos)