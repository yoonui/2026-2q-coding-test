def solution(participant, completion):
    pepoleList = {}

    for i in participant:
        if i in pepoleList:
            pepoleList[i] += 1
        else:
            pepoleList[i] = 1


    for i in completion:
        pepoleList[i] -= 1
        
    for i in pepoleList:
        if pepoleList[i] > 0:
            return i

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))