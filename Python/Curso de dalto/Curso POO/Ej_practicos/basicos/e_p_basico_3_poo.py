class Animal:
    def __init__(self, especie) -> None:
        self.especie = especie

    def comer(self):
        print(f"El/La {self.especie} está comiendo")


class Mamifero(Animal):
    def __init__(self, especie) -> None:
        super().__init__(especie)

    def amamantar(self):
        print(f"La {self.especie} está amamantando a su cría")


class Ave(Animal):
    def __init__(self, especie) -> None:
        super().__init__(especie)

    def volar(self):
        print(f"El/La {self.especie} está volando")


class Murcielago(Mamifero, Ave):
    def __init__(self, especie) -> None:
        super().__init__(especie)


murcielago = Murcielago("murcielago")

murcielago.comer()
murcielago.amamantar()
murcielago.volar()
