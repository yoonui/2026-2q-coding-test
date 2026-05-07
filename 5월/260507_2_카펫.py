def solution(brown, yellow):

    s = brown + yellow
    x = 0
    y = 0

    for i in range(1, s+1):
        if s % i == 0:
            tmp = s // i

            if (i-2)*(tmp-2) == yellow:
                    x = i
                    y = tmp

    answer = [x, y]
    answer.sort(reverse=True)
    return answer

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]
print(solution(26, 10)) # [12, 3]