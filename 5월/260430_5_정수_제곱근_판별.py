def solution(n):
    tmp = n ** (1/2)
    
    if tmp % 1 != 0:
        return -1
    
    tmp += 1
    return int(tmp**2)

print(solution(121))
print(solution(3))