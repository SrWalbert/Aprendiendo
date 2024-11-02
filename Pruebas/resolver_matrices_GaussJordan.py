import numpy as np
import sys

# Definimos la matriz aumentada del sistema
augmented_matrix = np.array(
    [
        [2, 3, 2, 1400],
        [1, 4, 1, 1100],
        [1, 2, 3, 1300],
    ],
    dtype=float,
)


# Aplicamos el método de Gauss-Jordan para reducir la matriz aumentada a forma escalonada reducida
def gauss_jordan_elimination(matrix):
    rows, cols = matrix.shape

    for i in range(rows):
        # Hacer que el pivote sea 1 dividiendo toda la fila por el elemento pivote
        pivot = matrix[i, i]
        matrix[i] = matrix[i] / pivot

        # Hacer ceros en la columna del pivote para las otras filas
        for j in range(rows):
            if j != i:
                factor = matrix[j, i]
                matrix[j] = matrix[j] - factor * matrix[i]

    return matrix


def main(*args: None) -> int:
    # Ejecutamos el método de Gauss-Jordan
    reduced_matrix = gauss_jordan_elimination(augmented_matrix.copy())
    print(reduced_matrix)
    # Extraemos las soluciones para X1, X2 y X3
    solutions = reduced_matrix[:, -1]
    print(solutions)

    return 0


if __name__ == "__main__":
    sys.exit(main())
