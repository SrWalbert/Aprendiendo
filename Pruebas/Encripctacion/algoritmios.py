"""Encriptar en codigo cesar y viguenere"""

"""Ayuda en textos"""
import re


"""-----------Codigo-----------"""
# Diccionario de palabras:
# Creación de un diccionario con las letras del alfabeto latino como claves y los números del 1 al 27 como valores.
alfabeto = "abcdefghijklmnopqrstuvwxyz"
diccionario: dict[str, int] = {letra: indice for letra, indice in enumerate(alfabeto)}


def en_cesar(key: str, input_: str, checked: bool = False) -> str:
    """Encripta en clave cesar en input que se le manda

    Args:
        key (str): Un caracter que señala cuanto se desplazarán las letras para cifrarse
        input_ (str): El texto que será cifrado
        checked (bool): Si viene del cifrado vigenere, no hará las comprobaciones, pues estas ya se hicieron previamente

    Returns:
        str: El texto ya cifrado
    """

    if not checked:
        key = key.lower()
        input_ = input_.lower()
        if (len(key) == 1) and (key in alfabeto):
            desplazamiento: int = alfabeto.index(key) + 1
        else:
            return (
                "Llave inválida, intente con una llave de un solo caracter alfabético"
            )
    else:
        desplazamiento: int = alfabeto.index(key) + 1

    texto_cifrado: str = ""

    for letra in input_:
        if letra in alfabeto:
            posicion_nueva: int = (alfabeto.index(letra) + desplazamiento) % 26
            letra_nueva: int = alfabeto[posicion_nueva]
            texto_cifrado += letra_nueva
        else:
            texto_cifrado += letra
    return texto_cifrado


def desen_cesar(key: str, cifrado: str, checked: bool = False) -> str:
    """Desencripta en clave cesar en input que se le manda

    Args:
        key (str): Un caracter que señala cuanto se desplazarán las letras para descifrarse
        input_ (str): El texto que será descifrado

    Returns:
        str: El texto ya descifrado
    """
    if not checked:
        key = key.lower()
        cifrado = cifrado.lower()
        if (len(key) == 1) and (key in alfabeto):
            desplazamiento: int = -alfabeto.index(key) - 1
        else:
            return (
                "Llave inválida, intente con una llave de un solo caracter alfabético"
            )
    else:
        desplazamiento: int = -alfabeto.index(key) - 1

    texto_descifrado: str = ""

    for letra in cifrado:
        if letra in alfabeto:
            posicion_nueva: int = (alfabeto.index(letra) + desplazamiento) % 26
            letra_nueva: int = alfabeto[posicion_nueva]
            texto_descifrado += letra_nueva
        else:
            texto_descifrado += letra
    return texto_descifrado


def en_viguenere(clave: str, input_: str) -> str:
    clave = clave.lower()
    input_ = input_.lower()
    for letra in clave:
        if letra not in alfabeto:
            return (
                "Llave inválida, intente con una llave de solo caracteres alfabéticos"
            )
    texto_cifrado: str = ""
    clave_extendida: str = (clave * (len(input_) // len(clave))) + clave[
        : len(input_) % len(clave)
    ]

    for char_clave, char_input in zip(clave_extendida, input_):
        nuevo_char = en_cesar(char_clave, char_input, checked=True)
        texto_cifrado += nuevo_char
    return texto_cifrado
