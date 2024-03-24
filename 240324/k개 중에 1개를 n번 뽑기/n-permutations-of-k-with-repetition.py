def get_pair(k, n, p):
    if n == 0:
        for i in range(len(p)):
            print(p[i], end=' ')
        print()
        return

    for i in range(1, k + 1):
        p.append(i)
        get_pair(k, n - 1, p)
        p.pop()


K, N = [int(x) for x in input().split()]
get_pair(K, N, [])