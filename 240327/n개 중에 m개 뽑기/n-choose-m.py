# 길이가 M인 모든 조합을 재귀적으로 만들어 출력하는 함수
def print_pair(N, M, l):
    if len(l) == M:
        for n in l:
            print(n, end=' ')
        print()
        return
    
    for i in range(1, N + 1):
        if i not in l and (len(l) < 1 or len(l) >= 1 and l[-1] < i):
            l.append(i)
            print_pair(N, M, l)
            l.pop()

N, M = [int(x) for x in input().split()]
print_pair(N, M, [])