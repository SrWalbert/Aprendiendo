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


"Duck typing"
# El duck typing es un concepto utilizado en lenguajes de programación como Python para determinar el tipo de un objeto en función de su comportamiento en lugar de su tipo explícito. La idea fundamental detrás del duck typing es que "si camina como un pato y suena como un pato, entonces debe ser un pato". En otras palabras, en lugar de preocuparse por el tipo específico de un objeto, Python se enfoca en lo que el objeto puede hacer o las operaciones que puede realizar.

# En Python, esto significa que no es necesario declarar explícitamente el tipo de una variable o un parámetro de función. En su lugar, Python evalúa el tipo en tiempo de ejecución según cómo se utilizan los objetos y si las operaciones que se realizan en ellos son válidas. Esto permite una flexibilidad significativa en la escritura de código y facilita la reutilización de código, ya que no es necesario preocuparse por los tipos concretos.

# Por ejemplo, si tiene una función que espera un objeto que pueda realizar una operación de suma, simplemente puede pasar cualquier objeto que implemente esa operación, sin importar su tipo real. Si el objeto es un número entero, una cadena o cualquier otra cosa que tenga una operación de suma definida, Python lo aceptará.

# Aquí hay un ejemplo sencillo de duck typing en Python:


def suma(a, b):
    return a + b


# Llamamos a la función con diferentes tipos de objetos
resultado1 = suma(5, 3)  # Enteros
resultado2 = suma("Hola, ", "mundo")  # Cadenas
resultado3 = suma([1, 2], [3, 4])  # Listas

print(resultado1)  # Resultado: 8
print(resultado2)  # Resultado: "Hola, mundo"
print(resultado3)  # Resultado: [1, 2, 3, 4]

# En este ejemplo, la función `suma` no se preocupa por los tipos de `a` y `b`, siempre y cuando puedan sumarse de alguna manera. Esto es un ejemplo de duck typing en acción en Python.

"enlaces estáticos y declarados"

# En el contexto de la programación en Python, los términos "enlace estático" y "enlace dinámico" se utilizan más comúnmente en el contexto de la importación de módulos y la resolución de nombres. Aunque Python es un lenguaje de programación de enlace dinámico, es útil entender estos conceptos para comprender cómo funcionan las importaciones y la resolución de nombres en Python.

# 1. **Enlace Estático:**
#    - En el enlace estático, las referencias a objetos y funciones se resuelven en tiempo de compilación. Esto significa que el enlace se realiza antes de que el programa se ejecute.
#    - En lenguajes de enlace estático, como C o C++, las referencias a funciones y variables globales se resuelven en tiempo de compilación. Esto implica que el código binario resultante contiene direcciones de memoria absolutas para las funciones y variables.
#    - En el enlace estático, si un módulo hace referencia a otro módulo, esta referencia se resuelve y se incorpora directamente en el código compilado. Por lo tanto, cualquier cambio en el módulo referenciado requeriría volver a compilar el programa completo.

# 2. **Enlace Dinámico:**
#    - En el enlace dinámico, las referencias a objetos y funciones se resuelven en tiempo de ejecución, en lugar de en tiempo de compilación.
#    - Python es un lenguaje de enlace dinámico, lo que significa que la resolución de nombres se realiza en tiempo de ejecución. Cuando importas un módulo en Python, el sistema busca y carga el módulo en tiempo de ejecución, y luego puedes acceder a sus objetos y funciones a través de nombres.
#    - Esto permite una mayor flexibilidad y modularidad, ya que los módulos pueden agregarse o modificarse sin necesidad de volver a compilar el programa principal. También facilita la creación de programas más dinámicos y la implementación de características como la reflexión.

# En Python, la resolución de nombres se realiza utilizando el sistema de módulos y el atributo `import`. Cuando importas un módulo, Python busca en los directorios especificados en `sys.path` y carga el módulo en memoria. Luego, puedes acceder a las variables y funciones definidas en ese módulo mediante la notación de punto, como `nombre_modulo.variable` o `nombre_modulo.funcion()`.

# En resumen, Python utiliza un enlace dinámico para la resolución de nombres, lo que significa que las referencias a objetos y funciones se resuelven en tiempo de ejecución, lo que proporciona una mayor flexibilidad y modularidad en comparación con los lenguajes de enlace estático.

"tipo real y declarado"
# En Python, no existe una distinción explícita entre "tipo real" y "tipo declarado" como la que se encuentra en algunos lenguajes de programación estáticamente tipados, como C o Java. En los lenguajes estáticamente tipados, se debe declarar el tipo de una variable antes de utilizarla, y el tipo de una variable es conocido y verificado en tiempo de compilación.

# En Python, es un lenguaje de tipado dinámico y fuertemente tipado, lo que significa que las variables pueden cambiar de tipo durante la ejecución del programa y que los tipos son importantes para el correcto funcionamiento del código, pero no es necesario declarar el tipo de una variable de antemano. En lugar de "tipo real" y "tipo declarado", en Python se habla más comúnmente de "tipo dinámico" y "tipo inferido".

# - **Tipo Dinámico**: En Python, el tipo de una variable es determinado en tiempo de ejecución según el valor al que se le asigne. Esto significa que puedes asignar un valor de un tipo a una variable y luego cambiar el tipo de esa variable asignándole un valor de otro tipo más tarde en el programa.

# Ejemplo:


x = 5  # x es de tipo int (entero)
x = "Hola"  # x ahora es de tipo str (cadena)

# - **Tipo Inferido**: Python infiere automáticamente el tipo de una variable en función del valor que se le asigna. No necesitas declarar explícitamente el tipo de una variable; Python lo determina por sí mismo.

# Python también proporciona funciones y operadores para verificar y convertir tipos cuando sea necesario. Por ejemplo, puedes usar las funciones `type()` para verificar el tipo de una variable y las funciones de conversión como `int()`, `str()`, `float()`, etc., para cambiar el tipo de una variable según sea necesario.

# En resumen, en Python, no se habla comúnmente de "tipo real" y "tipo declarado" como en algunos lenguajes de programación estática, sino más bien de "tipo dinámico" (determinado en tiempo de ejecución) y "tipo inferido" (determinado automáticamente por Python en función del valor asignado). Esto es una de las características clave del tipado dinámico en Python.

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

"Otros decoradores"

# @staticmethod: Se utiliza para definir un método estático en una clase. No recibe una referencia implícita a una instancia.
# @staticmethod
# def ejemplo():
#     pass


# @classmethod: Se usa para definir un método de clase en Python. Recibe la clase como argumento en lugar de la instancia.
# @classmethod
# def ejemplo(cls):
#     pass


# @property: Se utiliza para definir un método como una propiedad, permitiendo el acceso a ella como un atributo.
# @property
# def ejemplo(self):
#     return self._ejemplo


# @abstractmethod: Se utiliza en clases abstractas y asegura que las subclases implementen un método particular.
# from abc import ABC, abstractmethod

# class Ejemplo(ABC):
#     @abstractmethod
#     def metodo_abstracto(self):
#         pass


# @decorador_personalizado: Los decoradores personalizados son funciones que extienden el comportamiento de otras funciones.
# def decorador_personalizado(func):
#     def wrapper(*args, **kwargs):
#         Aquí va la lógica personalizada
#         return func(*args, **kwargs)
#     return wrapper

# @decorador_personalizado
# def funcion_ejemplo():
#     pass


# @lru_cache: Se utiliza para implementar un caché de resultados con tamaño limitado utilizando el algoritmo "Least Recently Used".
# from functools import lru_cache

# @lru_cache(maxsize=32)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


"Continua en Intermedio 2"
