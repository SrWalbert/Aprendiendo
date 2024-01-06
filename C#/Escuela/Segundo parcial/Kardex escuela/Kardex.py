# El c# está muy feo de trabajar, voy a usar python, si no le molesta
import sys


def main(*args: None) -> int:
    while True:
        print("Introduce tus datos.\n")
        try:
            nombre_de_la_escuela = input("Ingresa el nombre de tu escuela: ")
            nombre_del_alumno = input("Ingresa tu nombre completo: ")
            edad_del_alumno = int(input("Ingresa tu edad: "))
            grado_del_alumno = input("Ingresa tu grado: ")
            grupo_del_alumno = input("Ingresa tu grupo: ")
            periodo_del_alumno = input("Ingresa tu periodo, el NÚMERO de semestre: ")
            mes = input("En qué mes estás: ")

            materias = ("español", "matematicas", "ingles", "quimica", "fisica")
            calificaciones = {}
            for materia in materias:
                calificaciones[materia] = float(
                    input(f"Ingresa tu calificación de {materia} del uno al diez: ")
                )

            promedio = sum(calificaciones.values()) / len(materias)

            estatus_del_estudiante: str = "Aprobado" if promedio >= 6 else "Reprobado"

            print(
                f"\n---------------------\nNombre del alumno: {nombre_del_alumno}\nEdad:{edad_del_alumno}\nGrado: {grado_del_alumno}\nGrupo: {grupo_del_alumno}\nPeriodo {periodo_del_alumno}\nMes actual: {mes}\n\n\nEstado: {estatus_del_estudiante}"
            )

            for materia, calificacion in calificaciones.items():
                print(f"{materia.capitalize()}: {calificacion}")

            print(f"\nPromedio: {promedio}\nEstado: {estatus_del_estudiante}")

            return 0

        except ValueError as e:
            print(
                "Algo salió mal, no metiste tus datos correctamente, inténtalo de nuevo"
            )
            print(f"Tipo de error: {e}")


if __name__ == "__main__":
    sys.exit(main())
