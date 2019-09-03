from abc import abstractmethod
from figura.figura import Figura

class Paralelogramo(Figura):
    @abstractmethod
    def pintar(self): 
        pass