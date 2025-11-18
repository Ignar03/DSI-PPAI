from persistencia.repositories.motivoFueraDeServicio_repository import MotivosFueraDeServicioRepository
from entidades.motivo_fuera_servicio import MotivoFueraServicio
from persistencia.services.motivosTipo_service import MotivosTipoService


class MotivoFueraServicioService:
    def __init__(self):
        self.repository = MotivosFueraDeServicioRepository()
        self.motivoTipoService = MotivosTipoService()

    def obtenerMotivosFueraDeServicio(self):
        data = self.repository.obtenerMotivosFueraDeServicio()
        motivos = []

        for i in data:
            objetoMotivoTipo = self.motivoTipoService.obtenerMotivoTipoPorCodigo(i[2])
            motivo = MotivoFueraServicio(
                codigoMotivo=i[0],
                comentario=i[1],
                motivoTipo=objetoMotivoTipo
            )
            motivos.append(motivo)

        return motivos