import csv

with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_csv\\archivos_csv\\datos_de_ejemplo.csv"
) as archivo_de_datos:
    # print(archivo_de_datos.read())
    # Forma nativa de leer el archivo, pero nosotros usaremos una librería.

    # Leyendo datos con librería csv
    data_reader = csv.reader(archivo_de_datos)
    for row in data_reader:
        print(row)


# Nosotros usaremos la librería pandas
