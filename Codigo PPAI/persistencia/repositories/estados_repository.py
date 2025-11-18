from persistencia.connection import connection

class EstadosRepository:        

    def obtenerEstados(self):
        conn, cursor = connection()

        estados = cursor.execute(
        """
        SELECT * FROM Estados
        """
        ).fetchall()

        conn.commit()
        conn.close()
        
        return estados

    def obtenerEstadoPorCodigo(self, codigoEstado):
        conn, cursor = connection()

        estado = cursor.execute(
        """
        SELECT * FROM Estados e WHERE e.codigoEstado = ?
        """, [codigoEstado]
        ).fetchone()

        conn.commit()
        conn.close()
        
        return estado