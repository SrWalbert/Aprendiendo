import sys
import sympy as sp

# Definición de la matriz original
A = sp.Matrix(
    # fmt: off
    [
        
        [1, -2, 1, 2],
        [3, -1, -5, 4], 
        [-4, 3, 2, 4],
        [2, 4, -2, 1]
    ]
    # fmt:on
)

B = sp.Matrix(
    # fmt: off
    [
        [3,7],
        [2,5]
    ]
    # fmt:on
)


def main(*args: None) -> int:
    # Cálculo de la matriz de cofactores
    print(A.cofactor_matrix())
    print(A._eval_determinant())
    print(A**-1)
    print("-------------------------")
    # B
    print(B**-1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
