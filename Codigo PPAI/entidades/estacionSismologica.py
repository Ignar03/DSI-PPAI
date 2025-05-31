class EstacionSismologica:
    def __init__(self, codigoEstacion, documentoCertificacionAdq, fechaSolicitudCertificacion,
                 latitud, longitud, nombre, nroCertificacionAdquisicion):
        self.codigoEstacion = codigoEstacion
        self.documentoCertificacionAdq = documentoCertificacionAdq
        self.fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion

    def getCodigoEstacion(self):
        return self.codigoEstacion

    def getNombre(self):
        return self.nombre
