class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def multiply(m1, m2):
    return Matrix(
        m1.a * m2.a + m1.b * m2.c,
        m1.a * m2.b + m1.b * m2.d,
        m1.c * m2.a + m1.d * m2.c,
        m1.c * m2.b + m1.d * m2.d
    )

def power(m, n):
    if n == 1:
        return m
    half = power(m, n // 2)
    if n % 2 == 0:
        return multiply(half, half)
    return multiply(m, multiply(half, half))

def fibonacci_O_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    m = Matrix(1, 1, 1, 0)
    result = power(m, n - 1)
    return result.a  # F(n) is at position a

# Example usage
n = 100000  # Example input
print(f"Fibonacci (O(1)): {fibonacci_O_1(n)}")
