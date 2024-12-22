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
B = sp.Matrix(  # fmt:off
    [[2, 4, -3, -1], [-1, 1, 2, 2], [3, 2, -1, 4], [-2, 0, 0, -3]]
    # fmt: on
)


def main(*args: None) -> int:
    # Cálculo de la matriz de cofactores

    print(A**-1)
    print("----------------")
    print(A.cofactorMatrix())
    # print(A**-1)
    print("----------------")
    print(sp.transpose(A.cofactor_matrix()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
