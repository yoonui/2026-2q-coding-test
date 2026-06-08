def dfs(numbers, target, sumNum):
    global answer
    if len(numbers) == 0:
        if sumNum == target:
            answer += 1
        return

    first = numbers.pop(0)
    dfs(numbers[:], target, sumNum+first)
    dfs(numbers[:], target, sumNum-first)

def solution(numbers, target):
    global answer
    answer = 0

    dfs(numbers[:], target, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))