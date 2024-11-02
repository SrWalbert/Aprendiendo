"""Aquí estarán la informacion extra que no se vio en el curso de Dalto"""
# Para crear constantes se usa la convención del nombre en mayusculas
PI: float = 3.124159

# Hay numeros complejos en python
complx_numb: complex = 8j

# Para numeros grandes se puede hacerlos más legibles con _
numero_gigante = 1_000_000_000

# El operador += , -= junto con los demás,son útiles
a = 5
a += 3
a -= 3
a *= 3
a /= 3
# Y demás operadores

# Con punto y coma se pueden seleccionar elementos con indices desde un punto a otro, se incluye el primer numero, pero no el segundo.
# print(lista[a:b])


#
# Además del desempaquetado de tuplas que ya conocemos, se puede añadir un asterisco para que a la segunda variable se le aplique lo demás

tupla_asignable: tuple = "mi amigo", True, 5
a, *b = tupla_asignable

set1 = {"a,", True}
print(dir(set1))

# añadir los metodos que faltan a intermedio 1 de dalto


# ---------------------------

# if en una sola linea
# Haz_esto if True else Haz_esto_otro
# resultado = a if True else b

#Comment test