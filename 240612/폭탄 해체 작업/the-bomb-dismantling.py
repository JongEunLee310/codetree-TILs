N = int(input())
bombs = [[int(x) for x in input().split()] for _ in range(N)]

# 그리디 알고리즘을 사용해 얻을 수 있는 점수의 최대값을 구한다.
# 입력된 폭탄 정보의 점수를 첫번째 기준으로 내림차순 정렬하여 최대 값부터 더해가면 최대 점수를 구한다.
    # 시간은 마커를 사용해 폭탄의 제한 시간내에 해체한 폭탄이 없으면 더하지 않는다.

bombs.sort(key = lambda x : -x[0])
marker = [True if i == 0 else False for i in range(10001)]

# ans에 내림차순으로 정렬된 bombs의 점수를 더한다.
# marker에 제한시간 내 해체한 폭탄을 추가할 수 없을 때는 더하지 않는다.
    # marker의 j 인덱스가 True면 해당 시간대에 해체한 폭탄이 있다는 것을 의미
    # marker의 j 인덱스가 False면 해당 시간대에 해체한 폭탄이 없어 해체한 폭탄이 없다는 것을 의미
ans = 0
for i in range(N):
    s, t = bombs[i]
    for j in range(t, 0, -1):
        if not marker[j]:
            ans += s
            marker[j] = True
            break

print(ans)