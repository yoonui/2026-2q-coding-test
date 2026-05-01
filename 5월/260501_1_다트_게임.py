def solution(dartResult):
    tmp = ""
    tmpList = []

    for i in dartResult:
        if i == "S":
            n = int(tmp)**1
            tmpList.append(n)
            tmp = ""
            continue
        elif i == "D":
            n = int(tmp)**2
            tmpList.append(n)
            tmp = ""
            continue
        elif i == "T":
            n = int(tmp)**3
            tmpList.append(n)
            tmp = ""
            continue

        if i == "*":
            if len(tmpList) > 1:
                n1 = tmpList.pop()
                n2 = tmpList.pop()
                n1 *= 2
                n2 *= 2
                tmpList.append(n2)
                tmpList.append(n1)
                continue
            else:
                n = tmpList.pop()
                n *= 2
                tmpList.append(n)
                continue
        elif i == "#":
            n = tmpList.pop()
            n *= (-1)
            tmpList.append(n)
            continue
        
        tmp += i

    return sum(tmpList)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))