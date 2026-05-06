def solution(s):
    tmpList = []
    tmp = s.split(" ")

    for i in tmp:
        tmpStr = i.lower()
        tmpStr = tmpStr[0].upper() + tmpStr[1:]  if len(tmpStr) > 0 else ""
        tmpList.append(tmpStr)

    return ' '.join(tmpList)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution(" "))