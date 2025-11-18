from persistencia.connection import connection

class RolesRepository:
    def obtenerRoles(self):
        conn, cursor = connection()

        roles = cursor.execute(
        """
        SELECT * FROM Roles
        """
        ).fetchall()

        conn.commit()
        conn.close()

        return roles