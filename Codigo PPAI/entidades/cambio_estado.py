from entidades.motivo_fuera_servicio import MotivoFueraServicio
# from data.old.motivos import motivos as motivosData

class CambioEstado:
    def __init__(self,estado, fechaHoraInicio, fechaHoraFin, responsable, codigoCambioEstado=None):
        self.codigoCambioEstado = codigoCambioEstado
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.responsable = responsable
        self.estado = estado
        self.motivoFueraServicio = []

    def getEstado(self):
        return self.estado

    def getFechaHora(self):
        return self.fecha_hora

    def getResponsable(self):
        return self.responsable
    
    def esEstadoActual(self):
        if self.fechaHoraFin == "0":
            return self
        else:
            return None

    def setFechaHoraActual(self, fechaHoraActual):
        self.fechaHoraFin = fechaHoraActual
    
    def crearMotivoTipo(self, motivosSeleccionados, motivos):
        for m in motivosSeleccionados:
            for obj in motivos:
                if obj.getDescripcion() == m["motivo"]:
                    motivoSeleccionado = obj
                    break

            motivo = {
                "comentario": m["comentario"],
                "motivo": motivoSeleccionado
            }
                
            self.motivoFueraServicio.append( MotivoFueraServicio(motivo["comentario"], motivo["motivo"]) )