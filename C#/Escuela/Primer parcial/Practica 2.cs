using System;

public class Program
{
    public static void Main()
    {
        //Edad para votar
        Console.WriteLine("Teclea tu edad: ");
        int myAge = Convert.ToInt32(Console.ReadLine());
        int edadParaVotar = 18;
        if (myAge >= edadParaVotar)
        {
            Console.WriteLine("Si puedes votar");
        }
        else
        {
            Console.WriteLine("No puedes votar");
        }

        
        //Saludo segun hora del dia
        Console.WriteLine("Teclea la hora: ");
        int hora = Convert.ToInt32(Console.ReadLine());
        if (hora < 10)
        {
            Console.WriteLine("Buen dia");
        }
        else if (hora < 20 )
        {
            Console.WriteLine("Buenas tardes");
        }
        else
        {
            Console.WriteLine("Buenas noches");
        }
    }
}

