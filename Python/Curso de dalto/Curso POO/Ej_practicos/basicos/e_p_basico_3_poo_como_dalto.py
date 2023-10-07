class Animal:
    def comer(self):
        print("El animal está comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando a su cría")


class Ave(Animal):
    def volar(self):
        print("El animal está volando")


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()
