
class EstacionSismologica:
    def __init__(self, codigoEstacion, latitud, longitud, nombre, fechaSolicitud, documentoCertificacion, nroCertificacion ):
        self.codigo = codigoEstacion
        self.latitud = latitud
        self.longitud = longitud
        self.fechaSolicitud = fechaSolicitud
        self.documentoCertificacion = documentoCertificacion
        self.nombre = nombre
        self.nroCertificacion = nroCertificacion

    def getNombre(self):
        return self.nombre

    def obtenerIdentificadorSismografo(self, sismografos):
        for s in sismografos:
            if s.getEstacion().getCodigo() == self.codigo:
                return s
        else:
            return None
    
    def getCodigo(self):
        return self.codigo
    
    def ponerSismografoFueraDeServicio(self, fechaHoraActual, estadoSismografo,usuario, motivos, motivosSeleccionados, sismografos):
        sismografo = self.obtenerIdentificadorSismografo(sismografos)
        sismografo.fueraDeServicio(fechaHoraActual, estadoSismografo ,usuario, motivos, motivosSeleccionados)