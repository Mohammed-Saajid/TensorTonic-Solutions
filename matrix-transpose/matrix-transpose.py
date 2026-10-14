import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows = len(A)
    columns = len(A[0])

    result = np.zeros(shape=(columns,rows), dtype=int)
    for i in range(len(A)):
        for j in range(len(A[0])):
             result[j][i] = A[i][j]
    return result
