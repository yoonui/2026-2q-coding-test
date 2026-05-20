import heapq

def solution(n, works):
    answer = 0

    heap = []
    for i in works:
        heapq.heappush(heap, -i)

    for i in range(n):
        if heap:
            first = heapq.heappop(heap)
            first += 1
            if first == 0: continue
            heapq.heappush(heap, first)

    for i in heap:
        answer += i ** 2

    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1,1]))