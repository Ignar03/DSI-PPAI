import datetime

class Sesion:
    def __init__(self, codigoSesion, usuario, fechaInicio, fechaFin= None):
        self.codigoSesion = codigoSesion
        self.usuario = usuario
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin

    def getUsuarioActual(self):
        return self.usuario
    
    def getFecha(self):
        return self.fechaInicio

    def cerrarSesion(self):
        self.fechaFin = datetime.datetime.now()