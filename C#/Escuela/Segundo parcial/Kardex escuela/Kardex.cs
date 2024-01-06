using System;
namespace Kardex
{
    public class NewProgram
    {
        public static void Main(string[] args)
        {
            string nombreDeLaEscuela, nombreDelAlumno, gradoDelAlumno, grupoDelAlumno, periodoDelAlumno, mes;
            int edadDelAlumno;
            float calificacionEspanol, calificacionMatematicas, calificacionIngles, calificacionQuimica, calificacionFisica;

            while (true)
            {
                Console.WriteLine("Introduce tus datos. \n");
                try
                {
                    Console.Write("Ingresa el nombre de tu escuela: ");
                    nombreDeLaEscuela = Console.ReadLine();

                    Console.Write("Ingresa tu nombre completo: ");
                    nombreDelAlumno = Console.ReadLine();

                    Console.Write("Ingresa tu edad: ");
                    edadDelAlumno = int.Parse(Console.ReadLine());

                    Console.Write("Ingresa tu grado: ");
                    gradoDelAlumno = Console.ReadLine();

                    Console.Write("Ingresa tu grupo: ");
                    grupoDelAlumno = Console.ReadLine();

                    Console.Write("Ingresa tu periodo, el NÚMERO de semestre: ");
                    periodoDelAlumno = Console.ReadLine();

                    Console.Write("En qué mes estás: ");
                    mes = Console.ReadLine();

                    // Calificaciones
                    Console.Write("Ingresa tu calificación de español del uno al diez: ");
                    calificacionEspanol = float.Parse(Console.ReadLine());

                    Console.Write("Ingresa tu calificación de matemáticas del uno al diez: ");
                    calificacionMatematicas = float.Parse(Console.ReadLine());

                    Console.Write("Ingresa tu calificación de inglés del uno al diez: ");
                    calificacionIngles = float.Parse(Console.ReadLine());

                    Console.Write("Ingresa tu calificación de química del uno al diez: ");
                    calificacionQuimica = float.Parse(Console.ReadLine());

                    Console.Write("Ingresa tu calificación de física del uno al diez: ");
                    calificacionFisica = float.Parse(Console.ReadLine());

                    // Se rompe el bucle si todos los datos se ingresan correctamente
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Algo salió mal, no metiste tus datos correctamente, inténtalo de nuevo");
                    Console.WriteLine($"Tipo de error: {e}");
                }
            }

            float promedio = (calificacionEspanol + calificacionMatematicas + calificacionFisica + calificacionQuimica + calificacionIngles) / 5;
            string estatusDelEstudiante = promedio >= 6 ? "Aprobado" :  "Reprobado";

            Console.WriteLine($"\n---------------------\nNombre del alumno: {nombreDelAlumno}\nEdad: {edadDelAlumno}\nGrado: {gradoDelAlumno}\nGrupo: {grupoDelAlumno}\nPeriodo {periodoDelAlumno}\nMes actual: {mes}\n\n\nEspañol: {calificacionEspanol}\nMatemáticas: {calificacionMatematicas}\nInglés: {calificacionIngles}\nQuímica: {calificacionQuimica}\nFísica: {calificacionFisica}\n\nPromedio: {promedio}\nEstado: {estatusDelEstudiante}");
        }
    }
}


