from persistencia.repositories.usuarios_repository import UsuariosRepository
from entidades.usuario import Usuario

class UsuariosService:
    def __init__(self):
        self.repository = UsuariosRepository()

    def mapearUsuario(self, nombre, contrasena, legajo):
        usuario = Usuario(nombre,contrasena,legajo)

        return usuario


    def obtenerUsuarios(self):
        data = self.repository.obtenerUsuarios()

        usuarios = []

        for i in data:
            usuario = self.mapearUsuario(nombre=i[0], contrasena=i[1], legajo=i[2])
        
            usuarios.append(usuario)

        return usuarios


    def obtenerUsuarioPorNombre(self, nombre):
        data = self.repository.obtenerUsuarioPorNombre(nombre)

        if data:
            usuario = self.mapearUsuario(nombre=data[0], contrasena=data[1], legajo=data[2])
            return usuario
        else:
            return None