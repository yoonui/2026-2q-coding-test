from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for i in permutations(dungeons, len(dungeons)):
        tmp = k
        c = 0
        for j in i:
            if tmp >= j[0]:
                tmp -= j[1]
                c += 1
        answer = answer if answer >= c else c

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))