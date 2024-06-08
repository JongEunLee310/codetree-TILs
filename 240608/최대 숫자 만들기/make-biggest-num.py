from functools import cmp_to_key

# 리스트 정렬에 사용할 키를 위한 커스텀 비교 함수
# x는 리스트 순서에서 앞에 있는 숫자, y는 뒤에 있는 숫자를 의미
def compare(x, y):
    # 두 수가 같으면 0을 반환하기 위해 0으로 초기화
    # 아래 반복문에서 sig가 바뀌면 두 숫자가 다르다는 것을 의미
    sig = 0

    # x와 y 중 길이가 긴 숫자의 길이만큼 반복하면서 비교를 수행
    # 길이가 짧은 숫자의 길이만큼 자릿수가 같다가 이어지는 숫자의 크기에 따라 두 수의 자리를 바꾸는 여부를 결정할 수 있기 때문
    # 길이가 짧은 숫자의 인덱스는 해당 숫자의 길이를 넘어서지 않을만큼만 증가
        # 길이가 짧은 숫자의 인덱스를 넘어 검사방법
            # 길이가 긴 숫자의 인덱스는 계속 증가하며 길이가 짧은 숫자의 마지막 숫자와 계속 비교
    # sig가 0이 아닌 다른 수로 바뀌면 어느 숫자가 더 큰지 결정되므로 반복문 중단
    x_i, y_i = 0, 0
    while (x_i < max(len(x), len(y)) or y_i < max(len(x), len(y))) and sig == 0:
        if x[x_i] > y[y_i]:
            sig = -1
        elif x[x_i] < y[y_i]:
            sig = 1

        # 다음 x의 인덱스가 x의 길이보다 작을 때 x의 인덱스 1 추가
        if x_i + 1 < len(x):
            x_i += 1
        # 다음 y의 인덱스가 x의 길이보다 작을 때 y의 인덱스 1 추가
        if y_i + 1 < len(y):
            y_i += 1

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