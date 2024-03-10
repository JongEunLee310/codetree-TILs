from sys import maxsize

def get_max_dist(line, N):
    max_dist = 0
    max_loc = []
    s, e = 0, 1

    while e < N:
        if line[s] == '0':
            s, e = e, e + 1
            continue
        
        if line[e] == '1':
            dist = e - s
            if max_dist <= dist:
                if max_dist < dist:
                    max_loc.clear()
                max_dist = dist
                max_loc.append([s, e])
            s, e = e, e + 1
        else:
            e += 1

    return max_dist, max_loc

def get_min_dist(line, N):
    min_dist = maxsize
    s, e = 0, 1

    while e < N:
        if line[s] == '0':
            s, e = e, e + 1
            continue
        
        if line[e] == '1':
            dist = e - s
            if min_dist > dist:
                min_dist = dist
            s, e = e, e + 1
        else:
            e += 1

    return min_dist

N = int(input())
line = list(input())

max_dist, max_loc = get_max_dist(line, N)

result = 0
if len(max_loc) == 0:
    idx_1 = line.index('1')
    result = max(idx_1, N - idx_1 - 1)
else:
    max_dist_center_idx = (max_loc[0][1] + max_loc[0][0]) // 2
    line[max_dist_center_idx] = '1'
    result = get_min_dist(line, N)
    line[max_dist_center_idx] = '0'

    if line[0] == '0':
        line[0] = '1'
        result = max(result, get_min_dist(line, N))
        line[0] = '0'
    
    if line[-1] == '0':
        line[-1] = '1'
        result = max(result, get_min_dist(line, N))
        line[-1] = '0'

print(result)