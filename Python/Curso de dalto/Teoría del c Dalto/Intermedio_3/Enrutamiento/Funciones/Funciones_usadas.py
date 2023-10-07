# Funciones para primos
def es_primo(num):
    # Verificamos que ese numero no se puede dividir en entero entre de ni ese
    # mismo numero menos uno (solo se divide por sí mismo y uno)
    for i in range(2, num - 1):
        if num % i == 0:  # Si es divisible retorna falso
            return False
    return True  # Si no es divisible por nada retorna verdadero


# Lista de primos hasta un número
def primos_hasta(num):
    primos = list()  # Crea lista
    for i in range(3, num + 1):  # Para un numero i en el rango de 3 al limite
        # ...(más uno para que ese limite sea abierto [>=])
        resultado = es_primo(i)
        if resultado == True:  # Lo pasas a la función, si da verdadero lo añade
            # ...a la lista
            primos.append(i)
    return primos
