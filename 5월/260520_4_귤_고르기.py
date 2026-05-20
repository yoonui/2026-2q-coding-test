def solution(k, tangerine):
    fruitList = {}
    answer = 0

    for i in tangerine:
        if i in fruitList:
            fruitList[i] += 1
        else: fruitList[i] = 1
    
    fruitList2 = sorted(fruitList.items(), key=lambda x: x[1], reverse=True)

    for x, y in fruitList2:
        k -= y
        answer += 1
        if k <= 0:
            return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))