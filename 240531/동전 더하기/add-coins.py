n, k = [int(x) for x in input().split()]
coins = [int(input()) for _ in range(n)]

ans = 0
i = -1
# k가 0이 될 때까지 가장 큰 단위의 동전부터 가장 작은 동전까지 차례로 빼면서 사용하는 동전의 갯수를 센다.
while k > 0:
    # 현재 k가 현재 검사 중인 동전의 값보다 작으면 그 다음으로 큰 동전으로 바꾼다.
    if k < coins[i]:
        i -= 1
        continue
    
    # c는 현재 검사 중인 동전으로 최대한 k과 근접한 값을 만들기 위한 동전의 개수를 의미
    # c를 구하면 k에 현재 검사 중인 동전의 값을 c개를 사용한 만큼을 빼고 정답에는 c를 더한다.
    c = k // coins[i]
    k -= c * coins[i]
    ans += c

print(ans)