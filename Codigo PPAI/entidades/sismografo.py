class Sismografo:
    def __init__(self, identificadorSismografo, fechaAdquisicion=None, nroSerie=None):
        self.fechaAdquisicion = fechaAdquisicion    # Fecha de adquisición del sismógrafo
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estadoActual = "On-line"               # Atributo extra, útil para control


    def getIdentificadorSismografo(self):
        return self.identificadorSismografo

    def setEstadoActual(self, estado):
        self.estadoActual = estado

    def cerrarUltimoEstado(self):
        # Implementación según tus reglas; aquí es un stub
        pass

    def actualizarFueraServicio(self):
        self.estadoActual = "Fuera de Servicio"

    def cambiarEstadoFueraServicio(self):
        self.estadoActual = "Fuera de Servicio"
