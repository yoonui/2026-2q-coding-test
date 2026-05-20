def solution(score):
    average = []
    tmp = []

    for i in score:
        english, math = i
        average.append((english+math)/2)
        tmp.append((english+math)/2)
    
    average.sort(reverse=True)
    answer = []

    for i in tmp:
        c = average.index(i) + 1
        answer.append(c)

    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))