from persistencia.services.ordenes_service import OrdenesService

def ordenesTest():
    service = OrdenesService()

    ordenes = service.obtenerOrdenes()

    print(ordenes)

ordenesTest()