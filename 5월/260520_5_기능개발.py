import math

def solution(progresses, speeds):
    answer = []

    progressList = []
    for i in range(len(progresses)):
        n = (100-progresses[i]) / speeds[i]
        progressList.append(math.ceil(n))

    start = progressList.pop(0)
    stack = []
    stack.append(start)

    while progressList:
        n = progressList.pop(0)
        if max(stack) >= n:
            stack.append(n)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(n)

    answer.append(len(stack))
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))