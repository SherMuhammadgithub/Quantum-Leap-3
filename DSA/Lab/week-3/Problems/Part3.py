def MatAdd(A, B):
    # Get the dimensions of the matrices
    rows, cols = len(A), len(A[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform element-wise addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]

    return result


def MatAddPartial(A, B, start, size):
    # Unpack the start position
    x, y = start

    # Intialize the result matrix with zeros
    result = [[0 for _ in range(size) for _ in range(size)]]

    # Add the submatrices from A and B
    for i in range(size):
        for j in range(size):
            result[i][j] = A[x + i][y + j] + B[x + i][y + j]

    return result


def MatMul(A, B):
    # Get the dimensions
    rows_A, cols_A = len(A),len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result 