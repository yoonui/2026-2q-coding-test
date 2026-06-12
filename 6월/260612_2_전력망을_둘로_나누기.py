def solution(n, wires):
    answer = n

    for wire in wires:
        nodeList = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for j in wires:
            if wire == j:
                continue
            x, y = j
            nodeList[x].append(y)
            nodeList[y].append(x)

        queue = [1]
        visited[1] = True
        count = 1
        while queue:
            first = queue.pop(0)
            for node in nodeList[first]:
                if visited[node] == False:
                    visited[node] = True
                    queue.append(node)
                    count += 1
        
        answer = min(answer, abs(count - (n-count)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))