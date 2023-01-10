

def fibonacci(n):
    """Return the nth fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))


####
def fibonacci(n):
    """Return the nth fibonacci number in O(n) time."""
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    # Iterate through the sequence
    for i in range(n):
        # Calculate the next number in the sequence
        a, b = b, a + b
    # Return the nth number
    return a
####


def fibonacci(n):
    """Return the nth fibonacci number in O(log(n)) time."""
    # Initialize the base case
    if n == 0:
        return 0
    # Initialize the matrix representation of the Fibonacci sequence
    F = [[1, 1], [1, 0]]
    # Calculate the nth power of the matrix
    F = matrix_power(F, n - 1)
    # Return the top left element of the matrix
    return F[0][0]


def matrix_power(A, n):
    """Return the nth power of matrix A."""
    if n == 1:
        return A
    if n % 2 == 0:
        B = matrix_power(A, n // 2)
        return matrix_multiply(B, B)
    else:
        B = matrix_power(A, n // 2)
        return matrix_multiply(A, matrix_multiply(B, B))


def matrix_multiply(A, B):
    """Return the product of matrices A and B."""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C


print(fibonacci(40))
print(fibonacci(5000))
