from entidades.cambio_estado import CambioEstado 
from persistencia.services.cambioEstado_service import CambioEstadoService

class Sismografo:
    def __init__(self, codigoSismografo, estacion, cambiosEstado):
        self.codigoSismografo = codigoSismografo
        self.estacion = estacion
        self.cambiosEstado = cambiosEstado

    def getCodigo(self):
        return self.codigoSismografo

    def setEstado(self, estado):
        self.estado = estado

    def getEstacion(self):
        return self.estacion

    def getEstado(self):
        return self.estado
    
    def fueraDeServicio(self, fechaHoraActual, estadoSismografo, usuario, motivos, motivosSeleccionados):
        for cambioEstado in self.cambiosEstado:
            cambioEstadoActual = cambioEstado.esEstadoActual()

            if cambioEstadoActual is not None:
                break

        print(cambioEstadoActual)
        print("Cambio estado actual antes de setear fecha y hora:", cambioEstadoActual.estado.getCodigo())
        
            
        cambioEstadoActual.setFechaHoraActual(fechaHoraActual)

        nuevoCambioEstado = CambioEstado(estadoSismografo, fechaHoraActual, "", usuario.getNombre())
        nuevoCambioEstado.crearMotivoTipo(motivosSeleccionados, motivos)
        self.cambiosEstado.append(nuevoCambioEstado)
        
        CambioEstadoService().actualizarCambioEstado(cambioEstadoActual)
        CambioEstadoService().registrarCambioEstado(self.codigoSismografo, nuevoCambioEstado)
        
    
    

        

        