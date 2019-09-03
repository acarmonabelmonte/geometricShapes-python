from figura.triangulo.triangulo import Triangulo
from figura.paralelogramo.rombo import Rombo
from figura.paralelogramo.cuadrado import Cuadrado
from figura.paralelogramo.paralelogramo import Paralelogramo

class Principal(object):
    def main(self):
        # Inicializamos un array para almacenar las figuras instanciadas
        figuras = []
        cadena_paralelogramo = "Recuperamos figuras de tipo paralelogramo"
        cadena_triangulo = "Recuperamos figuras de tipo triángulo"
        
        # Instanciamos las figuras
        trianguloUno = Triangulo()
        cuadradoUno = Cuadrado()
        trianguloDos = Triangulo()
        cuadradoDos = Cuadrado()
        romboUno = Rombo()
        
        # Añadimos las figuras al array
        figuras.extend([trianguloUno, cuadradoUno, trianguloDos, cuadradoDos, romboUno])
        
        # Mostramos las figuras de tipo paralelogramo
        print (cadena_paralelogramo.center(50, "=")) 
        for figura in figuras:
            if isinstance(figura, Paralelogramo):
                figura.pintar()
                
        # Mostramos las figuras de tipo triángulo
        print (cadena_triangulo.center(50, "=")) 
        for figura in figuras:
            if isinstance(figura, Triangulo):
                figura.pintar()
    
if __name__ == "__main__":
    Principal().main()