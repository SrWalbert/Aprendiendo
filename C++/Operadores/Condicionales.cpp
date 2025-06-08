#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
  int a, b, c, d;
  bool respuesta;
  a = 5;
  b = 10;
  c = 15;
  d = 20;
  respuesta = (b > a && d > c);
  cout << respuesta << "\n";
  respuesta = (b > a && d == c);
  cout << respuesta << "\n";  
  respuesta = (b > a || d == c);
  cout << respuesta << "\n";
  respuesta = !(a < c);
  cout << respuesta << "\n";
  //

  int e, f;
  e = 5;
  f = 6;
  if (e<f)
  {
    cout << "e es mayor que f" << "\n";
  }else if (e==f)
  {
    cout << "e es igual que f" << "\n";
  } else
  {
    cout << "e es menor que f" << "\n";
  }
  // Ejercicio

  int edad = 0;
  cout << "Por favor introduzca su edad: ";
  cin >> edad;
  if (edad>= 18)
  {
    cout << "\n"
         << "¡Puede pasar!";
  }else
  {
    cout << "No puede pasar, ¡fuera!";
  }
  // Ejercicio ifs anidados
  int horas = 0;
  cout << "Introuduzca las horas que trabaja al día: ";
  cin >> horas;
  if (horas<=5)
  {
    cout << "usted gana 10 dólares";
  }else if (horas >5 && horas<=10)
  {
    cout << "usted gana 20 dólares";
  }else if (horas >10 && horas <16)
  {
    cout << "usted gana 30 dólares";
  } else
  {
    cout << "No es sano trabajar tanto al día!";
  }
  
  
  
  

  return 0;
}