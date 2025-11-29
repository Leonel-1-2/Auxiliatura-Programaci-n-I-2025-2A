class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def leer(self):
        self.ancho = int (input ("Ingrese el ancho del rectangulo: "))
        self.alto = int (input ("Ingrese el alto del rectangulo: "))

    def mostrar(self):
        print(f"Anchura: {self.ancho}")
        print(f"Altura: {self.alto}")

    def area(self):
        area = self.ancho * self.alto
        print (f"El area del rectangulo es: {area}")

    def perimetro(self):
        perimetro = (2 * self.ancho) + (2 * self.alto)
        print (f"El perimetro del rectangulo es: {perimetro}")
    
rectangulo1 = Rectangulo(4, 5)
rectangulo1.leer()
rectangulo1.mostrar()
rectangulo1.area()
rectangulo1.perimetro()