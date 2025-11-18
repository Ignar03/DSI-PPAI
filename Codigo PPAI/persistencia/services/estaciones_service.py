from persistencia.repositories.estacionesSismologica_repository import EstacionesSismologicaRepository
from entidades.estacion_sismologica import EstacionSismologica

class EstacionesService:
    def __init__(self):
        self.repository = EstacionesSismologicaRepository()

    def mapearEstacion(self, data):
        estacion = EstacionSismologica(
                codigoEstacion=data[0],
                latitud=data[1],
                longitud=data[2],
                nombre=data[3],
                fechaSolicitud=data[4],
                documentoCertificacion=data[5],
                nroCertificacion=data[6],
            )
        
        return estacion

    def obtenerEstaciones(self):
        data = self.repository.obtenerEstaciones()

        estaciones = []

        for fila in data:
            estacion = self.mapearEstacion(fila)
            estaciones.append(estacion)

        return estaciones
    
    def obtenerEstacionPorCodigo(self, codigoEstacion):
        data = self.repository.obtenerEstacionPorCodigo(codigoEstacion)

        estacion = self.mapearEstacion(data)

        return estacion
    
  