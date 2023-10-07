"Módulos"

# Un módulo es cualquier archivo .py, desde un módulo se puede llamar, cambiar, crear, cambiar rutas, acceder a paquetes.

# Hay varios tipos de módulos, los que te da python, que vienen programados en c.
# Los third-party modules, que son de tercetoros y creados por la comunidad, y los modulos propios (own modueles)

# Se usa import, y las funciones funcionarán como métodos
# Véase más en C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c. Dalto\Avanzado_Modulos

"Enrutamiento"
# Véase enrutamiento en C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c. Dalto\Avanzado_Enrutamiento

"Paquetes"
# Un modulo es un archivo .py , los paquetes son muchos de esos archivos python
# Para que python lo reconozca como paquete se usa un archivo python distintivo (No necista tener nada dentro) llamado __init__.py

# Si hay un subpaquete dentro de un paquete, y lo quieres llamar, debe de tener la carpeta __init__.py
# Tambien en capeta de enrutamiento

"Manipulación de archivos .txt"
# Un archivo es un contenedor o conjnto de datos de datos, también tienen un formato, que se da por su extención (eg. .txt , .docx , .py)

# .txt es un archivo de texto plano
# Ejercicios en la ruta C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c. Dalto\Avanzado\av_txt

"Manipulación de archivos .csv"

# .csv significa valores separados con comas, debe de tener todos los regulares.
# Se puede usar la librería csv, pero es mejor y más profesional usar pandas.
# En ciencia de datos, jupiternotebook se usa mucho


"Slicing"
# Una forma fácil de recorrer elementos en una cadena es usando slicing, es decir, al poner el index se puede elegir entre que valores usar.

cadena = "0123456789"
print(cadena[5])  # Accedemos al sexto elemento de la cadena
print("----------")
print(
    cadena[3:8]
)  # Accedemos desde el cuarto hasta el octavo elemento de la cadena (el último valor no está incluido)

"Trabajando con archivos y resolviendo problemas"
# Vease en C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\resolviendo problemas de archivos

# Forma de usar for en una linea:
# [
#     archivo_txt.writelines(f"Nombre: {n}\nApellido: {a}\n ------------ \n")
#     for n, a in zip(nombres, apellidos)
# ]
# Primero la instrucción a repetir, y luego el for normal

"Aprendiendo más de la libreria pandas y trabajando con csv en"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\trabajando con archivos\resolviendo problemas de archivos\problema_csv_1.py

"Archivos graficos lineales en"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\trabajando con archivos\Av_arch_graficos\Graficos_Lineales\Intro_a_G_L.py

"Archivos graficos de barras en"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\trabajando con archivos\Av_arch_graficos\Grafico_de_barras\Grafico de barras.py

"Archivos graficos de dispersión en"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\trabajando con archivos\Av_arch_graficos\Grafico_de_dispersion\Grafico de dispersion.py

"Archivps de bigotes o velas japonesas en"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Avanzado\trabajando con archivos\Av_arch_graficos\Grafico_bigotes_o_velas_japonesas\grafico bigotes.py

"Para leer archivos muy grandes con pandas"
# Puede que los archivos de datos sean muy grandes y .read_csv() no sea suficiente, por eso utilizamos

import pandas as pd  # Ten encuenta que importarlo a estas alturas del codigo es para la demostración, no debe hacerse en un archivo real.


def read_csv_in_chunks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name, chunk_size=1000)):
        print("Chunk#{}".format(1))
        print(chunk)


# read_csv_in_chunks("C:file\\path")

"Introducción a POO"

# Es una forma de programar de la que salen las clases y lo objetos
# Un objeto es la insatancia de una clase
# Una clase es como una plantilla que predefinimos, que definen las caracteristicas y los comportamientos de los objetos que pertenecen a esa clase.

"Continua en POO y avanzado_1"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Curso POO

# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\avanzado_1.py
