def solution(survey, choices):

    character = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
        }
    
    for i in range(len(survey)):
        if choices[i] > 4:
            character[survey[i][1]] += choices[i] - 4
        else:
            character[survey[i][0]] += 4 - choices[i]
    
    answer = ''
    answer += "R" if character["R"] >= character["T"] else "T"
    answer += "C" if character["C"] >= character["F"] else "F"
    answer += "J" if character["J"] >= character["M"] else "M"
    answer += "A" if character["A"] >= character["N"] else "N"
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))