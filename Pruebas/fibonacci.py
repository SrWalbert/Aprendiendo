"""Hacer un programa que de los numeros de la secuencia de fibonacci"""
import sys
from time import perf_counter


def fibonnacci(maximus: int) -> list:
    a, b = 0, 1
    lista_fibonacci = list([0])
    for i in range(maximus):
        if b > maximus:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a + b


optimized_fib = (
    lambda n, a=0, b=1, res=[]: res if b > n else optimized_fib(n, b, a + b, res + [b])
)


def main(*args: None) -> None:
    print(fibonnacci(50))
    print(optimized_fib(100))


if __name__ == "__main__":
    sys.exit(main())
