def get_win_cnt(rock, scissors, paper, num_match):
    num_dict = {rock:'r', scissors:'s', paper:'p'}
    cnt = 0
    for f, s in num_match:
        if is_win(num_dict[f], num_dict[s]):
            cnt += 1
    return cnt

def is_win(f, s):
    return f == 'r' and s == 's' or f == 's' and s == 'p' or f == 'p' and s == 'r'

N = int(input())
num_match = [[int(x) for x in input().split()] for i in range(N)]

# 숫자를 사용한 가위바위보 조합 -> 6가지
r1_s2_p3 = get_win_cnt(1, 2, 3, num_match)
r1_s3_p2 = get_win_cnt(1, 3, 2, num_match)
r2_s1_p3 = get_win_cnt(2, 1, 3, num_match)
r2_s3_p1 = get_win_cnt(2, 3, 1, num_match)
r3_s1_p2 = get_win_cnt(3, 1, 2, num_match)
r3_s2_p1 = get_win_cnt(3, 2, 1, num_match)

print(max(r1_s2_p3, r1_s3_p2, r2_s1_p3, r2_s3_p1, r3_s1_p2, r3_s2_p1))