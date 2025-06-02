class InterfazCCRS:
    def __init__(self):
        pass

    def publicarNotificacion(self, sismografoId, estadoSismografo, fechaHoraActual, motivos):
        print(f"[NOTIFICACIÓN ENVIADA CON: {sismografoId,estadoSismografo,fechaHoraActual,motivos}]")

interfazCCRS = InterfazCCRS()