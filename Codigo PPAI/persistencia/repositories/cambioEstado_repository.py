from persistencia.connection import connection

class CambioEstadoRepository:

    def obtenerCambiosEstado(self):
        conn, cursor = connection()

        cambiosEstado = cursor.execute(
        """
        SELECT * FROM CambiosEstado
        """
        ).fetchall()

        conn.commit()
        conn.close()

        return cambiosEstado
    
    def registrarCambioEstado(self, codigoSismografo, fechaInicio, responsable, codigoEstado, fechaFin=0):
        conn, cursor = connection()
        
        cursor.execute("""
            INSERT INTO CambiosEstado (fechaHoraInicio, fechaHoraFin, responsableCambio, codigoEstado)
            VALUES (?, ?, ?, ?)
        """, [fechaInicio, fechaFin, responsable, codigoEstado])

        codigoCambioEstado = cursor.lastrowid 

        print("NUEVO CAMBIO DE ESTADO", codigoCambioEstado)
       
        cursor.execute("""
            INSERT INTO CambiosEstadoSismografo (codigoSismografo, codigoCambioEstado)
            VALUES (?, ?)
        """, [codigoSismografo, codigoCambioEstado])

        conn.commit()
        conn.close()

        return codigoCambioEstado
    
    def actualizarCambioEstado(self, codigoCambioEstado, fechaFin, responsable, codigoEstado):
        conn, cursor = connection()

        cursor.execute("""
            UPDATE CambiosEstado
            SET fechaHoraFin = ?, responsableCambio = ?, codigoEstado = ?
            WHERE codigoCambioEstado = ?
        """, (fechaFin, responsable, codigoEstado, codigoCambioEstado))

        conn.commit()
        conn.close()