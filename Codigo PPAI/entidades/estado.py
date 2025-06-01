class Estado:
    def __init__(self, ambito, nombre):
        self.ambito = ambito
        self.nombre = nombre

    def sosCompletamenteRealizada(self):
        return self.nombre == "Completamente Realizada"

    def sosCerrada(self):
        return self.nombre == "Cerrada"

    def sosFueraDeServicio(self):
        return self.nombre == "Fuera de Servicio"

    def sosDeOrdenDeInspeccion(self):
        return self.nombre == "OI"
    
    def sosDeSismografo(self):
        return self.nombre == "S"

    def getNombre(self):
        return self.nombre
