def solution(n, lost, reserve):
    borrowList = []
    answer = n

    tmpLost = list(set(lost) - set(reserve))
    tmpLost.sort()
    tmpReserve = list(set(reserve) - set(lost))
    tmpReserve.sort()

    for i in tmpLost:
        tmp1 = i-1
        if tmp1 not in borrowList and tmp1 in tmpReserve:
            borrowList.append(tmp1)
            continue
        tmp2 = i+1
        if tmp2 not in borrowList and tmp2 in tmpReserve:
            borrowList.append(tmp2)
            continue
        answer -= 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [2, 3, 4], [3]))