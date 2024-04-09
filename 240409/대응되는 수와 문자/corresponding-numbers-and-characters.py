n, m = [int(x) for x in input().split()]
d = {}
for i in range(1, n + 1):
    c = input()
    d[c] = i
    d[i] = c

for _ in range(m):
    req = input()
    print(d[int(req)] if req.isnumeric() else d[req])