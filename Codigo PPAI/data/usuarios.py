from entidades.usuario import Usuario
from entidades.empleado import Empleado
from data.empleados import empleados

# Por ahora lo hard-codeamos a falta de una base de datos
usuarios = [
    Usuario("pj","12345", empleados[0]),
    Usuario("marialop","12345", empleados[1])
]