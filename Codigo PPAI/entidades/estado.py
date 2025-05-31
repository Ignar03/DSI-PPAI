class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def sosCompletamenteRealizada(self):
        return self.nombre == "Completamente Realizada"

    def esCerrada(self):
        return self.nombre == "Cerrada"

    def getNombre(self):
        return self.nombre
