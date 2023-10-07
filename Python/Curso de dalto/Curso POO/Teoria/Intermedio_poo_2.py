# Importando, véase linea 76
from abc import ABC, abstractclassmethod


"Decorador property"

# Nos permite usar getters, setters y deleters


class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self.__edad = edad

    # Se marca el decorador para no tener que usar los parentesis ni el prefijo get_ , set_ en los getters, etc., es decir, dejan de ser funciones y se convierten en propiedades
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self.__edad

    # Para este usaremos un decorador diferente, se accederá a él por medio de variables
    @nombre.setter
    def new_nombre(self, new_nombre):
        self._nombre = new_nombre

    # Para eliminar una propiedad
    @nombre.deleter
    def nombre(self):
        del self._nombre


persona = Persona("Isaac", 17)
print(persona.nombre)
print(persona.edad)

persona.new_nombre = "Walbert"
print(persona.nombre)

del persona.nombre

# A diferencia de la sintaxis vista en el documento anterior, esta sintaxis tiene ventajas, es más limpia, facilidad de trabajo, y flexibilidad en la evolución

print("-------------")


"Abstracción en poo"
# Es el ocultamiento de todo lo complicado al usuario y al desarrollador dejandolos solo con una interfaz simple


class Carro:
    def __init__(self) -> None:
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"
        print("El carro está encendido")

    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Estás conduciendo")


mi_auto = Carro()
mi_auto.conducir()
# El usuario o dev del carro no sabe cómo fuciona el código interno, ni tiene que saberlo, con que pueda aplicarlo está bien

print("-------------")


"Clases abstractas"

# Es como definir una plantilla para que futuras clases hereden sus propiedades, la diferencia es que no pueden salir objetos directamente de la clase abstracta

# Implementar quiere decir definir que instrucciones va a seguir un método

# Vamos a importar del módulo de python abc la metaclase ABC, y el decorador abstractmethod

# Un método abstracto es un método que no va a estar implementado, para que una subclase lo implemente


class People(ABC):
    @abstractclassmethod
    def __init__(self, name, age, sex, ocupation) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.ocupation = ocupation

    @abstractclassmethod
    def do_activity(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.name} y tengo {self.age} años")


class Estudiant(People):
    def __init__(self, name, age, sex, ocupation) -> None:
        super().__init__(name, age, sex, ocupation)

    def do_activity(self):
        print(f"Estoy estudiando {self.ocupation}")


class Worker(People):
    def __init__(self, name, age, sex, ocupation) -> None:
        super().__init__(name, age, sex, ocupation)

    def do_activity(self):
        print("Estoy trabajando")


pedrito = Estudiant("Pedro", 21, "Hombre", "programación")
isaac = Worker("Isaac", 22, "Hombre", "Analista")

pedrito.presentarse()
pedrito.do_activity()

isaac.presentarse()
isaac.do_activity()


# Como ves es como heredar clases, la diferencia es que debes implementar los métodos abstractos que escribiste, de lo contrario el código no funcionará
# Evita errores de "instaciar" clases base
# Se asegura el polimorfismo
