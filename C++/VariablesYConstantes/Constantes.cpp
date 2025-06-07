#include <iostream>
//Declarando constantes fuera del main
#define Pi 3.1416

using namespace std;

int main(int argc, char const *argv[])
{
  float altura = 1.70;
  const float GRAVEDAD = 9.8;
  altura = 1.75;
  cout << altura << "\n";
  cout << GRAVEDAD << "\n";

  return 0;
}
