
class Empleado:
    # Entidad Empleado del diagrama de secuencia
    def __init__(self, legajo, apellido, nombre, mail, telefono, rol):
        self.legajo = legajo
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.rol = rol

    def getLegajo(self):
        return self.legajo
    
    def getNombre(self):
        return self.nombre
    
    def obtenerMail(self):
        return self.mail
    
    def esResponsableReparacion(self):
        return self.rol.esResponsableReparacion()