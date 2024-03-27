# 재궈직으로 순열을 출력하는 함수
def print_permul(n, per, visited):
    if len(per) == n:
        for num in per:
            print(num, end=' ')
        print()
        return
    
    # 각 자리에 i를 포함하는 순열을 생성
    for i in range(1, n + 1):
        if not visited[i]:
            per.append(i)
            visited[i] = True
            print_permul(n, per, visited)
            per.pop()
            visited[i] = False

n = int(input())
visited = [False for _ in range(n + 1)]
print_permul(n, [], visited)