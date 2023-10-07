with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\sobreescribir.txt",
    "w",
    encoding="utf-8",
) as archivo_a_sobreescribir:
    archivo_a_sobreescribir.write(
        "Hola, esta archivo ahora está reescrito.\nTen un buen día."
    )
    print("El archivo se terminó de sobreescribir correctamente")
# Se usa "w" como segundo parametro para tener permiso de escritura, si no encuentra el archivo, lo crea. Importante, el texto que se intruduce se sobreescribe, es decir no guarda la información anterior.


with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\escribir.txt",
    "w",
    encoding="utf-8",
) as archivo_a_sobreescribir_con_writelines:
    archivo_a_sobreescribir_con_writelines.writelines(
        [
            "Cámara carnal, ¿cómo estás?\n",
            "Sobreescribiendo lineas con función .writelines() .\n",
        ]
    )
    archivo_a_sobreescribir_con_writelines.writelines(
        [
            "Sabías que:\n",
            "escribir .wl([a,b]) .wl[b,c] es igual a escribir .wl[a,b,c,d]\n\n",
        ]
    )
    print("escribir.txt reescrito correctamente con .writelines")
# .writelines() es lo contrario a .readlines, te pide una lista para sobreescribir un archivo, si escribes dos writelines() se suman, útil bucles for


# Para escribir en vez de sobreescribir, se usa append es decir "a" en el segundo parámetro de open(), con el mismo .write()
with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\escribir.txt",
    "a",
    encoding="utf-8",
) as archivo_a_escribir:
    for i in range(5):
        archivo_a_escribir.write(
            f"\nLinea {i+1} escrita en el archivo escribir.txt, con ayuda de 'a' en with open()\n"
        )

# ¡En una linea!
# with open(
#     "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\trabajando con archivos\\Av_txt\\Archivos_txts\\texto en una linea.txt",
#     "w",
# ) as txt:
#     txt.write("\n")
#     txt.writelines(map([lambda: i for i in range(5) f"Linea {i+1}\n"]))
#     # for i in range(5):
#     #     txt.write(f"Linea {i+1}\n")
#     print("Se ha escrito las lineas")
