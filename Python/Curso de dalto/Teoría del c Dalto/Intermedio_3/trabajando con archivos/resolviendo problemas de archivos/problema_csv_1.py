import pandas as pd

# Concigna: Cambia los tipos de datos de una columna
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\resolviendo problemas de archivos\\problema_csv_1.csv",
    names=["Nombre", "Apellido", "edad"],
    # skiprows=1,
    # quotechar='"',
)
df["edad"] = df["edad"].astype(str)
# Verificando que sean strings
print(type(df["edad"][1]))

# Reemplazando elemento

df["Apellido"].replace("Dalto", "Maestro", inplace=True)
print(df)

print("----------------")
# A nuestro csv le faltan dos datos en la útlima fila, para borrarla usamos:
df = df.dropna()
# Para borrar filas con datos repetidos usamos
df = df.drop_duplicates()
print(df)


# Pasar en limpio, crea un archivo con los datos que hemos estado cambiando en limpio
df.to_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\resolviendo problemas de archivos\\prob_csv_1_Limpio.csv"
)
