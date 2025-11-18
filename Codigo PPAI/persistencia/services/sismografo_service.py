from persistencia.repositories.sismografo_repository import SismografosRepository
from persistencia.services.estaciones_service import EstacionesService
from persistencia.services.cambioEstado_service import CambioEstadoService
from entidades.sismografo import Sismografo

class SismografoService:
    def __init__(self):
        self.repository = SismografosRepository()
        self.estacionesService = EstacionesService()

    def obtenerSismografos(self):
        filas = self.repository.obtenerSismografos()
        sismografos = []
        for fila in filas:
            sismografo = Sismografo(
                codigoSismografo = fila[0],
                estacion = self.obtenerEstacionSismologicaDeSismografo(fila[1]),
                cambiosEstado= self.obtenerCambiosEstadoDeSismografo(fila[0])
            )

            sismografos.append(sismografo)
        return sismografos
    
    def obtenerCambiosEstadoDeSismografo(self,codigoSismografo):
        filas = self.repository.obtenerCambiosEstadoDeSismografo(codigoSismografo)
        cambiosEstado = []

        for fila in filas:
            objetoCambioEstado = CambioEstadoService().mapearCambioEstado(fila)
            cambiosEstado.append(objetoCambioEstado)
            

        return cambiosEstado

    def obtenerEstacionSismologicaDeSismografo(self, codigoEstacion):
        objetoEstacion = EstacionesService().obtenerEstacionPorCodigo(codigoEstacion)
        return objetoEstacion