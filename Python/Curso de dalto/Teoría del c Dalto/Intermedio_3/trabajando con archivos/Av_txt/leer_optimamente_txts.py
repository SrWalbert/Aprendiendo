# Para evitar andar usando open() y .close()  python inventó:
with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\leer_txts.txt",
    encoding="utf-8",
) as texto_1:
    print(texto_1.read())
    print("El archivo se abrió y cerro correctamente")

# Mientras se pueda abrir y cerrar el archivo .txt se ejecutará el bloque identado. Importante saber que por defecto viene en modo read
# para asignar una varible se le puede dar "as" y el nombre

# with open(): es más rapido, eficiente, menor código, y con menos errores de excepciones que usar open() solo
