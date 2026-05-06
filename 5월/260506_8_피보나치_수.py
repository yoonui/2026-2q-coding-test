def solution(n):
    numList = [0, 1]

    for i in range(2, n+1):
        numList.append(numList[i-1] + numList[i-2])

    return numList[n] % 1234567

print(solution(3))
print(solution(5))