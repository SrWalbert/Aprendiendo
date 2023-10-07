# Importando librerías
# Leer datos de csv
import pandas as pd

# Visualización de datos
import matplotlib.pyplot as plt

# Graficos estadíaticos
import seaborn as sns


# Los gases son señal de malestar estomacal, se registraron la cantidad de gases durante el día, verifica si hay malestar estomacal
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_arch_graficos\\Graficos_Lineales\\Datos_para_G_L_1.csv"
)

# Obten los datos y asignalos a un eje x o y de df
sns.lineplot(x="Fecha", y="Gases", data=df)
# Haz un puntito en el punto que se te indica
plt.plot("01-09", 17, "o")
# Crea y muestra el grafico
plt.show()
