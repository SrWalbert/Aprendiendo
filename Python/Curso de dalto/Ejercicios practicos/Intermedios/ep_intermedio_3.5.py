# numeros_de_fibonacci_en_una_linea = lambda num: list(filter(lambda a, b: (a, b = 0, 1) (a,b = a, a+b while b < num )))

# numeros_de_fibonacci_en_una_linea = lambda num, a=0, b=1: list(
#     map(lambda f=[]: f.append(a + b), range(num))
# )


calcular_fibonacci = (
    lambda num, a=0, b=1: [a] + calcular_fibonacci(num - 1, b, a + b) if num > 0 else []
)


print(calcular_fibonacci(20))


fibonacci = (
    lambda n, a=0, b=1, res=[]: res if b > n else fibonacci(n, b, a + b, res + [b])
)

print(fibonacci(100))
