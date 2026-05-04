def solution(X, Y):
    answer = ""

    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))

    if len(answer) == 0: return "-1"
    if len(answer) == answer.count("0"): return "0"
    return answer

print(solution("100", "2345")) # -1
print(solution("100", "203045")) # 0
print(solution("100", "123450")) # 10
print(solution("12321", "42531")) # 321
print(solution("5525", "1255")) # 552
