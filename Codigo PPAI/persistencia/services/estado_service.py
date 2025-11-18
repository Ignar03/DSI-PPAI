from persistencia.repositories.estados_repository import EstadosRepository
from entidades.estado import Estado

class EstadoService:
    def __init__(self):
        self.repository = EstadosRepository()

    def obtenerEstados(self):
        data = self.repository.obtenerEstados()

        estados = []
        for i in data:
            codigoEstado = i[0]
            ambito = i[1]
            nombreEstado = i[2]
    
            estado = Estado(codigoEstado, ambito, nombreEstado)
            
            estados.append(estado)

        return estados

    def obtenerEstadoPorCodigo(self, codigoEstado):
        data = self.repository.obtenerEstadoPorCodigo(codigoEstado)

        codigoEstado = data[0]
        ambito = data[1]
        nombreEstado = data[2]
    
        estado = Estado(codigoEstado, ambito, nombreEstado)
        
        return estado