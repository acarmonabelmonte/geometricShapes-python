# Ejercicio Orientación Objetos en Python
El ejercicio consiste en desarrollar seis pequeñas clases utilizando herencia: **Figura**,
**Paralelogramo**, **Cuadrado**, **Rombo** y **Triángulo**. Y una última clase llamada **Principal**
que simplemente tendrá un pequeño método que recorra una lista.

La jerarquía de las figuras es la siguiente:
![enter image description here](https://lh3.googleusercontent.com/Byt3mOkVbK2SwjNGbVxaygrNztPDo4dKrHJwDzv9_PNi2X0dc-xXq7fNExsmNl1zv8FE5ckkYyk2)

La clase Figura es abstracta y tendrá un método llamado pintar(). El resto de clases
heredarán de Figura (o de sus hijos) y reimplementarán el método pintar. El método
pintar simplemente tiene que imprimir por consola el nombre de la figura.
Por último, la clase Principal tendrá un método main que instanciará una lista de
Figuras en la que meterá la siguiente lista de figuras en este mismo orden: Triángulo,
Cuadrado, Triángulo, Cuadrado y Rombo. A continación hará dos recorridos de la
lista:
1. Recuperará todas las figuras de tipo paralelogramo y para cada una de ellas
hará que ejecute su método pintar().
2. Recuperará todas los triángulos y para cada uno de ellos hará que ejecute su
método pintar().