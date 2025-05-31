class EstacionSismologica:
    def __init__(self, codigo, nombre, sismografo=None):
        self.codigo = codigo
        self.nombre = nombre
        self.sismografo = sismografo

    def getNombre(self):
        return self.nombre

    def getSismografo(self):
        return self.sismografo
