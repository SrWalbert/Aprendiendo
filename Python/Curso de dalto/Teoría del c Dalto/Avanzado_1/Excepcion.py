# Vamos a forzar una excepcion al convertir un str en int


def sumar_dos_numeros():
    a = input("Primer número: ")
    b = input("Segundo númro: ")
    resultado = int(a) + int(b)
    return resultado


# print(sumar_dos_numeros())


def sumar_dos_sin_excepciones():
    while True:  # Para repetir si sale mal
        a = input("Primer número: ")
        b = input("Segundo número: ")
        try:  # Íntentalo
            resultado = int(a) + int(b)
        except:  # Si lanza excepción entonces
            print("Te pedí números animal, no te hagas el gracioso")
            # Imprime y reinicia el bucle
        else:  # Si no lanza excepción entonces.
            break  # Termina el bucle
        finally:  # No importa lo que pase, eso siempre se ejecutará
            print("Esto se ejecuta siempre")
    return resultado


def sumar_dos_sin_excepciones_con_tipo_de_exc():
    while True:  # Para repetir si sale mal
        a = input("Primer número: ")
        b = input("Segundo número: ")
        try:  # Íntentalo
            resultado = int(a) + int(b)
        except Exception as e:
            # Si lanza excepción entonces ejecuta y dime qué salió mal
            #
            # Imprime:
            print("Te pedí números animal, no te hagas el gracioso")
            print(f"ERROR: {e}")
            # ...y reinicia el bucle
        else:  # Si no lanza excepción entonces.
            break  # Termina el bucle
        finally:  # No importa lo que pase, eso siempre se ejecutará
            print("Esto se ejecuta siempre")
    return resultado


# Podemos conocer el nombre de la excepción con type(e).__name__
# Así podemos configurar codigos de respuesta con   except ExceptName as e para tipos de error específicos
