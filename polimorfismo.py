class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describir(self):
        print(f"soy un animal del tipo {type(self).__name__} y soy un {self.especie}")

class Perro(Animal):
    def __init__(self, edad, dueño):
        super().__init__("mamifero", edad)
        self.dueño = dueño
    def hablar(self):
        print("guau guau")
    def moverse(self):
        print("camino en cuatro patas")

class Vaca(Animal):
    def __init__(self, edad):
        super().__init__("mamofero", edad)
    def hablar(self):
        print("muuu")
    def moverse(self):
        print("camino por el pasto")

class Abeja(Animal):
    def __init__(self, edad):
        super().__init__("insecto", edad)
    def hablar(self):
        print("bzzzz")
    def moverse(self):
        print("vuelo por el cielo")
    def picar(self):
        print("picar")

def main():
    perro = Perro(1, "nieve")
    vaca = Vaca(2)
    abeja = Abeja(3)

    animales = [perro, vaca, abeja]

    for animal in animales:
        animal.describir()
        animal.hablar()
        animal.moverse()

        if isinstance(animal, Abeja):
            animal.picar()
        print()

if __name__ == "__main__":
    main()