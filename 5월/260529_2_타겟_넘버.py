def dfs(sumNum, numList, target, result):
    global answer
    if len(numList) == 0 and sumNum == target:
        answer += 1
    else:
        if len(numList) == 0: return

        first = numList.pop(0)
        result += 1

        dfs(sumNum-first, numList[:], target, result)
        dfs(sumNum+first, numList[:], target, result)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(0, numbers, target, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))