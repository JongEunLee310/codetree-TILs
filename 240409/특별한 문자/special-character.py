string = input()

# 입력받은 문자열을 각 문자마다 개수를 센다.
d = {}
for c in string:
    try:
        d[c] += 1
    except:
        d[c] = 1

# 오름차순으로 정렬하여 가장 작은 개수의 문자가 1인 경우 값을 출력 아니면 None을 출력
sorted_list = sorted(d.items(), key = lambda x : [x[1]])
print(sorted_list[0][0] if sorted_list[0][1] == 1 else None)