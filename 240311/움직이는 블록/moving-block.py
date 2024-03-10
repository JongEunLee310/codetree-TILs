N = int(input())
bricks = [int(input()) for _ in range(N)]

target_bricks = sum(bricks) // N
result = 0
for brick in bricks:
    result += abs(target_bricks - brick)

print(result // 2)