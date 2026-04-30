def solution(num):
    n = num

    for i in range(501):
        if n == 1: return i
        if n % 2 == 0:
            n /= 2
        else: n = (n*3)+1
        
    return -1

print(solution(6))
print(solution(16))
print(solution(626331))