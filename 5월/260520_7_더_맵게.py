import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while len(heap) > 1 and heap[0] < K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        tmp = first + (second * 2)
        heapq.heappush(heap, tmp)
        answer += 1

    if heap[0] >= K:
        return answer

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
