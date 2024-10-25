def fibonacci_O_2n(n):
    if n <= 1:
        return n
    return fibonacci_O_2n(n - 1) + fibonacci_O_2n(n - 2)

# Example usage
n = 10000  # Example input
print(f"Fibonacci (O(2^n)): {fibonacci_O_2n(n)}")
