from persistencia.repositories.sesiones_repository import SesionesRepository
from persistencia.services.usuarios_service import UsuariosService
from entidades.sesion import Sesion

class SesionService:
    def __init__(self):
        self.repository = SesionesRepository()

    def obtenerSesionActual(self):
        data = self.repository.obtenerSesiones()

        sesion = Sesion(codigoSesion = data[0], fechaInicio = data[1], fechaFin = data[2], usuario = UsuariosService().obtenerUsuarioPorNombre(data[3]) )
            
        return sesion
