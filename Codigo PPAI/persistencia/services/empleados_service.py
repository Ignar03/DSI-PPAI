from persistencia.repositories.empleados_repository import EmpleadosRepository
from persistencia.services.roles_service import RolesService
from entidades.empleado import Empleado
from entidades.rol import Rol

class EmpleadosService:
    def __init__(self):
        self.repository = EmpleadosRepository()

    def mapearEmpleado(self, data):
        legajo = data[0]
        apellido = data[1]
        nombre = data[2]
        email = data[3]
        telefono = data[4]

        nombreRol = data[5]
        descripcionRol = data[6]
        rol = RolesService().mapearRoles(descripcion= descripcionRol, nombreRol=nombreRol)

        empleado = Empleado(legajo, apellido, nombre, email, telefono, rol)

        return empleado

    def obtenerEmpleados(self):
        data = self.repository.obtenerEmpleados()

        empleados = []

        for fila in data:
            empleado = self.mapearEmpleado(fila)

            empleados.append(empleado)

        return empleados

    def obtenerEmpleadoPorLegajo(self, legajo):
        data = self.repository.obtenerEmpleadoPorLegajo(legajo)

        empleado = self.mapearEmpleado(data)

        return empleado