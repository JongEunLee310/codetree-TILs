n = int(input())

# 입력받은 문자열을 정렬하여 그 값을 키로 사용
d = {}
for _ in range(n):
    sorted_input = ''.join(sorted(input()))
    try:
        d[sorted_input] += 1
    except:
        d[sorted_input] = 1

# 키에 해당하는 값을 내림차순으로 정렬하여 가장 앞에 있는 값을 출력
sorted_list = sorted(d.items(), key = lambda x : x[1], reverse=True)
print(sorted_list[0][1])