from functools import cmp_to_key

# 리스트 정렬에 사용할 키를 위한 커스텀 비교 함수
# x는 리스트 순서에서 앞에 있는 숫자, y는 뒤에 있는 숫자를 의미
def compare(x, y):
    # 두 수가 같으면 0을 반환하기 위해 0으로 초기화
    # 아래 반복문에서 sig가 바뀌면 두 숫자가 다르다는 것을 의미
    sig = 0

    # x와 y 중 길이가 짧은 수만큼 반복하면서 비교를 수행
    # 검사한 자릿수의 숫자가 같다면 더 짧은 길이의 수가 앞에 오는 것이 더 큰 수를 만들 수 있기 때문
    for i in range(min(len(x), len(y))):
        # 앞의 숫자가 뒤의 숫자보다 큰 경우 이미 내림차순이므로 -1을 반환
        if x[i] > y[i]:
            sig = -1
            break
        # 앞의 숫자가 뒤의 숫자보다 작은 경우 순서를 바꿔야하므로 1을 반환
        elif y[i] > x[i]:
            sig = 1
            break
    
    # 반복문 수행 이후에 sig가 0일 때는 두 수의 길이가 다른 경우 길이가 짧은 숫자만큼 검사했을 때 같다고 판단 될 수 있음
    # 이 경우 길이가 긴 쪽이 뒤로 가도록 해야함
    if sig == 0:
        # 앞에 있는 숫자의 길이가 길 때 순서를 바꿔야하므로 sig = 1
        if len(x) > len(y):
            sig = 1
        # 뒤에 있는 숫자의 길 경우는 이미 내림차순으로 정렬되어 있는 것이므로 sig = -1
        elif len(x) < len(y):
            sig = -1

    return sig


n = int(input())
nums = [input() for _ in range(n)]

# String으로 받은 숫자를 사전순으로 내림차준 정렬한 후 이어 붙이는 방법을 사용
# 커스텀 비교 함수의 값을 키로 사용하여 내림차순 정렬
nums.sort(key=cmp_to_key(compare))

# 리스트에 있는 모든 수를 이어 붙여 출력
ans = ''
for num in nums:
    ans += num
print(ans)