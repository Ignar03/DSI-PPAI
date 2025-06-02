class Rol:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def esResponsableReparacion(self):
        if self.nombre == "RR":
            return True
        else:
            return False