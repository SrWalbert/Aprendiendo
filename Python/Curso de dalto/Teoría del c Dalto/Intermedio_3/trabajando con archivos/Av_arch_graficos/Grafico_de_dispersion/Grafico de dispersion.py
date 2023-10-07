import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cofla se graduó y ahora trabaja como programador, pero consigue más dinero de sus otros empleos, he aquí la relacion entre el tiempo empleado y su ganancia
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_arch_graficos\\Grafico_de_dispersion\\Datos_para_G_D_1.csv"
)

# Obten los datos de df y asignalos a un eje x o y
sns.scatterplot(x="tiempo", y="dinero", data=df)

# Crea y muestra el grafico
plt.show()
