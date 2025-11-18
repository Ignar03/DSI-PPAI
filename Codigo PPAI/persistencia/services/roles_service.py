from persistencia.repositories.roles_repository import RolesRepository
from entidades.rol import Rol

class RolesService:
    def __init__(self):
        self.repository = RolesRepository()

    def mapearRoles(self, descripcion, nombreRol):
        rol = Rol(descripcion, nombreRol)

        return rol
    
    