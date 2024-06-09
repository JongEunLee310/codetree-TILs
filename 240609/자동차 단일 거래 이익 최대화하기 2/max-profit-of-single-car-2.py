n = int(input())
prices = [int(x) for x in input().split()]

# 그리디 알고리즘을 사용해서 숫자가 오름차순 순서일 때 해당 구간의 가장 작은 값과 가장 큰 값의 차이 중 가장 큰 차이를 답으로 구한다.
# ans는 최대 차익을 의미하며 차익이 0보다 작을 수는 없으므로 0으로 초기화하고 cur_min은 현재 구간의 최소값을 의미
ans, cur_min = 0, prices[0]
for i in range(n):
    # 입력된 순서대로 검사를 진행하다 구간의 최소값보다 현재 검사 중인 값이 발생하면 현재 검사 중인 값을 구간의 최소값으로 교체
    if prices[i] < cur_min:
        cur_min = prices[i]
    
    # 최대 차익은 ans과 현재 검사 중인 값 - 구간 최소값 중 최대값을 선택
    ans = max(ans, prices[i] - cur_min)

print(ans)