class Usuario:
    def __init__(self, nombre, contraseña, legajo):
        self.nombreUsuario = nombre
        self.contraseña = contraseña
        self.legajo = legajo

    def obtenerLegajo(self):
        return self.legajo
    
    def getFecha(self):
        return self.nombreUsuario
    
    def getNombre(self):
        return self.nombreUsuario