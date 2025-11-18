from persistencia.connection import connection

class OrdenesRepository:
  
    def obtenerOrdenes(self):
        conn, cursor = connection()

        ordenes = cursor.execute(
        """
        SELECT
        o.numeroOrden,
        o.fechaHoraInicio,
        o.fechaHoraFinalizacion,
        o.observacionCierre,
        e.*,
        em.*,
        es.*
        FROM OrdenesInspeccion o
        LEFT JOIN Estados e ON o.codigoEstado = e.codigoEstado
        LEFT JOIN Empleados em ON o.legajo = em.legajo
        LEFT JOIN Estaciones es ON o.codigoEstacion = es.codigoEstacion 
        """
        ).fetchall()

        conn.commit()
        conn.close()

        return ordenes

    def modificarOrdenes(self, codigoOrden, codigoEstado):
        conn, cursor = connection()

        cursor.execute(
            """
            UPDATE OrdenesInspeccion SET codigoEstado = ? WHERE codigoOrden = ?
            """, (codigoEstado, codigoOrden)
        )

        conn.commit()
        conn.close()