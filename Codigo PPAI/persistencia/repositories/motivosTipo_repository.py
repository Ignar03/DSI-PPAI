from persistencia.connection import connection

class MotivosTipoRepository:
  
    def obtenerMotivoTipo(self):
        conn, cursor = connection()

        motivos = cursor.execute(
        """
        SELECT * FROM MotivoTipo
        """
        ).fetchall()

        conn.commit()
        conn.close()
        
        return motivos
    
    def obtenerMotivoTipoPorCodigo(self, codigoMotivoTipo):
        conn, cursor = connection()

        motivo = cursor.execute(
        """
        SELECT * FROM MotivoTipo WHERE codigoMotivoTipo = ?
        """,
        (codigoMotivoTipo,)
        ).fetchone()

        conn.commit()
        conn.close()
        
        return motivo

