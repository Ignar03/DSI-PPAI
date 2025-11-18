from persistencia.repositories.cambioEstado_repository import CambioEstadoRepository
from persistencia.services.estado_service import EstadoService
from entidades.cambio_estado import CambioEstado

class CambioEstadoService:
    def __init__(self):
        self.repository = CambioEstadoRepository()
    
    def mapearCambioEstado(self, data):
        codigoCambioEstado = data[0]
        fechaHoraInicio = data[1]
        fechaHoraFin = data[2]
        responsableCambio = data[3]
        objetoEstado = EstadoService().obtenerEstadoPorCodigo(data[4])

        cambioEstado = CambioEstado(codigoCambioEstado=codigoCambioEstado, estado=objetoEstado, fechaHoraInicio=fechaHoraInicio, fechaHoraFin=fechaHoraFin, responsable=responsableCambio)

        return cambioEstado
        

    def obtenerCambiosEstado(self):
        data = self.repository.obtenerCambiosEstado()

        cambiosEstado = []

        for fila in data:
            cambioEstado = self.mapearCambioEstado(fila)

            cambiosEstado.append(cambioEstado)

        return cambiosEstado
    
    def registrarCambioEstado(self, codigoSismografo, cambioEstado):
        codigoCambioEstado = self.repository.registrarCambioEstado(
            codigoSismografo,
            cambioEstado.fechaHoraInicio,
            cambioEstado.responsable,
            cambioEstado.estado.codigoEstado
        )

        return codigoCambioEstado
    
    def actualizarCambioEstado(self, cambioEstado):
        self.repository.actualizarCambioEstado(
            cambioEstado.codigoCambioEstado,
            cambioEstado.fechaHoraFin,
            cambioEstado.responsable,
            cambioEstado.estado.getCodigo()
        )