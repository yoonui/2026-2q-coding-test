def solution(n, edge):    
    nodeList = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in edge:
        x, y = i
        if y not in nodeList[x]:
            nodeList[x].append(y)
        if x not in nodeList[y]:
            nodeList[y].append(x)
    
    queue = [1]
    visited[1] = 1

    while queue:
        first = queue.pop(0)
        for i in nodeList[first]:
            if visited[i] == 0:
                visited[i] = visited[first] + 1
                queue.append(i)

    num = max(visited)
    return visited.count(num)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))