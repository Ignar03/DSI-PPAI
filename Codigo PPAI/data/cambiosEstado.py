from data.estados import estados
from data.motivos import motivos
from entidades.cambio_estado import CambioEstado
from datetime import datetime, timedelta

# Tiempos hard-codeados jajas
ahora = datetime.now()
hace_3_dias = ahora - timedelta(days=3)
hace_2_dias = ahora - timedelta(days=2)
hace_1_dia = ahora - timedelta(days=1)

cambios = [
    CambioEstado(estados[3], hace_3_dias, hace_2_dias, "Usuario A"),
    CambioEstado(estados[4], hace_2_dias, hace_1_dia, "Usuario B"),
    CambioEstado(estados[3], hace_1_dia, "", "Usuario C"),
    CambioEstado(estados[3], hace_3_dias, hace_2_dias, "Técnico 1"),
    CambioEstado(estados[4], hace_2_dias, hace_1_dia, "Técnico 2"),
    CambioEstado(estados[3], hace_1_dia, "", "Técnico 3"), 
]