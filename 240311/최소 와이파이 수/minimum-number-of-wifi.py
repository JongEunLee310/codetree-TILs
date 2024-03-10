n, m = [int(x) for x in input().split()]
residence = [int(x) for x in input().split()]
is_wifi = [False for _ in range(n)]

result = 0
cur_wifi_loc = 0
while cur_wifi_loc < n:
    s, e = cur_wifi_loc - m, cur_wifi_loc + m
    if s < 0 or residence[s] == 0 or is_wifi[s]:
        if e >= n:
            sig = False
            for i in range(s, n):
                if residence[i] == 1 and not is_wifi[i]:
                    result += 1
                    sig = True
                    break
            if sig: break
        cur_wifi_loc += 1
        continue

    for i in range(s, e + 1):
        if i < n:
            is_wifi[i] = True
    cur_wifi_loc = e
    result += 1

print(result)