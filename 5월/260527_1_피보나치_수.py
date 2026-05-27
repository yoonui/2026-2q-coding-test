def solution(n):
    pibo = [0, 1]

    for i in range(2, n+1):
        tmp = pibo[i-2] + pibo[i-1]
        pibo.append(tmp)

    return pibo[n] % 1234567

print(solution(3))
print(solution(5))