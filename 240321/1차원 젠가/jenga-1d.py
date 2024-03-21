def rm_blk(zenga, s, e):
    new_zenga = []
    for i in range(len(zenga)):
        if i >= s - 1 and i <= e - 1:
            continue
        new_zenga.append(zenga[i])
    return new_zenga

n = int(input())
zenga = [int(input()) for _ in range(n)]
s1, e1 = [int(x) for x in input().split()]
s2, e2 = [int(x) for x in input().split()]


zenga = rm_blk(zenga, s1, e1)
zenga = rm_blk(zenga, s2, e2)

print(len(zenga))
for i in range(len(zenga)):
    print(zenga[i])