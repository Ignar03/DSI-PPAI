class Estado:
    def __init__(self, codigoEstado, ambito, nombre):
        self.codigoEstado = codigoEstado
        self.ambito = ambito
        self.nombre = nombre

    def sosCompletamenteRealizada(self):
        return self.nombre == "Completamente Realizada"

    def sosCerrada(self):
        return self.nombre == "Cerrada"

    def sosFueraDeServicio(self):
        return self.nombre == "Fuera de Servicio"

    def sosDeOrdenDeInspeccion(self):
        return self.ambito == "OI"
    
    def sosDeSismografo(self):
        return self.ambito == "S"

    def getNombre(self):
        return self.nombre
    
    def getCodigo(self):
        return self.codigoEstado
