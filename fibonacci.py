def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0 

    result = None
    for i in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

print(fibonacci(-5))

# for i in range(36):
#     print(i, fibonacci(i))

