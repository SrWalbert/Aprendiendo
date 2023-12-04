"""
Hacer un programa que pida al usuario tres número y encuentre el mayor
"""
type int_or_float = int | float
# Entrada de numeros
num_1: int_or_float = input("Introduce un número para comparar: ")
num_2: int_or_float = input("Introduce un número para comparar: ")
num_3: int_or_float = input("Introduce un número para comparar: ")


# Comparador
def comparator(*nums: int_or_float) -> tuple[int_or_float]:
    """Encuentra los maximos y minimos de unos valores dados.

    Returns:
        tuple[int_or_float]: Dos numeros, uno mayor y otro menor
    """

    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


# programa corriendo
print(comparator(num_1, num_2, num_3))

"""------------------------------------------------------------"""
"""Convertidor a celcious"""
grados_farengeit_dados = input("Introduce los grados farhengeit: ")
grados_farengeit_dados: float = float(grados_farengeit_dados)


def conversor_far_a_celc(farengheit: float) -> float:
    """Convierte farenheit a celcius

    Args:
        farengheit (float): Los grados que se introducen

    Returns:
        float: El equivalente en celcious
    """
    return (farengheit - 32) * 5 / 9


print(conversor_far_a_celc(grados_farengeit_dados))
