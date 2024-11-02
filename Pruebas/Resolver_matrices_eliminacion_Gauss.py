import sys
import numpy as np


def gaussian_elimination(matriz, resultados):
    """
    Solves the system of linear equations Ax = b using Gaussian elimination.

    Parameters:
    A (ndarray): The coefficient matrix.
    b (ndarray): The constant terms vector.

    Returns:
    ndarray: Solution vector x if the system has a unique solution, otherwise None.
    """
    n = len(resultados)
    # Augmenting matrix A with vector b
    Ab = np.hstack([matriz, resultados.reshape(-1, 1)])

    # Forward elimination
    for i in range(n):
        # Find the maximum element in the current column
        max_row = np.argmax(abs(Ab[i:, i])) + i
        if Ab[max_row, i] == 0:
            return None  # Singular matrix, no unique solution exists

        # Swap the current row with the row of the maximum element
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # Make the diagonal element 1 and eliminate below
        Ab[i] = Ab[i] / Ab[i, i]
        for j in range(i + 1, n):
            Ab[j] -= Ab[i] * Ab[j, i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1 : n], x[i + 1 : n])

    return x


def main(*args: None) -> int:
    # Ejemplo de uso
    A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
    b = np.array([8.0, -11.0, -3.0])

    solution = gaussian_elimination(A, b)
    print("Solution:", solution)

    return 0


if __name__ == "__main__":
    sys.exit(main())
