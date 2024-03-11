x1, y1, x2, y2 = [int(x) for x in input().split()]
a1, b1, a2, b2 = [int(x) for x in input().split()]

width = max(x1, x2, a1, a2) - min(x1, x2, a1, a2)
length = max(y1, y2, b1, b2) - min(y1, y2, b1, b2)
result = width * length
print(result)