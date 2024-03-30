# 이전에 쌓은 블록의 결과 값에 새로운 블럭을 추가하는 방식으로 문제를 해결하는 함수
def fill(n, m):
    if n <= 2:
        if n == 1 or n == 2: m[n] = n
        return m[n]
    
    if m[n] == 0:
        m[n] = fill(n - 1, m) + fill(n - 2, m) 
    return m[n]

n = int(input())
memo = [0 for _ in range(n + 1)]
print(fill(n, memo) % 10007)