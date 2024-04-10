from sortedcontainers import SortedDict

n = int(input())
s = SortedDict()
for _ in range(n):
    string = input()
    try:
        s[string] += 1
    except:
        s[string] = 1

for key, item in s.items():
    print("{0:} {1:.4f}".format(key, (item / n) * 100))