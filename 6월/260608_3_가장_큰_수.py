def solution(numbers):
    answer = ''

    numList = list(map(str, numbers))
    numList = sorted(numList, key=lambda x : x *3,  reverse=True)

    answer = ''.join(numList)
    
    if answer[0] == '0':
        return '0'
    
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))