# 말의 이동 거리가 윷놀이판의 길이보다 긴 경우 점수를 얻는 방식을 사용하는 모든 경우의 수 중 최대 점수를 구하는 함수
def get_maximum_point(n, m, k, dists, p):
    # 턴이 종료되었을 때 포인트를 얻은 말의 수 반환
    if n == len(dists):
        point = 0
        for i in range(k):
            if p[i] >= m:
                point += 1
        return point

    # 재귀적으로 움직일 말을 선택해서 움직인 후 최대 점수 구함
    max_point = 0
    for i in range(k):
        p[i] += dists[n]
        max_point = max(max_point, get_maximum_point(n + 1, m, k, dists, p))
        p[i] -= dists[n]

    return max_point

n, m, k = [int(x) for x in input().split()]
dists = [int(x) for x in input().split()]

print(get_maximum_point(0, m, k, dists, [1 for _ in range(k)]))