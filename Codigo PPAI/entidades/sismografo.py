
class Sismografo:
    def __init__(self, identificador):
        self.identificador = identificador
        self.estado = "On-line"

    def getIdentificador(self):
        return self.identificador

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado
