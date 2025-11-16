from abc import ABC, abstractclassmethod

class IObservadorNotificacionOrdenes(ABC):
    
    @abstractclassmethod
    def actualizar(self, dominio, idSismografo, nombreEstado, fechaHoraActual, motivos):
        pass
    
