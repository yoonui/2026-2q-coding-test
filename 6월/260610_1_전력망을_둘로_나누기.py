from collections import deque

def solution(n, wires):
    answer = n

    for i in wires:
        nodeList = [[] for i in range(n+1)]
        visited = [False] * (n+1)

        for a, b in wires:
            if [a, b] == i:
                continue
            nodeList[a].append(b)
            nodeList[b].append(a)

        visited[1] = True
        queue = deque([1])
        count = 1

        while queue:
            first = queue.popleft()

            for i in nodeList[first]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    count += 1

        answer = min(answer, abs(count - (n-count)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))