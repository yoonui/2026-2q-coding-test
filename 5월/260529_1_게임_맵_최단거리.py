from collections import deque

def solution(maps):
    visited = []
    for i in maps:
        tmp = []
        for j in i:
            tmp.append(False)
        visited.append(tmp)

    endX = len(maps[0])
    endY = len(maps)

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    visited[0][0] = True
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < endX and 0 <= ny < endY:
                if visited[ny][nx] == False and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))

    answer = -1 if maps[endY-1][endX-1] == 1 else maps[endY-1][endX-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))