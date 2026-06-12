def solution(n, computers):
    answer = 0

    nodeList = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for i in computers:
        for j in range(len(i)):
            for k in range(j+1, len(i)):
                if i[j] == 1 and i[k] == 1:
                    nodeList[j+1].append(k+1)
                    nodeList[k+1].append(j+1)
    
    for i in range(1, n+1):
        if visited[i] == True:
            continue

        queue = [i]
        visited[i] = True

        while queue:
            first = queue.pop(0)
            for i in nodeList[first]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))