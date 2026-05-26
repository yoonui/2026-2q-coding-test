from functools import cmp_to_key

def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    else:
        return 1

def solution(numbers):
    tmpList = sorted(numbers, key=cmp_to_key(compare))

    answer = ''.join(map(str, tmpList))
    
    if answer[0] == '0':
        return '0'

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))