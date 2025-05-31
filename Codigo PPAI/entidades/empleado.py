
class Empleado:
    # Entidad Empleado del diagrama de secuencia
    def __init__(self, legajo, nombre):
        self.legajo = legajo
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
