def solution(routes):
    routes.sort()
    answer = 1

    x, y = routes.pop(0)
    start = x
    end = y

    while routes:

        x, y = routes.pop(0)
        if x > end:
            answer += 1
            start = x
            end = y
        else:
            if x > start:
                start = x
            if y < end:
                end = y

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))