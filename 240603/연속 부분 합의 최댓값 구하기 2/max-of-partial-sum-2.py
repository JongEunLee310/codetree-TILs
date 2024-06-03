from sys import maxsize

n = int(input())
arr = [int(x) for x in input().split()]

# 그리디 알고리즘으로 풀이
# 현재까지 부분합이 음수가 될 때 다음 숫자와 합은 무조건 합이 줄어들기 때문에 현재 합을 다음 숫자와 같은 값으로 초기화
ans, cur = -maxsize, 0
i = 0
while i < n:
    # 현재 숫자까지 합을 구한다.
    cur += arr[i]

    # 정답이 부분합보다 작으면 값을 부분합으로 갱신한다.
    if ans < cur:
        ans = cur
    i += 1

    # 부분 합이 항상 음수인 경우가 있어서 현재 부분합이 음수일 때 0으로 초기화하는 순서를 반복문 가장 앞에서 뒤로 바꿈
    # 정답을 갱신하는 순서보다 앞에 있으면 구할 수 있는 모든 연속 부분합이 음수일 때 최대 연속부분합이 0이 되는 오류가 발생하기 때문
    if cur < 0: cur = 0

print(ans)