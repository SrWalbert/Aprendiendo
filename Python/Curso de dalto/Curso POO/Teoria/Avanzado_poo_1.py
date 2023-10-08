# Importando para la linea 123
from abc import ABC, abstractclassmethod

"Principios Solid"
# Hay que hacerse la pregunta de si el programa va a crecer más, o solo es una prueba, pues en caso de lo primero habrá que pensar en como se expandirá y los posibles hechos futuros, como nuevas versiones, librerias que quedan obsoletas o mejores formas de hacer las cosas

# 1 Mantenibilidad: debe de ser fácil de mantener y modificar de manera organizada. Con estructura clara y buenas prácticas
# 2 Reusabilidad: Se debe diseñar de tal forma que todos los componentes sean reutilizables (modulos, clases, funciones)
# 3 Legibilidad: Debe ser fácil de leer para cualquier otro desarrollador, comentar, convenciones de estilo entre otras buenas prácticas
# 4 Extencibilidad: Tiene que poder extenderse sin afectar su funcionamiento

# Los principios solid nos ayudan a todo esto, debes de seguirlos para poder hacer código de calidad.

"Principio de responsabilidad única"
# Una clase debe de tener solo una tarea o responsabilidad a ejercer, si tiene más, se debe de separar en dos. Esta clase no debe de depender de otras clases para realizar su tarea


# Ejercicio SRP:

# Carro se encarga de movimiento, lo demás se lo dejamos a otras clases


# Se encarga del llenado vaciado y verificación del combustible
class TanqueDeCombustible:
    def __init__(self, cantidad_inicial: int) -> None:
        self.combustible = cantidad_inicial

    def cargar_combustible(self, cantidad_de_combustible: int) -> float:
        self.combustible += cantidad_de_combustible

    def ver_combustible(self) -> float:
        return self.combustible

    def usar_combustible(self, a_gastar: float) -> float:
        self.combustible -= a_gastar


class Carro:
    def __init__(self, tanque) -> None:
        self.posision = 0
        self.tanque = tanque

    def mover(self, distancia: int) -> str:
        if self.tanque.ver_combustible() >= distancia / 2:
            self.posision += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"El carro se ha movido {distancia}")
        else:
            print("El carro no tiene suficiente combustible")


tanque1 = TanqueDeCombustible(100)
autito = Carro(tanque1)

autito.mover(64)


# Principio OCP (principo de obierto-cerrado)

# Dice que las entidades de software deben de estar abiertas para la extensión y cerradas para la modificación
# En vez de crear una clase y andar modificandola, mejor se parte en subclases más chicas, que no se necesiten cambiar (tanto), abierto a expandir, cerrado a modificar


class Notificador:
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self) -> None:
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def notificar(self) -> str:
        print(f"Enviando mensaje por email a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def notificar(self) -> str:
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")


# Principio de Liskov (LSP)
# Las subclases deben de ser poder hacer lo mismo o más que sus clases madre


# Esto puede traer errores


# class Ave:
#     def volar(self):
#         print("Volando")


# class Pingüino(Ave):
#     def volar(self):
#         print("No puede volar")


# def hacer_volar(ave=Ave):
#     return ave.volar()


# hacer_volar(Pingüino())


# Por esos se prefiere
class Ave:
    pass


class AveVoladora:
    def volar(self) -> str:
        print("Esoy volando")


class AveNoVoladora(Ave):
    pass


# Principio de segregación de la interfaz (ISP)
# Es no obligar al cliente a usar interfaces que no utiliza


# Ejemplo de como no se debe hacer
# class Trabajador(ABC):
#     @abstractclassmethod
#     def comer(self):
#         pass

#     @abstractclassmethod
#     def dormir(self):
#         pass

#     @abstractclassmethod
#     def trabajar(self):
#         pass


# class TrabajadorHumano(Trabajador):
#     def comer(self):
#         print("El trabajador está comiendo")

#     def dormir(self):
#         print("El trabajador está durmiendo")

#     def trabajar(self):
#         print("El trabajador está trabajando")


# class Robot(Trabajador):
#     def trabajar(self):
#         print("La máquina está trabajando")


# robot = Robot()


# Se debe hacer así
class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass


class Comensal(ABC):
    @abstractclassmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comensal, Durmiente):
    def comer(self):
        print("El trabajador está comiendo")

    def dormir(self):
        print("El trabajador está durmiendo")

    def trabajar(self):
        print("El trabajador está trabajando")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")


# Principio de inversión de dependencias (DIP)
# Establece:
# 1.- Los modulos de alto nivel no tienen que depender de los de bajo nivel, si no que ambos deben depender de las abstracciones
# 2.- Las abstracciones no deben depender de los detalles, al contrario: los detalles deben depender de las abstracciones

# De esta manera las clases de alto nivel (que se encarga de la logica) se mantiene independientes de las de bajo nivel (que atienden tareas muy especificas)

# Facilita que las implementaciones no rompan todo el código, además de ayudar en el testing


# Ejemplo


# class DiccionarioDePalabras:
#     def verificar_palabra(self, palabra) -> bool:
#         # código para verificar
#         pass


# class CorrectorOrtografico:
#     def __init__(self) -> None:
#         self.diccionario = DiccionarioDePalabras()

#     def corregir_texto(self, texto) -> str:
#         # codigo para corregir textos con diccionario
#         pass


# Al usar codigo que depende de lo de arriva, cualquier cambio desde arriva puede romper, o como minimo afectará mucho lo de abajo, no se debe de depender de una interfaz como la del ejemplo para una interfaz más grande e importante como es el correctorortografico


# Lo correcto sería:
class VerificadorOrtográfico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        pass


class Diccionario(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Codigo para verificar palabra
        pass


# de esta forma podemos añadir
class ServicioOnline(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabra
        pass


class CorrectoOrtográfico:
    def __init__(self, verificador) -> None:
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Usamos verificador para corregir texto
        pass
