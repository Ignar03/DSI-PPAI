class MotivoTipo:
    def __init__(self,codigoMotivoTipo, nombre, descripcion=""):
        self.codigoMotivoTipo = codigoMotivoTipo
        self.nombre = nombre
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion
