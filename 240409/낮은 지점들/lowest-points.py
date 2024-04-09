n = int(input())

# x를 키로 가지고 x에 대응하는 y의 최소값을 값으로 가지는 딕셔너리를 사용하여 y의 합을 구한다.
d = {}
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    try:
        d[x] = min(d[x], y)
    except:
        d[x] = y

# 딕셔너리의 value를 리스트로 변환 후 리스트의 모든 요소의 합을 춮력.
d_list = list(d.values())
ans = sum(d_list)
print(ans)