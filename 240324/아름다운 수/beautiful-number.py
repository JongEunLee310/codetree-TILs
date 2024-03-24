# 1 ~ 4까지 수를 사용한 모든 n자리 수 중 아름다운 수만 카운트한다. 
def get_beautiful_num(n, b):
    if n == 0:
        return 1 if is_beauty(b) else 0
    
    cnt = 0
    for i in range(1, 5):
        b.append(i)
        cnt += get_beautiful_num(n - 1, b)
        b.pop()
    
    return cnt

# 입력으로 들어온 수가 아름다운 수인지 판단
def is_beauty(b):
    result = True
    cur, cnt = b[0], 0
    for i in range(len(b)):
        if b[i] == cur:
            cnt += 1
        else:
            # 연속된 수의 개수가 해당 수의 배수이면 아름다운 수로 판별하고 그렇지 않으면 바로 거짓으로 판별
            if cnt % cur != 0:
                result = False
                break
            cur = b[i]
            cnt = 1

        # 현재 검사 중인 수의 위치를 고려했을 때 남아있는 자릿수로 아름다운 수를 만들 수 없으면 거짓으로 판별 
        if cnt % cur != 0 and (len(b) - 1 - i + (cnt % cur)) - cur < 0:
            result = False
            break

    return result

n = int(input())
print(get_beautiful_num(n, []))