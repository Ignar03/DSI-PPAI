from abstractas.i_observador_notificacion_ordenes import IObservadorNotificacionOrdenes

class InterfazCCRS(IObservadorNotificacionOrdenes):
    def __init__(self):
        self.dominio = ""
        self.idSismografo = ""
        self.nombreEstado = ""
        self.fechaHoraActual = ""
        self.motivos = []

    def actualizar(self, dominio, idSismografo, nombreEstado, fechaHoraActual, motivos):
        
        self.dominio = dominio
        self.idSismografo = idSismografo
        self.nombreEstado = nombreEstado
        self.fechaHoraActual = fechaHoraActual
        self.motivos = motivos
        self.enviarNotificacion()

    def enviarNotificacion(self):
        
        print(f"[NOTIFICACIÓN ENVIADA CON: {self.idSismografo, self.nombreEstado, self.fechaHoraActual, self.motivos}]")

        
interfazCCRS = InterfazCCRS()