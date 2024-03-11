x1, y1, x2, y2 = [int(x) for x in input().split()]
a1, b1, a2, b2 = [int(x) for x in input().split()]

width1 = max(max(x1, x2, a1, a2) - min(x1, x2, a1, a2), max(y1, y2, b1, b2) - min(y1, y2, b1, b2))
result = width1 ** 2
print(result)