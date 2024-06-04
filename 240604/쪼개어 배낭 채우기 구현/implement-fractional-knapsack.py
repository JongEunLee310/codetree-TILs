N, M = [int(x) for x in input().split()]
gems = [[int(x) for x in input().split()] for _ in range(N)]

# 입력 받은 보석 정보를 무게당 가치를 기준으로 내림차준 정렬하여 가치가 큰 것부터 선택하도록 한다.
gems.sort(key = lambda x : (x[1] / x[0]), reverse=True)

ans, i = 0, 0
# M이 0이 될 때까지 보석의 가치의 합을 구한다.
while M > 0 and i < N:
    w, v = gems[i]
    # 남은 가방 용량이 현재 검사 중인 보석의 무게 이상일 때
        # 남은 용량에서 보석의 무게를 뺀다
        # 보석의 가치를 그대로 정답에 더한다.
    if M >= w:
        M -= w
        ans += v
    # 남은 가방 용량이 현재 검사 중인 보석의 무게보다 적을 때
        # 보석의 단위 가치에 남은 용량을 곱한 값을 정답에 더한다.
        # 남은 가방의 용량은 0이 된다.
    else:
        ans += (v / w) * M
        M = 0

    i += 1

print('{0:.3f}'.format(ans))