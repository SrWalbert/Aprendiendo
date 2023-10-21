using System;
using System.Collections.Generic;

namespace CarSalesApp
{
    class Car
    {
        public string Brand { get; set; }
        public double BasePrice { get; set; }
        public double Tax { get; set; }
        public string Origin { get; set; }

        public Car(string brand, double basePrice, double tax, string origin)
        {
            Brand = brand;
            BasePrice = basePrice;
            Tax = tax;
            Origin = origin;
        }

        public double CalculatePrice()
        {
            double finalPrice = BasePrice * (1 + Tax);
            return finalPrice;
        }

        public void DisplayInfo()
        {
            Console.WriteLine("Car Information:");
            Console.WriteLine($"Brand: {Brand}");
            Console.WriteLine($"Base Price: {BasePrice}");
            Console.WriteLine($"Tax: {Tax}");
            Console.WriteLine($"Origin: {Origin}");
            Console.WriteLine($"Final Price: {CalculatePrice()}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Enter the car brand: ");
                string brand = Console.ReadLine();

                Console.WriteLine("Enter the base price: ");
                double basePrice = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("Enter the tax (in decimal form, e.g. 0.2 for 20% tax): ");
                double tax = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("Enter the car's origin (japan, italy, germany, usa): ");
                string origin = Console.ReadLine().ToLower();

                List<string> allowedOrigins = new List<string> { "japan", "italy", "germany", "usa" };

                if (!allowedOrigins.Contains(origin))
                {
                    throw new ArgumentException("Invalid origin entered.");
                }

                Car car = new Car(brand, basePrice, tax, origin);
                car.DisplayInfo();
            }
            catch (FormatException)
            {
                Console.WriteLine("Please enter a valid number.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (Exception)
            {
                Console.WriteLine("An error occurred. Please try again.");
            }
        }
    }
}


