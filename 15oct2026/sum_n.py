def fibo(n):
    if n <= 0:
        return0

    return n + fibo (n-1)

print(fibo(4))