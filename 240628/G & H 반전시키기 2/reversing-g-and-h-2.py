n = int(input())
init_str = list(input())
tgt_str = input()

# 그리디 알고리즘을 적용하여 뒤에서부터 문자열을 검사하며 특정 인덱스에 있는 두 문자열의 문자가 다를 때 무조건 반전 
    # 현재 검사 중인 인덱스에서 입력된 문자열의 문자가 목표 문자열의 문자와 같을 때는 continue
    # 현재 검사 중인 인덱스에서 입력된 문자열의 문자가 목표 문자열의 문자와 다를 때 반전 횟수 1 증가 및 이전 인덱스의 문자열을 모두 반전
ans = 0
ascii_G = ord('G')
for i in range(n - 1, -1, -1):
    # i 인덱스에서 두 문자열의 문자가 같을 때
    if init_str[i] == tgt_str[i]:
        continue
    
    # i 인덱스에서 두 문자열의 문자가 다를 때
    # 반복문을 사용해서 i 인덱스부터 이전 init_str의 문자를 반전시킨다.
    for j in range(i, -1, -1):
        init_str[j] = chr(ord(init_str[j]) % 2 + ascii_G)   # G와 H 중 하나로 변환시키기 위해 G나 H의 아스키 코드를 2로 나눈 나머지를 구해 G의 아스키 코드를 더하면 G나 H가 되는 원리로 G와 H로 반전이 가능

    # 반전 횟수 1 증가
    ans += 1

print(ans)