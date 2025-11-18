from persistencia.connection import connection

class UsuariosRepository:
 
    def obtenerUsuarios(self):
        conn, cursor = connection()

        usuarios = cursor.execute(
        """
        SELECT * FROM Usuarios
        """
        ).fetchall()

        conn.commit()
        conn.close()

        return usuarios
    
    def obtenerUsuarioPorNombre(self, nombreUsuario):
        conn, cursor = connection()

        usuario = cursor.execute(
        """
        SELECT * FROM Usuarios WHERE nombre = ?
        """, [nombreUsuario]
        ).fetchone()

        conn.commit()
        conn.close()

        return usuario
