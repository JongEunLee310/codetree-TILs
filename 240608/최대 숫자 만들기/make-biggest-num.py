from functools import cmp_to_key

# 리스트 정렬에 사용할 키를 위한 커스텀 비교 함수
# x는 리스트 순서에서 앞에 있는 숫자, y는 뒤에 있는 숫자를 의미
# 반환값
    # -1 : 앞의 숫자가 뒤의 숫자보다 앞에 있어야 하는 경우
    # 1 : 뒤의 숫자가 앞의 숫자보다 앞에 있어야 하는 경우
    # 0 : 두 수가 같은 경우
def compare(x, y):
    # 두 수가 같으면 0을 반환하기 위해 0으로 초기화
    # 아래 반복문에서 sig가 바뀌면 두 숫자가 다르다는 것을 의미
    sig = 0

    # 2번의 반복문을 수행
        # 길이가 짧은 숫자의 길이만큼만 자릿수르 비교하면 두수가 같다는 오류를 발생시킬 수 있기 때문
        # 첫번째 반복문
            # x와 y 중 길이가 짧은 숫자의 길이만큼 반복하면서 비교를 수행
            # 길이가 짧은 숫자만큼 검사하는 중 두 수의 순서를 결정할 수 있으면 첫번째 반복문만으로 끝낸다.
        # 두번째 반복문
            # 첫번째 반복문에서 반복한 이후의 인덱스를 검사
            # x와 y 중 길이가 긴 숫자의 길이만큼 추가 반복하면서 비교를 수행
            # 단, 길이가 긴 숫자의 자릿수는 길이가 짧은 숫자의 맨앞 자릿수와 비교해야한다.
                # 두 수을 이어붙였을 때 앞에 위차한 숫자의 뒷부분이 뒤에 위차한 숫자의 맨 앞보다 커야하기 떄문
    
    # 첫번째 반복문
    # x, y 중 길이가 짧은 쪽의 길이만큼 수행
    # sig가 바뀌면 바로 반복문 종료
    x_i, y_i = 0, 0
    while (x_i < min(len(x), len(y)) and y_i < min(len(x), len(y))) and sig == 0:
        if x[x_i] > y[y_i]:
            sig = -1
        elif x[x_i] < y[y_i]:
            sig = 1

        x_i += 1
        y_i += 1

    # 두번째 반복문 - sig == 0일 때만 수행
    if sig == 0:
        # x가 더 긴 숫자일 때 x_i만 증가시키며 y의 맨 앞 자릿수와 비교
        if len(x) > len(y):
            while x_i < len(x) and sig == 0:
                if x[x_i] >= y[0]:
                    sig = -1
                elif x[x_i] < y[0]:
                    sig = 1
                x_i += 1

        # y가 더 긴 숫자일 때 y_i만 증가시키며 x의 맨 앞 자릿수와 비교        
        elif len(x) < len(y):
            while y_i < len(y) and sig == 0:
                if y[y_i] >= x[0]:
                    sig = 1
                elif y[y_i] < x[0]:
                    sig = -1
                y_i += 1

    return sig

n = int(input())
nums = [input() for _ in range(n)]

# String으로 받은 숫자를 사전순으로 내림차준 정렬한 후 이어 붙이는 방법을 사용
# 커스텀 비교 함수의 값을 키로 사용하여 내림차순 정렬
nums.sort(key=cmp_to_key(compare))

# 리스트에 있는 모든 수를 이어 붙여 출력
for num in nums:
    print(num, end="")