def solution(begin, target, words):
    global answer
    answer = 0
    visited = [False] * len(words)

    def bfs(first, visited, c):
        global answer
        
        for idx, word in enumerate(words):
            if sum(x != y for x, y in zip(first, word)) == 1:
                if word == target:
                    answer = c+1
                    return
                if visited[idx] == False:
                    visited[idx] = True
                    bfs(word, visited[:], c+1)
                    visited[idx] = False

    if target not in words:
        return 0
    
    bfs(begin, visited[:], 0)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))