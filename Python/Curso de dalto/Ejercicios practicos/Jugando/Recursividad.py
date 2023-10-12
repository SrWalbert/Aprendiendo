def factorial(n: int) -> int:
    if n == 0:
        return 1  # Caso base: 0! = 1
    else:
        return n * factorial(n - 1)  # Caso recursivo: n! = n * (n - 1)!


while True:
    numero = input("Ingresa un numero entero para cualcular su factorial: ")
    try:
        int(numero)
        if type(numero) is int:
            print(factorial(numero))
    except:
        print("Tu numero no es entero")
