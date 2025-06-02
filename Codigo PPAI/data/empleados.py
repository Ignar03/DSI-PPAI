from entidades.empleado import Empleado
from data.roles import roles

# Por ahora lo hard-codeamos a falta de una base de datos
empleados = [
    Empleado("1111","Perez", "Juan", "juanperez@gmail.com", "3512345678",roles[1] ),
    Empleado("2222","López", "María", "marialopes@gmail.com", "3519876543",roles[0]),
    Empleado("3333","Benavidez", "Jeronimo", "jero@gmail.com", "3515345698",roles[1] ),

]