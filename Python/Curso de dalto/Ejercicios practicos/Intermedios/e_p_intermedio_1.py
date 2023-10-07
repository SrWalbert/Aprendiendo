# El profesor faltó, ordena a los alumnos de mayor a menor, el mayor será sustituto y el menor será asistente


# lista_de_alumnos = {
#     "miguel": 23,
#     "josé": 22,
#     "manuel": 22,
#     "carlos": 23,
#     "santiago": 24,
#     "anna": 21,
#     "ximena": 22,
#     "roberto": 25,
#     "jesús": 24,
#     "maría": 24,
#     "sofía": 23,
#     "julia": 22,
#     "roberto": 23,
#     "luís": 23,
#     "juan": 24,
# }


def obtener_datos_de_compañeros(num_de_companeros):
    lista_de_alumnos = list()
    for i in range(num_de_companeros):
        nombre = input("Ingresa el nombre del alumno: ")
        edad = int(input("Ingrese la edad de alumo: "))
        alumno = nombre, edad
        lista_de_alumnos.append(alumno)
    lista_de_alumnos.sort(key=lambda x: x[1], reverse=True)
    # key= es un parametro opcional en .sort(), dice cómo se debe de ordenar
    asistente = lista_de_alumnos[-1][0]
    profesor = lista_de_alumnos[0][0]
    return asistente, profesor


num_de_alumnos = input("Dame la cantidad de alumnos del grupo: ")

d_asistetne, d_profesor = obtener_datos_de_compañeros(num_de_alumnos)
print(f"El asitente será {d_asistetne} y el profesor {d_profesor}")
