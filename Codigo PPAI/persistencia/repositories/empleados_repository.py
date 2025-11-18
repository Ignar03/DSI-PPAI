from persistencia.connection import connection

class EmpleadosRepository:
    def obtenerEmpleados(self):
        conn, cursor = connection()

        empleados = cursor.execute(
        """
        SELECT e.legajo, e.apellido, e.nombre, e.email, e.telefono, e.nombreRol, r.descripcion FROM Empleados e LEFT JOIN Roles r ON e.nombreRol = r.nombre
        """
        ).fetchall()
        
        conn.commit()
        conn.close()

        return empleados

    def obtenerEmpleadoPorLegajo(self, legajo):
        conn, cursor = connection()

        empleado = cursor.execute(
            """
            SELECT 
            e.legajo, 
            e.apellido, 
            e.nombre, 
            e.email, 
            e.telefono, 
            e.nombreRol, 
            r.descripcion 
            FROM Empleados e LEFT JOIN Roles r ON e.nombreRol = r.nombre
            WHERE legajo = ?
            """, [legajo]
        ).fetchone()
        
        conn.commit()
        conn.close()

        return empleado
        
