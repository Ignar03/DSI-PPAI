class Empleado:
    def __init__(self, apellido, mail, nombre, telefono):
        self.apellido = apellido
        self.mail = mail
        self.nombre = nombre
        self.telefono = telefono

    def esResponsableDeReparacion(self):
        # Implementa la lógica real según tu sistema (acá retorna False por defecto)
        return False

    def obtenerMail(self):
        return self.mail

    def tomarNotificacion(self, mensaje):
        # Acción al recibir notificación (podés implementarla a tu gusto)
        print(f"Notificación para {self.nombre}: {mensaje}")
