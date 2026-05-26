def solution(d, budget):
    answer = 0
    d.sort()

    while budget > 0:
        if len(d) == 0: break
        first = d.pop(0)
        budget -= first
        if budget >= 0: answer += 1

    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))