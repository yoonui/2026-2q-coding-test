def solution(x):
    plusList = list(str(x))

    sumNum = 0
    for i in plusList:
        sumNum += int(i)

    if x % sumNum == 0: 
        return True
    return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))