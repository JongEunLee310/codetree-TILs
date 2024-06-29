N = int(input())
init_str = input()
tgt_str = input()

# 그리디 알고리즘 적용
    # 특정 인덱스에서 두 문자열의 문자가 같을 때
        # 구간의 길이가 0보다 클 때 구간의 수를 1 증가 및 구간의 길이를 0으로 초기화
    # 특정 인덱스에서 두 문자열의 문자가 다를 때
        # 구간의 길이를 1 증가. 단, 4보다 길어지면 구간 수를 1 증가 및 구간의 길이를 1로 초기화
    
ans, cur = 0, 0
for i in range(N):
    if init_str[i] == tgt_str[i]:
        if cur > 0:
            ans += 1
            cur = 0
    else:
        if cur < 4:
            cur += 1
        else:
            ans += 1
            cur = 1

# 반복문 이후에 cur이 0보다 클 때 ans를 1 증가
if cur > 0:
    ans += 1

print(ans)