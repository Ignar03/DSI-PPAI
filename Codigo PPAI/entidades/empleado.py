
class Empleado:
    # Entidad Empleado del diagrama de secuencia
    def __init__(self, legajo, apellido, nombre, mail, telefono):
        self.legajo = legajo
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

    def getLegajo(self):
        return self.legajo
    
    def getNombre(self):
        return self.nombre