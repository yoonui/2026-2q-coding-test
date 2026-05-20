def solution(survey, choices):
    testList = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0
    }

    for i in range(len(survey)):
        if choices[i] == 4:
            continue

        s = survey[i]

        if choices[i] < 4:
            num = 4 - choices[i]
            testList[s[0]] += num
            
        if choices[i] > 4:
            num = choices[i] - 4
            testList[s[1]] += num

    answer = ''

    if testList["R"] != testList["T"]: answer += "R" if testList["R"] > testList["T"] else "T"
    else: answer += "R"

    if testList["C"] != testList["F"]: answer += "C" if testList["C"] > testList["F"] else "F"
    else: answer += "C"

    if testList["J"] != testList["M"]: answer += "J" if testList["J"] > testList["M"] else "M"
    else: answer += "J"

    if testList["A"] != testList["N"]: answer += "A" if testList["A"] > testList["N"] else "N"
    else: answer += "A"

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))