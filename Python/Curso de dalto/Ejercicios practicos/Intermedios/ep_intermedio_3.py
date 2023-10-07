# Calculando serie de fibonacci
def calculo_fibonacci(num):
    a, b = 0, 1
    lista_fibonacci = list([0])
    for i in range(num + 1):
        if b > num:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a + b


resultado = calculo_fibonacci(100)
print(resultado)
