def solution(n):
    fibo = [1, 1]

    if n == 1: return fibo[n]

    for i in range(2, n+1):
        tmp = fibo[i-1]+fibo[i-2]
        fibo.append(tmp)

    return fibo[n] % 1234567

print(solution(4))
print(solution(3))