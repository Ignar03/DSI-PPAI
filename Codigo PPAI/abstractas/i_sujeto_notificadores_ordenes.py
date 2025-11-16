from abc import ABC, abstractclassmethod

class ISujetoNotificadorOrdenes(ABC):
    
    @abstractclassmethod
    def __init__(self):
        self.observadores = []

    @abstractclassmethod
    def notificar(self):
        pass
    
    @abstractclassmethod
    def desuscribir(self, observadores):
        pass
    
    @abstractclassmethod
    def suscribir(self, observadores):
        pass