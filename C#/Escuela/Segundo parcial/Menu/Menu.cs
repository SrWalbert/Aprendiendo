using System;
namespace Manu
{
    class Program
    {
        static void Main(string[] args)
        {
            // Información
            Console.WriteLine("|__________Menu de hamburguesas__________|\n|1.Hamburguesas.......................$50|\n|2.Pizza.............................$30|\n|3.Agua..............................$50|\n|4.Refresco..........................$15|\n|5.Papas.............................$15|");

            // Para que seleccionen qué van a pedir
            Console.WriteLine("¿Qué vas a pedir?\n");

            while (true)
            {
                int pedido;
                try
                {
                    pedido = Convert.ToInt32(Console.ReadLine());
                    if (pedido > 5)
                    {
                        throw new Exception();
                    }
                    break;
                }
                catch (Exception e)
                {
                    if (e.GetType() == typeof(FormatException))
                    {
                        Console.WriteLine("Introduce el dato correctamente");
                    }
                    else
                    {
                        Console.WriteLine("Tu número es superior a 5");
                    }
                }
            }

            Console.WriteLine("Estamos procesando tu pedido");

            switch (pedido)
            {
                case 1:
                    Console.WriteLine("Se están preparando tus hamburguesas");
                    break;
                case 2:
                    Console.WriteLine("Se está preparando tu pizza");
                    break;
                case 3:
                    Console.WriteLine("Aquí está tu agua");
                    break;
                case 4:
                    Console.WriteLine("Aquí está tu refresco");
                    break;
                case 5:
                    Console.WriteLine("Aquí están tus papas");
                    break;
                default:
                    break;
            }
        }
    }

}
