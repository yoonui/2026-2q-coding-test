def solution(priorities, location):
    answer = 0

    queue = []
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    while queue:
        startx, starty = queue.pop(0)
        if queue and starty < max(y for x, y in queue):
            queue.append((startx, starty))
        else:
            answer += 1
            if startx == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))