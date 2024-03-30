n = int(input())
dp = [0 for _ in range(n + 1)]

# 루트 노드에 있는 값을 중심으로 왼쪽와 오른쪽에 들어갈 노드로 만들 수 있는 BST의 개수를 곱한 후 더하면 서로 다른 BST의 개수를 알 수 있다.
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])