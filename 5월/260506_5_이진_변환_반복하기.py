def solution(s):
    count = 0
    whileCount = 0

    while len(s) > 1:
        count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        whileCount += 1

    return [whileCount, count]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))