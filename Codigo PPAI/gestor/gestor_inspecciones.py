
class GestorInspecciones:
    # Clase Control según diagrama de secuencia
    def __init__(self, ordenes, legajo_usuario):
        self.ordenes = ordenes
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.motivos = []
        self.legajo_usuario = legajo_usuario

    def buscarOrdenesInspeccion(self):
        return [o for o in self.ordenes if o.esFinalizada() and o.sosDeRI(self.legajo_usuario)]

    def seleccionarOrdenInspeccion(self, id_orden):
        for o in self.ordenes:
            if o.id == id_orden:
                self.ordenSeleccionada = o
                return o
        return None

    def tomarObservacionCierre(self, texto):
        self.observacionCierre = texto

    def tomarMotivoCierre(self, motivo, comentario):
        self.motivos.append((motivo, comentario))

    def validarCierreOrden(self):
        if not self.ordenSeleccionada:
            return False
        if not self.observacionCierre.strip():
            return False
        if not self.motivos:
            return False
        for motivo, comentario in self.motivos:
            if comentario.strip() == "":
                return False
        return True

    def buscarEstadoCerrado(self):
        if self.ordenSeleccionada:
            return self.ordenSeleccionada.esCerrada()
        return False

    def cerrarOrden(self, notificar_mail=True, notificar_monitor=True):
        if not self.validarCierreOrden():
            return False
        if self.buscarEstadoCerrado():
            return False

        # Aca se registra fecha/hora, observación, motivos, y se actualiza el estado y el historial.
        responsable = self.ordenSeleccionada.empleado
        self.ordenSeleccionada.cambiarEstadoCerrado(responsable)
        self.ordenSeleccionada.setFechaHoraCierre()
        self.ordenSeleccionada.observacion = self.observacionCierre
        self.ordenSeleccionada.motivosCierre = self.motivos

        # Notificaciones
        if notificar_mail and not notificar_monitor:
            self.enviarNotificacionEmpleado(self.ordenSeleccionada)
        elif not notificar_mail and notificar_monitor:
            self.enviarNotificacionInterfazCCRS(self.ordenSeleccionada)
        elif notificar_mail and notificar_monitor:
            self.enviarNotificacionEmpleado(self.ordenSeleccionada)
            self.enviarNotificacionInterfazCCRS(self.ordenSeleccionada)

        # NO elimina la orden: sólo cambia su estado
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.motivos = []
        return True

    def enviarNotificacionEmpleado(self, orden):
        print(f"[NOTIFICACIÓN POR MAIL] Orden {orden.id} cerrada.")

    def enviarNotificacionInterfazCCRS(self, orden):
        print(f"[NOTIFICACIÓN EN MONITOR CCRS] Orden {orden.id} cerrada.")
