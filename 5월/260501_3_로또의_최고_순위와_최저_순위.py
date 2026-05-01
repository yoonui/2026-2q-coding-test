def calc_rank(count):
    return 6 if count < 2 else 7 - count

def solution(lottos, win_nums):
    answer = []

    set1 = set(lottos)
    set2 = set(win_nums)
    setResult = set1 & set2
    zeroCount = lottos.count(0)

    answer.append(calc_rank(len(setResult) + zeroCount))
    answer.append(calc_rank(len(setResult)))
    
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))