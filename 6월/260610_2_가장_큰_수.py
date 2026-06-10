from functools import cmp_to_key

def sortFuc(a, b):
    if a+b > b+a:
        return -1
    else: return 1

def solution(numbers):
    strList = list(map(str, numbers))
    strList = sorted(strList, key=cmp_to_key(sortFuc))

    answer = ''.join(strList)
    if answer[0] == '0': answer = '0'
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))