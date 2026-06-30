def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[-1] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if x1 < j < x2 and y1 < i < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = []
    queue.append([characterX*2, characterY*2])
    visited = [[1] * 102 for _ in range(102)]
    visited[characterY*2][characterX*2] = 0

    while queue:
        x, y = queue.pop(0)
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[y][x] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if field[ny][nx] == 1 and visited[ny][nx] == 1:
                queue.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1

    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))