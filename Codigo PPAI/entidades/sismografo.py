from entidades.cambio_estado import CambioEstado 

class Sismografo:
    def __init__(self, identificador, cambiosEstado):
        self.identificador = identificador
        self.cambiosEstado = cambiosEstado

    def getIdentificador(self):
        return self.identificador

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado
    
    def fueraDeServicio(self, fechaHoraActual, estadoSismografo, empleadoLogueado, motivos):
        for cambioEstado in self.cambiosEstado:
            cambioEstadoActual = cambioEstado.esEstadoActual()
            
        cambioEstadoActual.setFechaHoraActual(fechaHoraActual)

        nuevoCambioEstado = CambioEstado(estadoSismografo, fechaHoraActual, "", empleadoLogueado.getNombre())
        
        

        nuevoCambioEstado.crearMotivoTipo(motivos)

        

        