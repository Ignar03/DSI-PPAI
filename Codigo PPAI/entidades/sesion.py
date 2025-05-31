import datetime

class Sesion:
    def __init__(self, idSesion, usuario):
        self.idSesion = idSesion
        self.usuario = usuario
        self.fechaInicioSesion = datetime.datetime.now()
        self.fechaFinSesion = None

    def getUsuarioActual(self):
        return self.usuario
    
    def getFecha(self):
        return self.fechaInicioSesion

    def cerrarSesion(self):
        self.fechaFinSesion = datetime.datetime.now()