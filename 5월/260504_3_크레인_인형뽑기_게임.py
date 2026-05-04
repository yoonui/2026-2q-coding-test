def solution(board, moves):
    dollList = []
    stack = []
    answer = 0

    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            if board[j][i] == 0: continue
            tmp.append(board[j][i])
        dollList.append(tmp)

    for i in moves:
        if len(dollList[i-1]) == 0: continue
        doll = dollList[i-1].pop(0)
        stack.append(doll)

        if len(stack) >=2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))