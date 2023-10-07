import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cofla se graduó y ahora trabaja como programador, pero consigue más dinero de sus otros empleos
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_arch_graficos\\Grafico_de_barras\\Datos_para_G_B_1.csv"
)

# Obten los datos de df y asignalos a un eje x o y
sns.barplot(x="fuente", y="ingresos", data=df)
# Obteniendo el total, sumando todos los ingresos
total_ingresos = df["ingresos"].sum()
# Mostandolo
print(f"Lo que Cofla consigue al final del mes es {total_ingresos} USD")
# Crea y muestra el grafico
plt.show()
