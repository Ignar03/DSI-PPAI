from persistencia.connection import connection

class MotivosFueraDeServicioRepository:

    def obtenerMotivosFueraDeServicio(self):
        conn, cursor = connection()

        motivosFueraDeServicio = cursor.execute(
        """
        SELECT * FROM MotivoFueraServicio
        """
        ).fetchall()
        
        conn.commit()
        conn.close()

        return motivosFueraDeServicio
