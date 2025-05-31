class Usuario:
    def __init__(self, nombre, contraseña, empleado):
        self.nombreUsuario = nombre
        self.contraseña = contraseña
        self.empleado = empleado

    def obtenerEmpleado(self):
        return self.empleado
    
    def getFecha(self):
        return self.nombreUsuario