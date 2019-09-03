from figura.paralelogramo.paralelogramo import Paralelogramo

class Cuadrado(Paralelogramo):
    # sobrecribiendo método abstracto
    def pintar(self): 
        print("Cuadrado") 
        