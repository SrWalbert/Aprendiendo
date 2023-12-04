"""
Crea una función custom que funcione igual que max
"""


def custom_max(*args: int | float) -> int | float:
    """Tomando una conjunto de números, encuentra el mas grande

    Raises:
        ValueError: si no se dan argumentos

    Returns:
        int | float: número más grande
    """
    if not args:
        raise ValueError("No se proveyeron números para la comparación")

    max_number: int | float = args[0]
    for arg in args:
        if arg > max_number:
            max_number = arg
    return max_number


print(custom_max(1, 2, 6, 8, 12, 9, 15, 26, 148, 98, 100, 0.3))
