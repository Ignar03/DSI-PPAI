class MotivoTipo:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion

    @staticmethod
    def buscarMotivoTipo(lista_motivos, descripcion):
        # Busca un motivo por descripción en una lista de MotivoTipo
        for motivo in lista_motivos:
            if motivo.descripcion == descripcion:
                return motivo
        return None
