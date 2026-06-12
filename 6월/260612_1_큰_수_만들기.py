def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and num > stack[-1]:
            stack.pop()
            k -= 1

        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))