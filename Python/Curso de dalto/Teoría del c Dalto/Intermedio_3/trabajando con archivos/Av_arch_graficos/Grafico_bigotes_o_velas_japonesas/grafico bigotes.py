import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Abriendo archivo
df = pd.read_csv(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_arch_graficos\\Grafico_bigotes_o_velas_japonesas\\Datos_para_G_B_o_G_VJ.csv"
)

# Creando grafico
sns.boxplot(x="categoria", y="valor", data=df)
# Mostrando grafico
plt.show()
