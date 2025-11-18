from persistencia.repositories.ordenes_repository import OrdenesRepository
from persistencia.services.empleados_service import EmpleadosService
from persistencia.services.estado_service import EstadoService
from persistencia.services.estaciones_service import EstacionesService
from entidades.orden_inspeccion import OrdenDeInspeccion

class OrdenesService:
    def __init__(self):
        self.repository = OrdenesRepository()

    def mapearOrden(self, data):
        empleadoService = EmpleadosService()
        estadoService = EstadoService()
        estacionService = EstacionesService()

        estado = estadoService.obtenerEstadoPorCodigo(data[4])
        empleado = empleadoService.obtenerEmpleadoPorLegajo(data[7])
        estacion = estacionService.obtenerEstacionPorCodigo(data[13])

        orden = OrdenDeInspeccion(
            numeroOrden=data[0], 
            fechaHoraInicio= data[1], 
            fechaHoraCierre=0, 
            fechaHoraFinalizacion=data[2], 
            observacionCierre=data[4], 
            estado=estado, 
            empleado=empleado, 
            estacion=estacion 
        )

        return orden
        
    def obtenerOrdenes(self):
        data = self.repository.obtenerOrdenes()

        ordenes = []

        for fila in data:
            orden = self.mapearOrden(fila)
        
            ordenes.append(orden)

        return ordenes