def fibonacci_O_n(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = 100000  # Example input
print(f"Fibonacci (O(n)): {fibonacci_O_n(n)}")
