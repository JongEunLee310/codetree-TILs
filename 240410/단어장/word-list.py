from sortedcontainers import SortedDict

n = int(input())
s = SortedDict()
for _ in range(n):
    word = input()
    try:
        s[word] += 1
    except:
        s[word] = 1

for key, item in s.items():
    print(key, item)