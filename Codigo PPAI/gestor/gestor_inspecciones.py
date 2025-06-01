from data.sesion import actualSesion
from data.ordenes import ordenes
from data.motivos import motivos
from data.estados import estados
from datetime import datetime

class GestorInspecciones:
    # Clase Control según diagrama de secuencia
    def __init__(self, intefaz):
        self.actualizacionSismografo = ""
        self.motivos = []
        self.ordenes = ordenes
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.fechaHoraActual = ""
        self.interfaz = intefaz

        self.empleadoLogueado = self.buscarEmpleadoLogueado()
        ordenesCompRealizadas = self.buscarOrdenesInspeccion()
        self.mostrarOrdCompRealizadas(ordenesCompRealizadas)

    def buscarEmpleadoLogueado(self):
        usuarioActual = actualSesion.getUsuarioActual()
        empleadoLogueado = usuarioActual.obtenerEmpleado()

        return empleadoLogueado

    def buscarOrdenesInspeccion(self):      
        ordenesSinOrdenar = [o for o in self.ordenes if o.sosCompletamenteRealizada() and o.sosDeEmpleado(self.empleadoLogueado.legajo)]
        ordenesOrdenadas = self.ordenarPorFechaDeFinalizacion(ordenesSinOrdenar)
        return ordenesOrdenadas

    def ordenarPorFechaDeFinalizacion(self, ordenesSinOrdenar):
        ordenesOrdenadas = sorted(ordenesSinOrdenar, key=lambda o: o.fechaFinalizacion)
        return ordenesOrdenadas

    def mostrarOrdCompRealizadas(self, ordenes):
        self.interfaz.mostrarOrdCompRealizadas(ordenes)

    def tomarOrdenDeInspeccionSeleccionada(self, id_orden):
        for o in self.ordenes:
            if o.id == id_orden:
                self.ordenSeleccionada = o
                return o
            
        return None

    def pedirObservacion(self):
        self.interfaz.pedirObservacion()

    def tomarObservacion(self, texto):
        self.observacionCierre = texto
        
        self.buscarTipoMotivoFueraDeServicio()

    def buscarTipoMotivoFueraDeServicio(self):
        descMotivos = []
        
        for motivo in motivos:
            descMotivos.append(motivo.getDescripcion())

        self.mostrarMotivosTipo(descMotivos)
            
    def mostrarMotivosTipo(self, descMotivos):
        self.interfaz.mostrarMotivosTipo(descMotivos)
        
    def solicitarSeleccionMotivoFueraDeServicio(self, motivos):
        indiceMotivo = 0
        self.interfaz.solicitarSeleccionMotivoFueraDeServicio(motivos, indiceMotivo)

    def tomarMotivosFueraServicio(self, motivos, indiceMotivo):
        if indiceMotivo >= len(motivos):
            self.pedirConfirmacionCierreOrden()
            return

        self.motivos.append({"motivo": motivos[indiceMotivo], "comentario": ""})
        self.interfaz.pedirComentario(motivos, indiceMotivo)

    def tomarComentario(self, indiceMotivo, comentario):
        self.motivos[indiceMotivo]["comentario"] = comentario

    def pedirConfirmacionCierreOrden(self):
        self.interfaz.pedirConfirmacionCierreOrden()

    def tomarConfirmacionCierreOrden(self, confirmado):
        if self.validarExistenciaObservacion():
            if self.validarExistenciaMotivoTipo():
                estadoOrden = self.buscarEstadoCerrada()

                self.fechaHoraActual = self.getFechaHoraActual()

                estadoSismografo = self.buscarFueraDeServicio()

                if estadoOrden != None or estadoSismografo != None:
                    print("Error obteniendo los estados")
                    return
                
                self.cerrarOrdenInspeccion(estadoOrden)
                self.ponerSismografoFueraDeServicio(estadoSismografo)
        else:
            pass
    
    def validarExistenciaObservacion(self):
        if self.observacionCierre == "":
            return False
        else:
            return True
    
    def validarExistenciaMotivoTipo(self):
        if len(self.motivos) == 0:
            return False
        else:
            return True

    def buscarEstadoCerrada(self):
        for estado in estados:
            if estado.sosDeOrdenDeInspeccion() and estado.sosCerrada():
                return estado
        
        return None

    def getFechaHoraActual(self):
        return datetime.now()
    
    def buscarFueraDeServicio(self):
        for estado in estados:
            if estado.sosDeSismografo() and estado.sosFueraDeServicio():
                return estado
        
        return None
    
    def cerrarOrdenInspeccion(self, estadoOrden):
        self.ordenSeleccionada.cerrarOrden(self.fechaHoraActual, estadoOrden)

    def ponerSismografoFueraDeServicio(self, estadoSismografo):
        self.ordenSeleccionada.ponerSismografoFueraDeServicio(self.fechaHoraActual, estadoSismografo, self.empleadoLogueado, self.motivos)

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
