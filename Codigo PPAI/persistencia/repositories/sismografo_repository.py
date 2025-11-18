from persistencia.repositories.cambioEstado_repository import CambioEstadoRepository
from persistencia.connection import connection

class SismografosRepository:
   
    def obtenerSismografos(self):
        conn, cursor = connection()

        sismografos = cursor.execute(
        """
        SELECT * FROM Sismografos 
        """
        ).fetchall()

        conn.commit()
        conn.close()

        return sismografos
    
    def obtenerCambiosEstadoDeSismografo(self, codigoSismografo):
        conn, cursor = connection()

        cambiosEstado = cursor.execute(
        """
        SELECT 
        ce.codigoCambioEstado, 
        ce.fechaHoraInicio,
        ce.fechaHoraFin,
        ce.responsableCambio,
        ce.codigoEstado
        FROM CambiosEstadoSismografo ces
        LEFT JOIN CambiosEstado ce ON ce.codigoCambioEstado = ces.codigoCambioEstado
        WHERE codigoSismografo = ? 
        """, [codigoSismografo]
        ).fetchall()

        conn.commit()
        conn.close()

        return cambiosEstado
    
    def modificarSismografo(self, codigoSismografo,fechaInicio,fechaFin,responsable,codigoEstado):
        conn, cursor = connection()

        codigoCambioEstado = CambioEstadoRepository.registrarCambioEstado(fechaInicio,fechaFin,responsable,codigoEstado)

        cursor.execute(
            """
            INSERT INTO CambiosEstadoSismografo (codigoSismografo, codigoCambioEstado) VALUES (?,?)
            """, [codigoSismografo,codigoCambioEstado]
        ).fetchall()

        conn.commit()
        conn.close()