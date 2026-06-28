def solution(tickets):
    answer = []
    tickets = sorted(tickets, key=lambda x:x[1])
    visited = [False] * len(tickets)

    def bfs(first, visited, ansList):
        if len(ansList) == len(tickets)+1:
            answer.append(ansList)
            return
        for idx, ticket in enumerate(tickets):
            if ticket[0] == first and visited[idx] == False:
                visited[idx] = True
                ansList.append(ticket[1])
                bfs(ticket[1], visited[:], ansList[:])
                ansList.pop()
                visited[idx] = False
    
    bfs("ICN", visited[:], ["ICN"])

    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))