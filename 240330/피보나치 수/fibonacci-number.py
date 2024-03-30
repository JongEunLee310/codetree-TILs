def fibo(n, m):
    if n < 2: return m[n]

    if m[n] == 0:
        m[n] = fibo(n - 1, m) + fibo(n - 2, m)
    
    return m[n]

n = int(input())
memo = [0 for _ in range(n + 1)]
memo[1] = 1
print(fibo(n, memo))