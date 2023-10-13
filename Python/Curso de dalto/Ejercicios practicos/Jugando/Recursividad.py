def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    try:
        numero = input("Ingresa un número entero para calcular su factorial: ")
        numero = int(numero)  # Debes asignar el resultado a una variable.

        print(
            factorial(numero)
        )  # Debes imprimir o hacer algo con el resultado de la función.

    except ValueError:
        print("Tu número no es entero o es negativo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
