/*Calculadora de masa corporal*/
#include <iostream>
#include <math.h>
#include <iomanip>


using namespace std;

int main(int argc, char const *argv[])
{
  //variables
  float peso = 0;
  float altura = 0;
  float imc = 0;

  cout << "Calculadora de índice de masa corporal imc" << "\n";
  cout << "ingrese su peso en kg: ";
  cin >> peso;
  cout << "ingrese su altura en metros: ";
  cin >> altura;

  imc = peso / pow(altura,2);
  cout << "Su indice de masa corporale es: " << setprecision(4) << imc << " kg/m^2";
  return 0;
}