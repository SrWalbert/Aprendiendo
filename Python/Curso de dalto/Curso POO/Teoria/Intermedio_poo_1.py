"Polimorfismo"
# El polimorfismo de python es mayormente doferente a como trabaja en otros lenguajes, pues el mismo python en sí ya es muy peculiar

# El polimorfismo es mandar el mismo mensaje a muchos objetos y recibir diferentes respuestas en función de sus propiedades

# EL "polimorfismo en tiempo de ejecución" o "polimorfismo de inclusión" es lo que grosmodo hacen las variables, pues, al menos en python estas pueden ser de diferente tipo


# En otros lengujes de "tipiado" estático se deben de hacer un montón de cosas, como herencias e interfases, pero aquí es más fácil


class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"


gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())


# Otra forma de hacer polimorfismo es el polimorfismo de función
def hacer_sonido(animal):
    print(animal.sonido())


hacer_sonido(perro)

# El polimorfismo de herencia es lo que se comenteba anteriormente (en la linea 9) pues en los leguajes de "tipiado" estático se requiere alguna clase padre que les herede el método algo así como:
# Y esto funciona exactamente igual

# class Animal:
#     def sonido(self):
#         pass


# class Gato(Animal):
#     def sonido(self):
#         return "Miau"


# class Perro(Animal):
#     def sonido(self):
#         return "Guau"


print("-----------\n")
# El polimorfismo de sobrecarga no existe en python por su propiedad de "tipiado" dinámico, dicho polimorfismo es: al definir una variable en una clase, "sobreescribirla" y dependiendo los datos que se introduscan se dará un resultado u otro

# El polimorfismo de coherción, se hace de forma automática, por ejemplo en la suma de un "int" más un "float", pues el resultado de la función suma (+) dará un "float"


# otro ejemplo de este tipo de polimorfismo es:
def recorrer(lista):
    for item in lista:
        print(f"El elemento actual es {item}")


lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = "String a recorrer"
recorrer(lista_1)
recorrer(lista_2)


print("\n-----------\n")

"   Detalles técnicos"
# Tarea investigar "Duck typing", enlaces estáticos y dinámicos, tipo real y tipo declarado
# https://youtu.be/HtKqSJX7VoM?si=QFoggxaNNNuLTVZv&t=6347


"Encapsulamiento"
# Es una forma de proteger ciertas partes del código para que nisiquiera el desarrollador pueda acceder, no existe en python pero si en otros idiomas (los famosos private y public), aunque en python se puede intentar aplicar de otra forma, no son privados de verdad
#


class ClaseDeEjemplo1:
    def __init__(self) -> None:
        self._atributo_x_privado = "valor"
        # El gión bajo (_) al inicio sirve para marcarlo como privado para el desarrollador, es una convención entre la gente del medio. Para hacerlo privado de verdad se usan dos, si lo intentamos ver con print se marca error excepción
        self.__atributo_x_muy_privado = "Valor privado"

    def __metotdo_privado(self):
        return "Esto es privado"
        # Esto es un método privado


objeto_x = ClaseDeEjemplo1()
print(objeto_x._atributo_x_privado)

# En python no su usa la misma terminología que otros lenguajes

# Python, Otros Lenguajes

# publico, publico
# privado (convención), publico
# Muy privado, Seguro/ protegido
# No hay, Muy privado


# El encapsulamiento te permite ocultar la complejidad dentro de la clase en tu código, para hacer más facil usarla
# Proteccion de algunos atributos, y algo de abstracción


"Getter y setter"
# Son formas de acceder (getter) y modificar(setter) a estos atributos/metodos muy privados


class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self.__edad = edad

    # Se añade el get_ , en ambos casos funcionará
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self.__edad

    def set_new_nombre(self, new_nombre):
        self._nombre = new_nombre


persona = Persona("Isaac", 17)
print(persona.get_nombre())
print(persona.get_edad())

persona.set_new_nombre("Walbert")
print(persona.get_nombre())

print("-----------------")

"Decoradores"
# En python un decorador es una función especial que decora a otra
# Toma una función de entrada, le añade código extra y devuelve la función con el código extra


def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a a la función")
        funcion
        print("Después de llamar a la función")

    return funcion_modificada


def saludo_de_ejemplo():
    print("Hola a todos")


# Creo la función decorada con variables
saludo_modificado = decorador(saludo_de_ejemplo())
saludo_modificado()

print("-----------------")


# La forma más facil de hacer esto es así
def mi_decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a a la función")
        funcion
        print("Después de llamar a la función")

    return funcion_modificada


@decorador
def saludo_de_ejemplo_2():
    print("Hola a todos")


saludo_de_ejemplo_2()

# Investigar sobre decoradores


"Continua en Intermedio 2"
