"""
En este archivo se escribe todo lo relacionado con la interfaz gráfica, tanto para 'inputs' como para 'outputs' de información para el usuario final. Dando a la aplicación de: botones y opciones hasta gráficas entre otra visualización de datos.
"""

# Importando los módulos o librerías necesarias
"""Por ahora estaremos trabajando con la librería Tkinder para las interfaces graficas"""
import tkinter

# Desarrollando el programa
"""Iniciando la raíz y configuraciones básicas"""
root = tkinter.Tk()
root.title("Analisis de datos")
root.iconbitmap(bitmap=".\\logo_data_analisis.ico")
root.config()

# Creando un frame
first_frame = tkinter.Frame()
first_frame.pack()
first_frame.config(width=600, height=800)

root.mainloop()
