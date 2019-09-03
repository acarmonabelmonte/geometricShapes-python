from abc import abstractmethod
from figure import Figura

class Paralelogramo(Figura):
    @abstractmethod
    def pintar(self): 
        pass