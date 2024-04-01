n = int(input())
dict = {}
for i in range(n):
    s = input()
    try:
        dict[s] += 1
    except:
        dict[s] = 1

sorted_dict = sorted(dict.items(), key = lambda x : x[1])
print(sorted_dict[-1][1])