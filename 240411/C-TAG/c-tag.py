import copy

# m - 1까지의 인덱스 중 c개를 선택해 만들 수 있는 모든 조합을 반환
def get_comb(c, m, comb, cur, cur_num):
    if len(cur) == c:
        comb.append(copy.deepcopy(cur))
        return
    if cur_num == m:
        return
    
    # cur_num에 해당하는 숫자를 사용했을 때의 경우를 탐색
    cur.append(cur_num)
    get_comb(c, m, comb, cur, cur_num + 1)
    cur.pop()

    # cur_num에 해당하는 숫자를 사용하지 않았을 때의 경우를 탐색
    get_comb(c, m, comb, cur, cur_num + 1)

N, M = [int(x) for x in input().split()]
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

# 초합의 길이가 3인 조합 중 A, B 그룹을 구별할 수 있는 개수를 구한다.
cnt = 0
comb = []
get_comb(3, M, comb, [], 0)
for c in comb:
    # c에 선택된 인덱스를 사용해서 A, B에 있는 문자열의 조합을 저장
    a_s = set()
    b_s = set()
    for j in range(N):
        a = ''
        b = ''
        for idx in c:
            a += A[j][idx]
            b += B[j][idx]
        a_s.add(a)
        b_s.add(b)

    # a_s와 b_s에 선택된 조합 중 같은 것이 없으면 cnt를 1추가
    result = True
    for a in a_s:
        if a in b_s:
            result = False
            break
    if result: cnt += 1

print(cnt)