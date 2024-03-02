primos_hasta_en_una_linea = lambda num: list(
    filter(
        lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, num)
    )
)
print(primos_hasta_en_una_linea(21))

primos_hasta_en_una_linea_legible = lambda num: [
    # x for x in range(2, num) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    x
    for x in range(2, num)
    if False not in [x % i != 0 for i in range(2, int(x**0.5) + 1)]
]


print(list(primos_hasta_en_una_linea_legible(21)))
