import sys
import sympy as sp

# Definición de la matriz original
A = sp.Matrix(
    # fmt: off
    [
        
        [1, 0, 0, 0, 0],
        [-2, 2, 4, -3, -1], 
        [-2, -1, 1, 2, 2],
        [1, 3, 2, -1, 4],
        [0, -2, 0, 0, -3]
    ]
    # fmt:on
)
B = sp.Matrix(#fmt:on
              [[1, 0, 6], [2, -3, 5], [2, 3, 1]])  # fmt: off


def main(*args: None) -> int:
    # Cálculo de la matriz de cofactores
    
    # print(B._eval_determinant())
    print(A**-1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
