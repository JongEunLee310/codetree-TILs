n = int(input())
meetings = [[int(x) for x in input().split()] for _ in range(n)]

# 그리디 알고리즘을 적용하여 회의가 끝나는 시점을 기준으로 더 빨리 끝나는 회의부터 차례로 선택
meetings.sort(key = lambda x : x[1])

# ans는 회의 갯수이며 처음 1번은 무조건 회의를 진행하므로 1로 초기화
# cur는 마지막으로 진행한 회의를 의미하며 meetings[0]으로 초기화
ans, cur = 1, meetings[0]
for i in range(n):
    s, _ = meetings[i]

    # 다음 회의로 선택할 회의의 시작 시간이 마지막으로 선택된 회의의 종료시간보다 빠르면 다음 순서로 넘김
    if s < cur[1]:
        continue
    
    # 선택한 회의를 cur로 바꾸로 ans를 1증가
    cur = meetings[i]
    ans += 1

print(ans)