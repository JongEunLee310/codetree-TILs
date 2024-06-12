N = int(input())

# 시간대별로 폭탄을 분류하기 위해 폭탄 정보를 Dict에 저장한다.
bombs = {}
for i in range(N):
    s, t = [int(x) for x in input().split()]
    try:
        bombs[t].append(s)
    except:
        bombs[t] = [s]

# 그리디 알고리즘을 사용해 얻을 수 있는 점수의 최대값을 구한다.
# 입력된 폭탄 정보의 각 시간대에 존재하는 점수를 내림차순 정렬하여 각 시간대에 얻을 수 있는 최대 값의 합을 구한다.

# 시간 제한의 범위가 1 <= t <= 10000이고 폭탄 정보가 dict이므로 1부터 10000까지 순회하며 존재하는 시간대에서 점수를 내림차순으로 정렬 
for i in range(1, 10001):
    try:
        bombs[i].sort(reverse=True)
    except:
        continue

# ans에 최대 점수를 더한다.
# 시간 제한 내에 폭탄을 해제하면 되므로 마지막으로 폭탄을 해체한 시점부터 다음 제한 시간 내에 해제 가능한 폭탄을 ans에 모두 더한다.
ans = 0
last_t = 0  # 마지막으로 폭탄을 해체한 시점
for i in range(1, 10001):
    try:
        for j in range(i - last_t):
            ans += bombs[i][j]
            last_t += 1  # 폭탄을 해체했으므로 마지막 폭탄 시점 갱신 -> 폭탄 1개당 1시간이므로 1추가

    # i 시간대에 점수가 없을 경우 예외 처리
    # i 시간대에 점수의 개수가 i - last_t보다 적어 j가 i 시간대 리스트의 인덱스 범위를 넘어설때 예외처리
    except:
        continue

print(ans)