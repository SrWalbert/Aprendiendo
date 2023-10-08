# juego de fusión


class Personaje:
    def __init__(self, nombre: str, habilidad: str, poder: int) -> None:
        self.nombre = nombre
        self.habilidad = habilidad
        self.poder = poder

    def __add__(self, otro_personaje: object) -> object:
        nuevo_nombre = self.nombre + "-" + otro_personaje.nombre
        nueva_habilidad = self.habilidad + " y " + otro_personaje.habilidad
        nuevo_poder = round(((self.poder + otro_personaje.poder) / 2) ** 2)
        return Personaje(nuevo_nombre, nueva_habilidad, nuevo_poder)

    def __repr__(self) -> str:
        return f"{self.nombre}, (habilidad: {self.habilidad}, poder {self.poder}) "


mecatron = Personaje("Mecatrón", "Fuego santo", 600)
goku = Personaje("Gokú", "Super ki", 200)

nuevo_personaje = mecatron + goku
print(mecatron)
print(goku)
print(nuevo_personaje)
