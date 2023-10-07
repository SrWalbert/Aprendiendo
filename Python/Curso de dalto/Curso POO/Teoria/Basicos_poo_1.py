# Ahora que tenemos las herraminetas básicas y sabemos movernos por el código razonablemente bien. Es hora de comenzar.
# POO es un paradigma de la programación, señala que hay clases, objetos, atributos y acciones.

# Si quieres llevar a cabo un proyecto grande será necesario adquirir un paradigma, pues la programación secuencial que hemos estado aplicando hasta ahora no es suficiente. Puede se enredoza llegados un punto.

"Clases y objetos"
# Las clases nos permiten definir todo sobre un objeto
# Usamos pascal-case para trabajar con clases


# Declaramos clase
# class NombreClase:
#     propiedad1 = "valor1"
#     propiedad2 = "valor2"
#     propiedad3 = "valor3"
#     propiedad4 = "valor4"


class CelularAtrEstaticos:
    marca = "Samsung"
    modelo = "s23"
    camara_frotal = "24mp"


# Creando objeto en base a clase, los objetos se guardan en ram
celular1 = CelularAtrEstaticos()
print(celular1.marca)

# Estos son atributos estáticos, es decir que creando más celulares no se modifican sus atributos, se pueden modificar por fuera de la clase. Pero todos los objetos que se creen en esta clase por defecto siempre van a traer esos mismos atributos

# Cuando creamos un objetos estamos creando una instancia de la clase

# Cuando creamos un objeto podemos ver que el susodicho es una propiedad de un objeto mayor: __main__ que es el archivo (módulo) en el que trabajamos


"Atributos"
# nt: los atributos de una clase solo se aplican a sus objetos y no son variables que se puedan buscar independientemente a ellos

# Propiedades y atributos pueden ser usados como sinónimos (?)


# Las propiedades de instancia se llaman así porque las definimos cuando creamos la instancia de una clase.
# Para usarlos, al crear la clase, no le pondremos los parentesis, y le agragamos el método especial '__init__', como aparece en el siguiente ejemplo.
# Cada vez que insaticiemos esta clase, init se va a ejecutar automáticamente
# Self es una forma de hacer referencia a sí mismo, luego los atributos que queremos que tenga


class Celular:
    def __init__(self, la_marca, el_modelo, la_camara):
        # Aquí definimos los atributos. Esta función se aplica automaticamente
        # creando propiedad de self = accediendo a un parámetro (el de arriba)
        # Toda esta función se llama constructora
        self.marca = la_marca
        self.modelo = el_modelo
        self.camara = la_camara


celular_1 = Celular("Samsung", "S23", "48MP")
# es una función que se ejecuta

celular_2 = Celular("Apple", "15 pro", "48MP")

"Métodos"

# Son acciones que se aplican a los objetos
# Todas las funciones que creemos dentro de una clase es un método


class Celular:
    def __init__(self, la_marca, el_modelo, la_camara):
        # Aquí definimos los atributos. Esta función se aplica automaticamente
        # creando propiedad de self = accediendo a un parámetro (el de arriba)
        # Toda esta función se llama constructora
        self.marca = la_marca
        self.modelo = el_modelo
        self.camara = la_camara

    # Los metodos que construyamos deben de tener el parametro self para poder utilizar la notación
    def llamar(self):
        print(f"Estás llamando desde un: {self.marca} {self.modelo}")

    def cortar(self):
        print("Haz cortado la llamanda")


celular_3 = Celular("Samsung", "A12", "2MP")

celular_3.llamar()

# Ejercicio practico en C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Curso POO\Ej_practicos\basicos\e_p_basico_1_poo.py


"Herencia"

# Permite a una clase hija heredar todo lo que tiene una clase padre


class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, te estoy hablando")


# Para que una clase herede los atributos de otra se usan ()
class EmpleadoEjemplo(Persona):
    pass  # Si no quieres definir una clase o una función se usa pass


# Crear un objeto con la clase persona
roberto = EmpleadoEjemplo("Roberto", 32, "México")

print(roberto.edad)
roberto.hablar()


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        # Internamente la función init no está preparada para añadir nuevos valores, para eso se ocupa super().__init__
        # Se le dan todas las propiedades de la clase padre más las propias
        super().__init__(nombre, edad, nacionalidad)  # Aquí lo que queremos que herede
        self.trabajo = trabajo
        self.salario = salario

    # Se pueden sobreescibir métodos y practicamente cualquier cosa


roberto = Empleado("Roberto", 32, "México", "Programador", 300000)
print(roberto.trabajo)

# Esta fue la herencia simple
# Cuando hay más clases hijas dependiendo de una padre se le llama herencia jerarquica


"Herencia Multiple"
# Es cuando una subclase hereda de dos o más superclases


class Artista:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


class ArtistaEmpleado(Empleado, Artista):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario, habilidad) -> None:
        Empleado.__init__(self, nombre, edad, nacionalidad, trabajo, salario)
        Artista.__init__(self, habilidad)

    def presentarse(self):
        print(
            f"Hola me llamo {self.nombre} y {super().mostrar_habilidad()}, trabajo en {self.trabajo}"
        )
        # Se puede usar super().habilidad para acceder a la habilidad desde artisa, esto nos sirve para salvar las reescrituras de las subclases. Es una buena practica llamar desde clase padre, solo cuando es obligatorio o necesario se hace desde la clase hijo como en este ejemplo


jose = ArtistaEmpleado("José", 20, "Chile", "Marketing", 100000, "Pintar")

jose.presentarse()

# Hay funciones que retornan buleanos que nos sirven para verificar si ciertas clases son sub clases o si un objeto es una instancia de alguna clase

es_sub_clase_de = issubclass(ArtistaEmpleado, Artista)
print(es_sub_clase_de)
es_instancia_de = isinstance(jose, ArtistaEmpleado)
print(es_instancia_de)
# Los objetos de las clases más bajas seguirán siendo instancias de las clases más altas

"Continua en Basicos_poo_2.py"
