def fibo(n, m):
    if n <= 2:
        if m[n] == 0:
            m[n] = 1
        return m[n]
 
    return m[n] if m[n] != 0 else fibo(n - 1, m) + fibo(n - 2, m)

n = int(input())
memo = [0 for i in range(n + 1)]
print(fibo(n, memo))