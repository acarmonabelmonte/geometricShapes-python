from figura.triangulo.triangulo import Triangulo
from figura.paralelogramo.rombo import Rombo
from figura.paralelogramo.cuadrado import Cuadrado
from figura.paralelogramo.paralelogramo import Paralelogramo

def main():
    # Inicializamos un array para almacenar las figuras instanciadas
    figuras = []
    
    # Instanciamos las figuras
    trianguloUno = Triangulo()
    cuadradoUno = Cuadrado()
    trianguloDos = Triangulo()
    cuadradoDos = Cuadrado()
    romboUno = Rombo()
    
    # Añadimos las figuras al array
    figuras.append(trianguloUno)
    figuras.append(cuadradoUno)
    figuras.append(trianguloDos)
    figuras.append(cuadradoDos)
    figuras.append(romboUno)
    
    # Mostramos las figuras de tipo paralelogramo
    print("Recuperamos todas las figuras de tipo paralelogramo: ")
    for figura in figuras:
        if isinstance(figura, Paralelogramo):
            figura.pintar()
            
    # Mostramos las figuras de tipo triángulo
    print("Recuperamos todas las figuras de tipo triángulo: ")
    for figura in figuras:
        if isinstance(figura, Triangulo):
            figura.pintar()
    
if __name__ == "__main__":
    main()