from abstractas.i_observador_notificacion_ordenes import IObservadorNotificacionOrdenes

class InterfazNotificacionMail(IObservadorNotificacionOrdenes):
    def __init__(self):
        self.dominios = []
        self.dominio = ""
        self.idSismografo = ""
        self.nombreEstado = ""
        self.fechaHoraActual = ""
        self.motivos = []

    def actualizar(self, dominios, idSismografo, nombreEstado, fechaHoraActual, motivos):
        self.dominios = dominios
        self.idSismografo = idSismografo
        self.nombreEstado = nombreEstado
        self.fechaHoraActual = fechaHoraActual
        self.motivos = motivos
        
        for dominio in dominios:
            self.dominio = dominio
            self.enviarCorreo()

    # Envia UN SOLO correo por cada dominio
    # Es un print a falta de una API de mails 
    def enviarCorreo(self):
        print(f"[MAIL ENVIADO A {self.dominio} CON: {self.idSismografo, self.nombreEstado, self.fechaHoraActual, self.motivos}]")

interfazNotificacionMail = InterfazNotificacionMail()