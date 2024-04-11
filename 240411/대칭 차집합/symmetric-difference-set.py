na, nb = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# a의 원소 개수와 b의 원소 개수의 합에 ab의 합집합의 원소 개수를 빼면 ab의 교집합의 원소 개수를 구할 수 있음
    # ab의 합집합의 원소수에 ab의 교집합를 빼면 대칭 차집합의 원소수 개수를 구할 수 있다.
ab = set()
for i in range(na):
    ab.add(a[i])
for i in range(nb):
    ab.add(b[i])

# 괄호 안은 교집합의 원소의 개수
ans = len(ab) - (na + nb - len(ab))
print(ans)