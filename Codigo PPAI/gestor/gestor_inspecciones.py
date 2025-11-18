from persistencia.recopilador.recopilador import sesion as actualSesion
from persistencia.recopilador.recopilador import ordenes
from persistencia.recopilador.recopilador import motivosTipo as motivos
from persistencia.recopilador.recopilador import estados
from persistencia.recopilador.recopilador import empleados
from persistencia.recopilador.recopilador import sismografos
from persistencia.services.empleados_service import EmpleadosService
from abstractas.i_sujeto_notificadores_ordenes import ISujetoNotificadorOrdenes
from datetime import datetime
from interfaz.interfaz_notificacion_mail import interfazNotificacionMail
from interfaz.interfaz_ccrs import interfazCCRS

class GestorInspecciones(ISujetoNotificadorOrdenes):
    def __init__(self, interfaz):
        self.actualizacionSismografo = ""
        self.motivosSeleccionados = []
        self.ordenes = ordenes
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.fechaHoraActual = ""
        self.interfaz = interfaz
        self.observadores = []
        self.dominios = []
        self.estadoOrden = None

        self.legajoEmpleadoLogueado = self.buscarEmpleadoLogueado()
        ordenesCompRealizadas = self.buscarOrdenesInspeccion()
        self.mostrarOrdCompRealizadas(ordenesCompRealizadas)

    def buscarEmpleadoLogueado(self):
        usuarioActual = actualSesion.getUsuarioActual()
        legajoEmpleadoLogueado = usuarioActual.obtenerLegajo()

        return legajoEmpleadoLogueado

    def buscarOrdenesInspeccion(self):      
        ordenesSinOrdenar = [] 

        for o in ordenes:
            
            if o.sosCompletamenteRealizada() and o.sosDeEmpleado(self.legajoEmpleadoLogueado):
                orden = {
                    "id" : o.obtenerNumeroDeOrden(),
                    "fechaFinalizacion": o.obtenerFechaFinalizacion(),
                    "estacionSismologica": o.obtenerEstacionSismologica(),
                    "sismografoId": o.obtenerIdentificadorSismografo(sismografos).getCodigo()
                }

                print(o.obtenerFechaFinalizacion())
                
                ordenesSinOrdenar.append(orden)

        ordenesOrdenadas = self.ordenarPorFechaDeFinalizacion(ordenesSinOrdenar)
        return ordenesOrdenadas

    def ordenarPorFechaDeFinalizacion(self, ordenesSinOrdenar):
        print(ordenesSinOrdenar)
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

        self.motivosSeleccionados.append({"motivo": motivos[indiceMotivo], "comentario": ""})
        self.interfaz.pedirComentario(motivos, indiceMotivo)

    def tomarComentario(self, comentario, indiceMotivo):
        self.motivosSeleccionados[indiceMotivo]["comentario"] = comentario

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
        if len(self.motivosSeleccionados) == 0:
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
        self.ordenSeleccionada.ponerSismografoFueraDeServicio(self.fechaHoraActual, estadoSismografo, actualSesion.getUsuarioActual(),motivos, self.motivosSeleccionados, sismografos)

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
        motivos = self.motivosSeleccionados
        nombreEstado = estadoSismografo.getNombre()

        interfazCCRS.publicarNotificacion(sismografoId, nombreEstado, fecha, motivos )
    
    def suscribir(self, observadores):
        self.observadores = observadores

    def notificar(self):
        for observador in self.observadores:
            sismografoId = self.ordenSeleccionada.obtenerIdentificadorSismografo(sismografos).getCodigo()
            nombreEstado = self.estadoOrden.getNombre()

            observador.actualizar(self.dominios, sismografoId, nombreEstado, self.fechaHoraActual, self.motivosSeleccionados)

    def desuscribir(self, observadores):
        nuevosObservadores = []

        for observador in self.observadores:
            if observador not in observadores:
                nuevosObservadores.append(observador)
        
        self.observadores = nuevosObservadores
    # actualiza al sismógrafo de la ES como fuera de servicio, asociando al nuevo estado los motivos seleccionados por el 
    # RI, la fecha y hora del sistema como fecha en la que el sismógrafo deja de estar inhabilitado por inspección para estar fuera 
    # de servicio y el RI logueado responsable del cierre.

    # 1. Crear un nuevo cambio de estado con los nuevos motivos asociados, fechas y asociarlo al sismografo 👍
    # 2. Setear fechahorafin del cambio de estado viejo y cambiar el estado a "Fuera de servicio" 👍

    def finCU(self):
        # Recargar datos desde la base
        from persistencia.services.ordenes_service import OrdenesService
        from persistencia.services.sismografo_service import SismografoService

        self.ordenes = OrdenesService().obtenerOrdenes()  # << recarga fresca
        nuevosSismografos = SismografoService().obtenerSismografos()
        sismografos.clear()
        sismografos.extend(nuevosSismografos)

        nuevasOrdenes = self.buscarOrdenesInspeccion()

        self.actualizacionSismografo = ""
        self.motivosSeleccionados = []
        self.ordenSeleccionada = None
        self.observacionCierre = ""
        self.fechaHoraActual = ""

        self.mostrarOrdCompRealizadas(nuevasOrdenes)
        self.filtrarOrdenes()



        print("CU terminado")

    # def finCU(self):
    #     nuevasOrdenes = self.buscarOrdenesInspeccion()

    #     self.actualizacionSismografo = ""
    #     self.motivosSeleccionados = []
    #     # self.ordenes = self.filtrarOrdenes()
    #     self.ordenes = []
    #     self.ordenSeleccionada = None
    #     self.observacionCierre = ""
    #     self.fechaHoraActual = ""
        
    #     self.mostrarOrdCompRealizadas(nuevasOrdenes)
    #     print("CU terminado")
    
    def filtrarOrdenes(self):
        ordenesCompRealizadas = self.buscarOrdenesInspeccion()
        self.mostrarOrdCompRealizadas(ordenesCompRealizadas)