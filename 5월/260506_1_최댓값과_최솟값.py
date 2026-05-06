def solution(s):
    answer = ''

    tmp = s.split(" ")
    tmp = [int(x) for x in tmp]
    
    answer = str(min(tmp)) + " " + str(max(tmp))
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))