# Memoization을 사용하고 현재 계단보다 -2, -3인 결과값을 사용한다.
def climb(n, m):
    if n <= 3:
        if n == 2 or n == 3 and m[n] == 0:
            m[n] = 1
        return m[n]
    
    if m[n] == 0:
        m[n] = climb(n - 2, m) + climb(n - 3, m)
    return m[n]

n = int(input())
memo = [0 for _ in range(n + 1)]
print(climb(n, memo) % 10007)