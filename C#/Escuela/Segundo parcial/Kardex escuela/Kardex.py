# El c# está muy feo de trabajar, voy a usar python, si no le molesta

# Capturando datos
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
        calificacion_español = input(
            "Ingresa tu calificación de español del uno al diez: "
        )
        calificacion_matematicas = input(
            "Ingresa tu calificación de matematicas del uno al diez: "
        )
        calificacion_ingles = input(
            "Ingresa tu calificación de inglés del uno al diez: "
        )
        calificacion_quimica = input(
            "Ingresa tu calificación de química del uno al diez: "
        )
        calificacion_fisica = input(
            "Ingresa tu calificación de física del uno al diez: "
        )

        # Convertir a numeros
        edad_del_alumno = int(edad_del_alumno)
        calificacion_español = float(calificacion_español)
        calificacion_matematicas = float(calificacion_matematicas)
        calificacion_ingles = float(calificacion_ingles)
        calificacion_quimica = float(calificacion_quimica)
        calificacion_fisica = float(calificacion_fisica)
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
    + calificacion_ingles
) / 5

# Rebrobar  o no
if promedio >= 6:
    estatus_del_estudiante = "Aprobado"
else:
    estatus_del_estudiante = "Reprobado"

# Mostrar información

print(
    f"\n---------------------\nNombre del alumno: {nombre_del_alumno}\nEdad:{edad_del_alumno}\nGrado: {grado_del_alumno}\nGrupo: {grupo_del_alumno}\nPeriodo {periodo_del_alumno}\nMes actual: {mes}\n\n\nEspañol. {calificacion_español}\nMatematicas: {calificacion_matematicas}\nInglés: {calificacion_ingles}\nQuímica: {calificacion_quimica}\nFísica {calificacion_fisica}\n\nPromedio: {promedio}\nEstado: {estatus_del_estudiante}"
)
