def all_same_check(A):
    cnt = 0
    for i in range(len(A)):
        if A[i] == A[0]: cnt += 1
    return True if cnt == len(A) else False

A = list(input())

if not all_same_check(A):
    while A[0] == A[-1]:
        tmp = A[-1]
        for i in range(len(A) - 1, 0, -1):
            A[i] = A[i - 1]
        A[0] = tmp

new_A = ''
cur = A[0]
cnt = 0
for i in range(len(A)):
    if A[i] == cur:
        cnt += 1
    else:
        new_A += cur + str(cnt)
        cnt = 1
        cur = A[i]
if len(new_A) == 0 or len(new_A) >= 2 and cur != new_A[-2]:
    new_A += cur + str(cnt)

print(len(new_A))