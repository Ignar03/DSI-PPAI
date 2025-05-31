class Estado:
    def __init__(self, ambito, nombreEstado):
        self.ambito = ambito              # Por ejemplo: "OrdenDeInspeccion", "Sismografo", etc.
        self.nombreEstado = nombreEstado  # Por ejemplo: "Finalizada", "Cerrada", etc.

    def esRealizada(self):
        # True si el nombre del estado indica realizada
        return self.nombreEstado.lower() in ["realizada", "finalizada", "completada"]

    def sosAmbitoSismografo(self):
        # True si el estado corresponde a un sismógrafo
        return self.ambito.lower() == "sismografo"

    def sosFueraServicio(self):
        # True si el estado es "Fuera de Servicio"
        return self.nombreEstado.lower() == "fuera de servicio"

    def getNombre(self):
        return self.nombreEstado

