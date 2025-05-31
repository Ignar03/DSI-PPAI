class GestorInspecciones:
    def __init__(self):
        self.listaOrdenesInspeccion = []
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.motivos = []

    def buscarOrdenesInspeccion(self):
        # Devuelve solo las órdenes finalizadas
        return [o for o in self.listaOrdenesInspeccion if o.esFinalizada()]

    def tomarOrdenInspección(self, numeroOrden):
        for o in self.listaOrdenesInspeccion:
            if o.numeroOrden == numeroOrden:
                self.ordenSeleccionada = o
                return o
        return None

    def tomarOrdenObservaciónCierre(self, texto):
        self.observacionCierre = texto

    def tomarMotivoCierre(self, motivo, comentario):
        self.motivos.append((motivo, comentario))

    def validarCierreOrden(self):
        # Verifica que la orden, la observación y los motivos sean válidos
        if not self.ordenSeleccionada:
            print("No hay orden seleccionada")
            return False
        if not self.observacionCierre or not self.observacionCierre.strip():
            print("Observación de cierre vacía:", self.observacionCierre)
            return False
        if not self.motivos:
            print("Motivos de cierre vacíos")
            return False
        for motivo, comentario in self.motivos:
            if not comentario.strip():
                print("Comentario de motivo vacío:", comentario)
                return False
        return True

    def cerrarOrden(self):
        # Guarda los datos de cierre antes de validar
        self.ordenSeleccionada.guardarObservacionCierre(self.observacionCierre)
        self.ordenSeleccionada.motivosCierre = self.motivos
        if not self.validarCierreOrden():
            return False
        # Cambia el estado de la orden a "Cerrada"
        self.ordenSeleccionada.estado.nombreEstado = "Cerrada"
        self.ordenSeleccionada.setFechaHoraCierre()
        # Limpia el estado interno del gestor
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.motivos = []
        return True

    def enviarNotificacionEmpleado(self, mensaje):
        print(f"[NOTIFICACIÓN POR MAIL] {mensaje}")

    def enviarNotificacionInterfazCCRS(self, mensaje):
        print(f"[NOTIFICACIÓN CCRS] {mensaje}")


