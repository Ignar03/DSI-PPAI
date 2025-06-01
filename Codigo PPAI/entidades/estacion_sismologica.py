class EstacionSismologica:
    def __init__(self, codigo, nombre, sismografo=None):
        self.codigo = codigo
        self.nombre = nombre
        self.sismografo = sismografo

    def getNombre(self):
        return self.nombre

    def obtenerIdentificadorSismografo(self):
        return self.getSismografo().getIdentificador()

    def getSismografo(self):
        return self.sismografo
    
    def ponerSismografoFueraDeServicio(self, fechaHoraActual, estadoSismografo,empleadoLogueado,motivos):
        self.sismografo.fueraDeServicio(fechaHoraActual, estadoSismografo,empleadoLogueado, motivos)
