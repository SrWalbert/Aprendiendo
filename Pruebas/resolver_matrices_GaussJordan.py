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


def comprobation(original_aumented_matrix, solution_vector) -> bool:
    coeficientes_de_la_matriz = original_aumented_matrix[:, :-1]
    resultados_originales_de_la_matriz = original_aumented_matrix[:, -1]
    calculated_solutions = np.dot(coeficientes_de_la_matriz, solution_vector)

    return np.allclose(calculated_solutions, resultados_originales_de_la_matriz)


def main(*args: None) -> int:
    # Definimos la matriz aumentada del sistema
    augmented_matrix = np.array(
        # fmt: off
        [
           [2,1,-3, 4],
           [1,1,2, 3],
           [-1,-2,0, -5]
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
