import pandas as pd


# datos_con_panda = pd.read_csv(
#     "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_csv\\archivos_csv\\datos_de_ejemplo.csv",
#     sep=",",
#     encoding="utf-8",
# )
# print(datos_con_panda)


# Al ser un data frame, prefiero usar df como variable
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_csv\\archivos_csv\\datos_de_ejemplo.csv",
    names=["name", "lastname", "age", "sex", "txt"],  # Añadimos encabezado
)

nombres = df["name"]
print(nombres)
print("----------------")
print(df)

# Ordenando por un tipo de dato específico
df_ordenado_asc = df.sort_values(by="age")
df_ordenado_desc = df.sort_values(by="age", ascending=False)

print(df_ordenado_asc)
print(df_ordenado_desc)

print("----------------")
# Concatenando dataframes
df2 = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_csv\\archivos_csv\\datos_de_ejemplo.csv",
)
df_concatenado = pd.concat([df, df2])  # Lista con dataframes a concatenar
print(df_concatenado)


# Leer de arriba a abajo
primer_fila = df.head(
    1
)  # Como parametros, nos pide el numero de filas que queremos ver. 0 para el encabezado, 1 para la primera fila etc.
print(primer_fila)

ultimas_filas = df.tail(3)  # Últimas filas del dataframe
print(ultimas_filas)

cantidad_de_filas_y_columnas_totales = df.shape
# Accediendo al atributo shape del objeto df
print(cantidad_de_filas_y_columnas_totales)
# Resultado: tupla con dos valores, que se pueden leer como aprendimos
filas_totales = cantidad_de_filas_y_columnas_totales[0]
columnas_totales = cantidad_de_filas_y_columnas_totales[1]

# Mismos datos, pero ahora usando el despempaquetado de variables
filas_totales, columnas_totales = df.shape
print(filas_totales)
print(columnas_totales)

# Obteniendo información estadística general
df_info = df.describe()
print(df_info)

# Accediendo a datos con loc, primero index de fila, luego columna
dato_especifico_loc = df.loc[3, "age"]
print(dato_especifico_loc)
# Accediendo a dato con iloc, mismo formato, pero solo con indices
dato_especifico_iloc = df.iloc[3, 3]
print(dato_especifico_iloc)
# Accediendo a todos los datos de todas las filas pertenecientes a una columna con loc
apellidos = df.loc[:, "lastname"]

# Accediendo a todos los datos de todas las filas pertenecientes a una columna con iloc
apellidos = df.iloc[:, 1]
print(apellidos)

# Accediendo a los datos de una fila con loc
fila3 = df.loc[2, :]

# Accediendo a los datos de una fila con iloc
fila3 = df.iloc[2, :]
print(fila3)

# Accediendo a filas con la condición de que su edad sea mayor a 30
filas_edad_mayores_a_30 = df.loc[df["age"] > 30, :]
print(filas_edad_mayores_a_30)
