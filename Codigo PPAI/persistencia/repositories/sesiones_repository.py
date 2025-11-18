from persistencia.connection import connection

class SesionesRepository:

    def obtenerSesiones(self):
        conn, cursor = connection()

        sesiones = cursor.execute(
        """
        SELECT * FROM Sesiones
        """
        ).fetchone()

        conn.commit()
        conn.close()

        return sesiones