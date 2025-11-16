from data.sesion import actualSesion
from data.ordenes import ordenes
from data.motivos import motivos
from data.estados import estados
from data.empleados import empleados
from abstractas.i_sujeto_notificadores_ordenes import ISujetoNotificadorOrdenes
from datetime import datetime
from interfaz.interfaz_notificacion_mail import interfazNotificacionMail
from interfaz.interfaz_ccrs import interfazCCRS

class GestorInspecciones(ISujetoNotificadorOrdenes):
    def __init__(self, interfaz):
        self.actualizacionSismografo = ""
        self.motivos = []
        self.ordenes = ordenes
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.fechaHoraActual = ""
        self.interfaz = interfaz
        self.observadores = []
        self.dominios = []
        self.estadoOrden = None

        self.empleadoLogueado = self.buscarEmpleadoLogueado()
        ordenesCompRealizadas = self.buscarOrdenesInspeccion()
        self.mostrarOrdCompRealizadas(ordenesCompRealizadas)

    def buscarEmpleadoLogueado(self):
        usuarioActual = actualSesion.getUsuarioActual()
        empleadoLogueado = usuarioActual.obtenerEmpleado()

        return empleadoLogueado

    def buscarOrdenesInspeccion(self):      
        ordenesSinOrdenar = [] 
        for o in ordenes: 
            if o.sosCompletamenteRealizada() and o.sosDeEmpleado(self.empleadoLogueado.legajo):
                orden = {
                    "id" : o.obtenerNumeroDeOrden(),
                    "fechaFinalizacion": o.obtenerFechaFinalizacion(),
                    "estacionSismologica": o.obtenerEstacionSismologica(),
                    "sismografoId": o.obtenerIdentificadorSismografo()
                }
                
                ordenesSinOrdenar.append(orden)

        ordenesOrdenadas = self.ordenarPorFechaDeFinalizacion(ordenesSinOrdenar)
        return ordenesOrdenadas

    def ordenarPorFechaDeFinalizacion(self, ordenesSinOrdenar):
        ordenesOrdenadas = sorted(ordenesSinOrdenar, key=lambda o: o["fechaFinalizacion"])
        return ordenesOrdenadas

    def mostrarOrdCompRealizadas(self, ordenes):
        self.interfaz.mostrarOrdCompRealizadas(ordenes)
        self.interfaz.pedirSeleccionOrdenInspeccion()

    def tomarOrdenDeInspeccionSeleccionada(self, idOrden):
        for o in self.ordenes:
            if o.id == idOrden:
                self.ordenSeleccionada = o
                return o
            
        return None

    def pedirObservacion(self):
        self.interfaz.pedirObservacion()

    def tomarObservacion(self, observacion):
        self.observacionCierre = observacion
        
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

    def tomarComentario(self, comentario, indiceMotivo):
        self.motivos[indiceMotivo]["comentario"] = comentario

    def pedirConfirmacionCierreOrden(self):
        self.interfaz.pedirConfirmacionCierreOrden()

    def tomarConfirmacionCierreOrden(self):
        if self.validarExistenciaObservacion() and self.validarExistenciaMotivoTipo():
            
            self.estadoOrden = self.buscarEstadoCerrada()

            self.fechaHoraActual = self.getFechaHoraActual()

            estadoSismografo = self.buscarFueraDeServicio()

            if self.estadoOrden == None or estadoSismografo == None:
                print("Error obteniendo los estados")
                return False
            
            self.cerrarOrdenInspeccion(self.estadoOrden)
            self.ponerSismografoFueraDeServicio(estadoSismografo)
            
            self.buscarResponsablesReparacion()

            observadores = [interfazNotificacionMail, interfazCCRS]

            self.suscribir(observadores)

            self.notificar()

            self.finCU()

            return True
        else:
            return False
    
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
        ahora = datetime.now()
        return ahora.strftime("%Y-%m-%d %H:%M:%S")

    def buscarFueraDeServicio(self):
        for estado in estados:
            if estado.sosDeSismografo() and estado.sosFueraDeServicio():
                return estado
        
        return None
    
    def cerrarOrdenInspeccion(self, estadoOrden):
        self.ordenSeleccionada.cerrarOrden(self.fechaHoraActual, estadoOrden)

    def ponerSismografoFueraDeServicio(self, estadoSismografo):
        self.ordenSeleccionada.ponerSismografoFueraDeServicio(self.fechaHoraActual, estadoSismografo, self.empleadoLogueado, self.motivos)

    def buscarResponsablesReparacion(self):
        for empleado in empleados:
            if empleado.esResponsableReparacion():
                dominio = empleado.obtenerMail()
                
                self.dominios.append(dominio)

    def enviarCorreo(self,mail):
        interfazNotificacionMail.enviarCorreo(mail)
        
    def enviarNotificacion(self,estadoSismografo):
        sismografoId = self.ordenSeleccionada.obtenerIdentificadorSismografo()
        fecha = self.fechaHoraActual
        motivos = self.motivos
        nombreEstado = estadoSismografo.getNombre()

        interfazCCRS.publicarNotificacion(sismografoId, nombreEstado, fecha, motivos )
    
    def suscribir(self, observadores):
        self.observadores = observadores

    def notificar(self):
        for observador in self.observadores:
            sismografoId = self.ordenSeleccionada.obtenerIdentificadorSismografo()
            nombreEstado = self.estadoOrden.getNombre()

            observador.actualizar(self.dominios, sismografoId, nombreEstado, self.fechaHoraActual, self.motivos)

    def desuscribir(self, observadores):
        nuevosObservadores = []

        for observador in self.observadores:
            if observador not in observadores:
                nuevosObservadores.append(observador)
        
        self.observadores = nuevosObservadores

    # Actualizamos el arreglo de ordenes para que la orden cerrada ya no se vea reflejada 😀
    def finCU(self):
        nuevasOrdenes = self.buscarOrdenesInspeccion()
        
        self.actualizacionSismografo = ""
        self.motivos = []
        self.ordenes = self.filtrarOrdenes()
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.fechaHoraActual = ""
        
        self.mostrarOrdCompRealizadas(nuevasOrdenes)
        print("CU terminado")
    
    def filtrarOrdenes(self):
        ordenesFiltradas = []
        for orden in self.ordenes:
            if orden.obtenerNumeroDeOrden() == self.ordenSeleccionada.obtenerNumeroDeOrden():
                continue
            ordenesFiltradas.append(orden)
        return ordenesFiltradas