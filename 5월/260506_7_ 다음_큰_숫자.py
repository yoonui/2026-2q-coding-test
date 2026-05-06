def solution(n):
    answer = 0

    nBin = bin(n).count("1")
    tmp = n + 1

    while True:
        tBin = bin(tmp).count("1")
        if nBin == tBin:
            answer = tmp
            break
        tmp += 1
    
    return answer

print(solution(78))
print(solution(15))