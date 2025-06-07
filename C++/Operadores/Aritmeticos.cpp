#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[])
{
  int a = 20;
  float b = 10;
  cout << a + b << "\n";
  cout << a - b << "\n";
  cout << a * b << "\n";
  cout << a / b << "\n";
  int c = 5;
  int d = 2;
  cout << c % d << "\n";

  //
  a *= b;
  cout << a;
  

  return 0;
}