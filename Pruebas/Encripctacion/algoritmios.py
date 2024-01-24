"""Encriptar en codigo cesar y viguenere"""

"""Ayuda en textos"""
import re


"""-----------Codigo-----------"""
# Alfabeto para usar
ALFABERTO = "abcdefghijklmnopqrstuvwxyz"


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
        if (len(key) == 1) and (key in ALFABERTO):
            desplazamiento: int = ALFABERTO.index(key) + 1
        else:
            return (
                "Llave inválida, intente con una llave de un solo caracter alfabético"
            )
    else:
        desplazamiento: int = ALFABERTO.index(key) + 1

    texto_cifrado: str = ""

    for letra in input_:
        if letra in ALFABERTO:
            posicion_nueva: int = (ALFABERTO.index(letra) + desplazamiento) % 26
            letra_nueva: int = ALFABERTO[posicion_nueva]
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
        if (len(key) == 1) and (key in ALFABERTO):
            desplazamiento: int = -ALFABERTO.index(key) - 1
        else:
            return (
                "Llave inválida, intente con una llave de un solo caracter alfabético"
            )
    else:
        desplazamiento: int = -ALFABERTO.index(key) - 1

    texto_descifrado: str = ""

    for letra in cifrado:
        if letra in ALFABERTO:
            posicion_nueva: int = (ALFABERTO.index(letra) + desplazamiento) % 26
            letra_nueva: int = ALFABERTO[posicion_nueva]
            texto_descifrado += letra_nueva
        else:
            texto_descifrado += letra
    return texto_descifrado


def en_vigenere(clave: str, input_: str) -> str:
    """Encripta textos en cifrado vigenere

    Args:
        clave (str): Secuencia de letras sin espacios con la que encriptan los textos en cesar
        input_ (str): Texto a encriptar

    Returns:
        str: Texto encriptado
    """

    clave = clave.lower()
    input_ = input_.lower()
    for letra in clave:
        if letra not in ALFABERTO:
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


def desen_vigenere(clave: str, cifrado: str) -> str:
    clave = clave.lower()
    cifrado = cifrado.lower()
    for letra in clave:
        if letra not in ALFABERTO:
            return (
                "Llave inválida, intente con una llave de solo caracteres alfabéticos"
            )

    texto_descifrado: str = ""
    clave_extendida: str = (clave * (len(cifrado) // len(clave))) + clave[
        : len(cifrado) % len(clave)
    ]

    for char_clave, char_cifrado in zip(clave_extendida, cifrado):
        nuevo_char: str = desen_cesar(char_clave, char_cifrado, checked=True)
        texto_descifrado += nuevo_char
    return texto_descifrado
