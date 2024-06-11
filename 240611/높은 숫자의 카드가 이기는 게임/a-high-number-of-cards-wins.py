N = int(input())
B = [int(input()) for _ in range(N)]
B.sort()

# A의 카드덱 생성
# B를 내림차순으로 정렬한 수 2N만큼 반복문을 수행해 현재 검사 중인 숫자 i가 B에 없으면 A에 i를 추가
A = []
b_i = 0
for i in range(1, 2 * N + 1):
    if b_i < N and B[b_i] == i:
        b_i += 1
        continue

    A.append(i)

# 그리디 알고리즘을 사용해서 B의 카드보다 큰 수 중 가장 작은 숫자를 낸다.
# 이를 위해 B의 카드를 오름차순으로 정렬한 후 반복문을 사용해 A의 카드와 비교
    # A의 a_i 인덱스의 수가 B의 b_i 인덱스의 수보다 클 때
        # ans 1증가
        # a_i와 b_i 1증가
    # A의 a_i 인덱스의 수가 B의 b_i 인덱스의 수보다 작을 때
        # a_i만 증가
a_i, b_i = 0, 0
ans = 0
while a_i < N and b_i < N:
    if A[a_i] > B[b_i]:
        b_i += 1
        ans += 1
    a_i += 1

print(ans)