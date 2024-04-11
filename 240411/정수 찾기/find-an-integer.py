n = int(input())
s1 = set([int(x) for x in input().split()])
m = int(input())
nums = [int(x) for x in input().split()]

for num in nums:
    print(1 if num in s1 else 0)