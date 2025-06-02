class InterfazNotificacionMail:
    def __init__(self):
        pass

    def enviarCorreo(self, mail):
        # Es un print a falta de una API de mails 
        print(f"[MAIL ENVIADO A {mail}]")

interfazNotificacionMail = InterfazNotificacionMail()