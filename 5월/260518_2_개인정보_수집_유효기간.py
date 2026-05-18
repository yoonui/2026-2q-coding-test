def solution(today, terms, privacies):
    answer = []

    today = today.split(".")
    today = [int(n) for n in today]

    termsList = {}
    for i in terms:
        x, y = i.split(" ")
        termsList[x] = int(y)

    for i in range(len(privacies)):
        date, t = privacies[i].split(" ")

        date = date.split(".")
        date = [int(n) for n in date]

        date[0] += (date[1] + termsList[t] - 1) // 12
        date[1] = (date[1] + termsList[t] - 1) % 12 + 1

        date[2] -= 1
        if date[2] == 0:
            date[1] -= 1
            date[2] = 28
            if date[1] == 0:
                date[1] = 12
                date[0] -= 1

        if today[0] > date[0]:
            answer.append(i+1)
        elif today[0] == date[0]:
            if today[1] > date[1]:
                answer.append(i+1)
            elif today[1] == date[1]:
                if today[2] > date[2]:
                    answer.append(i+1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))