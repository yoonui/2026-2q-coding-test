def solution(s):
    pNum = s.count("p") + s.count("P")
    yNum = s.count("y") + s.count("Y")
    
    return pNum == yNum

print(solution("pPoooyY"))
print(solution("Pyy"))