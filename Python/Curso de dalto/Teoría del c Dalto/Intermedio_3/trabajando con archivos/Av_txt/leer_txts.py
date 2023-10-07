mi_archivo_sin_leer = open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\leer_txts.txt",
    encoding="utf-8",
)  # Llamando al archivo con open, asignandolo a la variable

# archivo_leido = mi_archivo_sin_leer.read()  # Leyendo archivo


# En caso de errores de codificación se puede usar, en open, encoding = utf-8


# print(archivo_leido)

print("-----------")

# linea1_archivo = mi_archivo_sin_leer.readline()

# Dentro del parentesis de la función .readline() van la cantidad de caracteres que se quieren leer, si no ha lee toda la linea
# print(linea1_archivo)
# Info: El archivo no se puede leer dos veces (por motivos de seguridad)

# Leyendo lineas
lineas = mi_archivo_sin_leer.readlines()
print(lineas)
# Nos da una lista separanod las lineas
# \n es la forma de dejar un espacio en linea (enter)

# Si son archivos muy grandes puede haber problemas con la ram, usa .readlines() con conciencia.


# Una vez terminaste, le das a cerrar el archivo con .close() , de lo contrario el usuario tendrá problemas abriendo ese archivo, mientras tu código se ejecuta.
mi_archivo_sin_leer.close()

# Si quieres volver a leer deberás usar open(), pero puedes almacenar la información en variables y usarla mientras el archivo permanezca cerrado
