def solution(n, lost, reserve):
    okList = []
    lostResult = list(set(lost)-set(reserve))
    reserveResult = list(set(reserve)-set(lost))
    n -= len(lostResult)

    for i in reserveResult:
        if i-1 in lostResult and i-1 not in okList:
            n += 1
            okList.append(i-1)
        elif i+1 in lostResult and i+1 not in okList:
            n += 1
            okList.append(i+1)

    return n

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [2,3], [1,2]))