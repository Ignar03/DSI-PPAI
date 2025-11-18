from persistencia.repositories.motivosTipo_repository import MotivosTipoRepository
from entidades.motivo_tipo import MotivoTipo

class MotivosTipoService:
    def __init__(self):
        self.repository = MotivosTipoRepository()
    
    def obtenerMotivosTipo(self):
        motivos_tipo_filas = self.repository.obtenerMotivoTipo()
        motivos_tipo = []
        for fila in motivos_tipo_filas:
            motivo_tipo = MotivoTipo(
                fila[0],
                fila[1],
                fila[2]
            )
            motivos_tipo.append(motivo_tipo)
        return motivos_tipo
    def obtenerMotivoTipoPorCodigo(self, codigo):
        fila = self.repository.obtenerMotivoTipoPorCodigo(codigo)
        if fila:
            return MotivoTipo(
                fila[0],
                fila[1],
                fila[2]
            )
        return None