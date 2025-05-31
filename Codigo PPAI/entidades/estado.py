class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def esFinalizada(self):
        return self.nombre == "Finalizada"

    def esCerrada(self):
        return self.nombre == "Cerrada"

    def getNombre(self):
        return self.nombre
