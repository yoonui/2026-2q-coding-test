def dfs(begin, target, wordList, count, visited):
    global answer

    if begin == target:
        answer = min(answer, count)
    else:
        for i in range(len(wordList)):
            if visited[i] == False and sum(x!=y for x, y in zip(begin, wordList[i])) == 1:
                visited[i] = True
                dfs(wordList[i], target, wordList, count+1, visited)
                visited[i] = False

def solution(begin, target, words):
    global answer
    answer = 51

    if target not in words:
        return 0
    
    visited = [False] * len(words)
    dfs(begin, target, words, 0, visited)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))