from persistencia.services.empleados_service import EmpleadosService

def empleadosTest():
    service = EmpleadosService()

    empleados = service.obtenerEmpleados()

    print(empleados)

empleadosTest()