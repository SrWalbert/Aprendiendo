# El c# está muy feo de trabajar, voy a usar python, si no le molesta

# Capturando datos
from numpy import var


while True:
    print("Introduce tus datos. \n")
    try:
        nombre_de_la_escuela = input("Ingresa el nombre de tu escuela: ")
        nombre_del_alumno = input("Igresa tu nombre completo: ")
        edad_del_alumno = input("Ingresa tu edad: ")
        grado_del_alumno = input("Ingresa tu grado: ")
        grupo_del_alumno = input("Ingresa tu grupo: ")
        periodo_del_alumno = input("Igresa tu periodo, el NÚMERO de semestre: ")
        mes = input("En qué mes estás: ")
        materias = ("español", "matematicas", "ingles", "quimica", "fisica")
        calificacion_ = {}
        for materia in materias:
            calificacion_[materia] = input(
                f"Ingresa tu calificación de {materia} del uno al diez: "
            )
            calificacion_[materia] = float(calificacion_[materia])
        
        calificacion_.keys() = calificacion_.values()
        # calificacion_español = input(
        #     "Ingresa tu calificación de español del uno al diez: "
        # )
        # calificacion_matematicas = input(
        #     "Ingresa tu calificación de matematicas del uno al diez: "
        # )
        # calificacion_ingles = input(
        #     "Ingresa tu calificación de inglés del uno al diez: "
        # )
        # calificacion_quimica = input(
        #     "Ingresa tu calificación de química del uno al diez: "
        # )
        # calificacion_fisica = input(
        #     "Ingresa tu calificación de física del uno al diez: "
        # )

        # Convertir a numeros
        edad_del_alumno = int(edad_del_alumno)
    except Exception as e:
        print("Algo salió mal, no metiste tus datos correctamente, inténtalo de nuevo")
        print(f"Tipo de error: {e}")
    else:
        break


# Operaciones para sacar el promedio
promedio = (
    calificacion_español
    + calificacion_matematicas
    + calificacion_fisica
    + calificacion_quimica
    + califcacion_ingles
) / 5

# Rebrobar  o no
if promedio >= 6:
    estatus_del_estudiante = "Aprobado"
else:
    estatus_del_estudiante = "Reprobado"

# Mostrar información

print(
    f"\n---------------------\nNombre del alumno: {nombre_del_alumno}\nEdad:{edad_del_alumno}\nGrado: {grado_del_alumno}\nGrupo: {grupo_del_alumno}\nPeriodo {periodo_del_alumno}\nMes actual: {mes}\n\n\nEspañol. {español}\nMatematicas: {matematicas}\nInglés: {ingles}\nQuímica: {quimica}\nFísica {fisica}\n\nPromedio: {promedio}\nEstado: {estatus_del_estudiante}"
)
