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

# Cálculo de la matriz de cofactores
print(A.cofactor_matrix())
print(A._eval_determinant())
