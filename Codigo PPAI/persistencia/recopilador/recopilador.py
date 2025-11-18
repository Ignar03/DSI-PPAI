from persistencia.services.cambioEstado_service import CambioEstadoService
from persistencia.services.empleados_service import EmpleadosService
from persistencia.services.estaciones_service import EstacionesService
from persistencia.services.estado_service import EstadoService
from persistencia.services.motivosFueraServicio_service import MotivoFueraServicioService
from persistencia.services.motivosTipo_service import MotivosTipoService
from persistencia.services.ordenes_service import OrdenesService
from persistencia.services.sismografo_service import SismografoService
from persistencia.services.usuarios_service import UsuariosService
from persistencia.services.sesion_service import SesionService

empleados = EmpleadosService().obtenerEmpleados()
cambiosEstado = CambioEstadoService().obtenerCambiosEstado()
estaciones = EstacionesService().obtenerEstaciones()
estados = EstadoService().obtenerEstados()
motivosFueraServicio = MotivoFueraServicioService().obtenerMotivosFueraDeServicio()
motivosTipo = MotivosTipoService().obtenerMotivosTipo()
ordenes = OrdenesService().obtenerOrdenes()
sismografos = SismografoService().obtenerSismografos()
usuarios = UsuariosService().obtenerUsuarios()
sesion = SesionService().obtenerSesionActual()


