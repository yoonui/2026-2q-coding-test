def solution(maps):
    lenY = len(maps)
    lenX = len(maps[0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = [(0, 0)]
    while queue:
        sX, sY = queue.pop(0)

        for i in range(len(dx)):
            tX = sX + dx[i]
            tY = sY + dy[i]

            if 0 <= tX < lenX and 0 <= tY < lenY and maps[tY][tX] == 1:
                maps[tY][tX] = maps[sY][sX] + 1
                queue.append((tX, tY))

    answer = -1 if maps[lenY-1][lenX-1] == 1 else maps[lenY-1][lenX-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))