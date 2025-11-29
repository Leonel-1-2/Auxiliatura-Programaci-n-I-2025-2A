class Circulo:
    def __init__(self, posx, posy, radio):
        self.posx = posx
        self.posy = posy
        self.radio = radio

    def leer(self):
        self.posx = int(input("Ingrese posición x: "))
        self.posy = int(input("Ingrese posición y: "))
        self.radio = int(input("Ingrese el radio: "))

    def mostrar(self):
        print(f"La posición de x es {self.posx}")
        print(f"La posición de y es {self.posy}")
        print(f"El radio es {self.radio}")

    def area(self):
        area = 3.1416 * self.radio * self.radio
        print (f"El area es: {area}")

    def circunferencia(self):
        circunferencia = 2 * 3.1416 * self.radio
        print (f"La circunferencia es: {circunferencia}")
    
    def diametro(self):
        diametro = (2 * 3.1416 * self.radio)/3.1416
        return diametro
    
circulo1 = Circulo(4, 5, 10)
circulo1.mostrar()
circulo1.area()
circulo1.circunferencia()
dia = circulo1.diametro()
print(f"El diamentro es: {dia}")

print("--------------- Metodos del circulo 2 ---------------")
circulo2 = Circulo(6, 4, 15)
circulo2.mostrar()
circulo2.area()
circulo2.circunferencia()
dia2 = circulo1.diametro()
print(f"El diamentro es: {dia2}")

print("--------------- Sobreescritura ---------------")
circulo1 = circulo2
circulo1.mostrar()
circulo1.leer()
circulo1.mostrar()
circulo1.area()
