n = int(input())
meetings = [[int(x) for x in input().split()] for _ in range(n)]

# 그리디 알고리즘을 적용하여 회의가 끝나는 시점을 기준으로 더 빨리 끝나는 회의부터 차례로 선택
# 최대한 많은 회의를 선택한 후 전체 회의 수를 뺀 것을 출력
meetings.sort(key = lambda x : x[1])

# cnt_meetings는 최대 참석 회의 수
# cur는 마지막으로 진행한 회의를 의미하며 meetings[0]으로 초기화
cnt_meetings, cur = 1, meetings[0]
for i in range(n):
    s, _ = meetings[i]

    # 다음 회의로 선택할 회의의 시작 시간이 마지막으로 선택된 회의의 종료시간보다 빠르면 다음 순서로 넘김
    if s < cur[1]:
        continue
    
    # 선택한 회의를 cur로 바꾸로 ans를 1증가
    cur = meetings[i]
    cnt_meetings += 1

print(n - cnt_meetings)