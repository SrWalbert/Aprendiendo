# Importando sys, librerias por defecto
import sys

# Añadimos a sys una ruta
sys.path.append(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Ejercicios practicos\\Intermedios\\ep_intermedio_3"
)

# Importamos otras funciones
# Importando todo de carpeta funciones, archivo Funciones_usadas

# from Funciones.Funciones_usadas import *
# import Funciones.Otras_funciones

# En vez de usar importar esos dos uno por uno, lo haré con un paquete
import Funciones.Funciones_usadas
import Funciones.Otras_funciones

# Importando del path
# from ep_intermedio_3 import *


print(sys.path)  # Quiero ver el path
print("-----------------")
print(Funciones.__path__)
print("-----------------")
print(Funciones.Funciones_usadas.es_primo(7))

print(Funciones.Otras_funciones.saludar_persona("Xavier"))
# Nos devuelve, además de lo que pedimos, nos ejecuta __name__

print("---------------")
# Si lo que quieres importar no está en tu ruta, importas sys y le agragas la ruta
print(sys.builtin_module_names)
print("-------------")
# print(calculo_fibonacci(90))
