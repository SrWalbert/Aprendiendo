# Dos listas con nombre y apellido optimamente con loop for

# Lista en forma de diccionario
dic_nombres_apellidos = {
    "Juan": "Perez",
    "Felipe": "Trejo",
    "David": "Torres",
    "Angel": "Marinez",
    "Anna": "Moreno",
}

# Dos listas
nombres = ["Juan", "Felipe", "David", "Angel", "Anna"]
apellidos = ["Perez", "Trejo", "Torres", "Martinez", "Moreno"]


with open(
    "C:\\Users\\gertr\\OneDrive\\Escritorio\\Walbert\\VS Code\\Aprendiendo\\Python\\Curso de dalto\\Teoría del c Dalto\\Intermedio_3\\resolviendo problemas de archivos\\problema_txt_1.txt",
    "w",
    encoding="utf-8",
) as archivo_txt:
    # Resolviendo con diccionario
    archivo_txt.writelines("Los datos son:\n\n")
    for nombre, apellido in dic_nombres_apellidos.items():
        archivo_txt.writelines(
            f"Nombre: {nombre}\nApellido: {apellido}\n ------------ \n"
        )
    else:
        print("Texto escrito correctamente con diccionario")

    # Resolviendo con dos listas
    archivo_txt.writelines("\n\n\nLos datos son:\n\n")
    [
        archivo_txt.writelines(f"Nombre: {n}\nApellido: {a}\n ------------ \n")
        for n, a in zip(nombres, apellidos)
    ]
    print("Texto escrito correctamente con dos listas")
