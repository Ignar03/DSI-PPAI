from persistencia.connection import connection

class EstacionesSismologicaRepository:

    def obtenerEstaciones(self):
        conn, cursor = connection()

        estaciones = cursor.execute(
        """
        SELECT * FROM Estaciones
        """
        ).fetchall()

        conn.commit()
        conn.close()
        
        return estaciones
    
    def obtenerEstacionPorCodigo(self, codigoEstacion):
        conn, cursor = connection()

        estacion = cursor.execute(
        """
        SELECT * FROM Estaciones e WHERE codigoEstacion = ?
        """,
        [codigoEstacion]
        ).fetchone()

        conn.commit()
        conn.close()
        
        return estacion
