import numpy as np
import sys

np.set_printoptions(suppress=True)


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


# La comprobación está pendiente de ser arreglada
def comprobation(original_matrix, solution_vector) -> bool:
    original_rows, original_cols = original_matrix.shape
    original_solutions = original_matrix[:, -1]
    for i in range(original_rows):
        for j in range(original_cols - 1):
            for k in solution_vector:
                if j * k in [solution for solution in original_solutions]:
                    continue
                else:
                    return False
    return True


def main(*args: None) -> int:
    # Definimos la matriz aumentada del sistema
    augmented_matrix = np.array(
        # fmt: off
        [
            [2, 3, 2, 1400],
            [1, 4, 1, 1100],
            [1, 2, 3, 1300],

        ],
        # fmt: on
        dtype=float,
    )
    # Ejecutamos el método de Gauss-Jordan
    resolved_matrix = gauss_jordan_elimination(augmented_matrix.copy())
    print(resolved_matrix)
    # Extraemos las soluciones para X1, X2 y X3
    solutions = resolved_matrix[:, -1]
    print("Soluciones: ", solutions)

    print("¿Está correcto?", comprobation(augmented_matrix, solutions))
    return 0


if __name__ == "__main__":
    sys.exit(main())
