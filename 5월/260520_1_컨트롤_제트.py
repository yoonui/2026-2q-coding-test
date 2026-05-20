def solution(s):
    numList = s.split(" ")
    stack = []

    for i in numList:
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)

print(solution("1 2 Z 3")) #4
print(solution("10 20 30 40")) #100
print(solution("10 Z 20 Z 1")) #1
print(solution("10 Z 20 Z")) #0
print(solution("-1 -2 -3 Z")) #-3