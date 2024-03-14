br = input()

is_right = 'Yes'
stack = []
for b in br:
    if b == '(':
        stack.append(b)
    else:
        if len(stack) == 0 or stack[-1] != '(':
            is_right = 'No'
            break
        stack.pop()
    
if stack: is_right = 'No'
print(is_right)