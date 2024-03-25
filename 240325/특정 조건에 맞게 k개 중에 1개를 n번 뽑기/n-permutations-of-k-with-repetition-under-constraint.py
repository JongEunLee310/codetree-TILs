# 같은 수가 3번 이상 반복되지 않는 모든 경우의 수를 출력하는 함수
def get_pair(k, n, p):
    if len(p) == n:
        for num in p:
            print(num, end=' ')
        print()
        return
    
    for i in range(1, k):
        if len(p) < 2 or len(p) >= 2 and not (p[-1] == i and p[-2] == i):
            p.append(i)
            get_pair(k, n, p)
            p.pop()

K, N = [int(x) for x in input().split()]
get_pair(K + 1, N, [])