using System;

public class Program
{
    public static void Main()
    {
        
        //Constantes
        int porcentajeDescuento=20;
        
        //variables de lectura de datos
        string nombre, direccion, mes;
        int kw =0,valor_kw =0;
        
        //Variables de operacion
        float totalPagar = 0,subTotal = 0, valorDescuento=0,valorConsumo=0;

        //Lectura de la información suministrada por el usuario
        Console.WriteLine("*** PROGRAMA DE FACTURA DE CONSUMO DEL SERVICIO DE ENERGÍA ***");
        Console.WriteLine("***                ELECTRIFICADORA AZUL                ***\n");
        
        Console.WriteLine("* Escriba el nombre del propietario de la vivienda:");
        nombre=Console.ReadLine();
        
        Console.WriteLine("\n* Escriba la dirección de la vivienda:");
        direccion=Console.ReadLine();		

        Console.WriteLine("\n* Escriba el mes del recibo facturado:");
        mes=Console.ReadLine(); 
        
        Console.WriteLine("\n* Escriba el numero de KW de este mes:");
        kw = Convert.ToInt32(Console.ReadLine());
        
        //Calcular Precio de Kw
        if (kw < 501)
        {
            valor_kw = 15;
        }
        if (kw > 500 && kw <1001)
        {
            valor_kw = 25;
        }
        if (kw > 1000 && kw <1501)
        {
            valor_kw = 30;
        }
        if (kw > 1500)
        {
            valor_kw = 35;
        }
        
        //Calcular Valor Cosumo
        valorConsumo= valor_kw * kw;
        
        //Calcular Total a Pagar
        if (kw < 1000)
        {
            valorDescuento = (valorConsumo * porcentajeDescuento ) / 100;
            subTotal=valorConsumo;
            totalPagar = valorConsumo - valorDescuento;
        }
        
        if (kw > 1000)
        {
            subTotal=valorConsumo;
            totalPagar = valorConsumo;
        }
        
        //Salida de los datos según el requerimiento
        Console.WriteLine("\n*** RECIBO DE CONSUMO DEL SERVICIO DE ENERGÍA ***\n");

        Console.WriteLine("* Nombre................. : {0}", nombre);
        Console.WriteLine("* Dirección................... : {0}", direccion);
        Console.WriteLine("* Mes Facturado................... : {0}", mes);
        Console.WriteLine("* Total Kw/Mes................ : {0}", kw);
        Console.WriteLine("* Valor KW.................... : {0}", valor_kw);
        Console.WriteLine("* Subtotal.................... : ${0}", subTotal);
        Console.WriteLine("* Valor a descontar por ahorro : ${0}", valorDescuento);
        Console.WriteLine("* Valor total a pagar......... : ${0}", totalPagar);
        Console.WriteLine("\n******************************************************\n");
    }
}