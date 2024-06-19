N = int(input())
init_str = input()
tgt_str = input()

# 그리디 알고리즘을 사용해서 두 문자열이 연속으로 다른 구간의 개수를 센다.
# i 인덱스에서 두 문자열의 문자가 다를 때
    # 현재 구간의 다른 문자의 개수 1 증가
# i 인덱스에서 두 문자열의 문자가 같을 때
    # 이전 구간에서 서로 다른 문자의 개수가 1 이상일 때 ans 1증가, 이전 구간에서 다른 문자의 개수 0으로 초기화
    # 이전 구간에서 서로 다른 문자의 개수가 0일 때 continue
ans, diff = 0, 0
for i in range(N):
    if init_str[i] != tgt_str[i]:
        diff += 1
    else:
        if diff >= 1:
            ans += 1
            diff = 0
        else:
            continue

# for 반복문이 끝났을 때 diff가 1이상인 경우 ans에 반영이 안 되어서 ans에 1추가 해야한다.
if diff >= 1:
    ans += 1
print(ans)