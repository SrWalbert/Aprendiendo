class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def nombre_y_edad(self):
        print(f"El nombre y la edad es {self.nombre} y {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_(self):
        print(f"El grado es {self.grado}")


oscar = Estudiante("Oscar", 24, "3ro")

oscar.nombre_y_edad()
oscar.grado_()
