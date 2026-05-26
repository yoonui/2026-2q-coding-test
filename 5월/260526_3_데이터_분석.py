def solution(data, ext, val_ext, sort_by):
    answer = []
    dataType = {
        "code":0,
        "date":1,
        "maximum":2,
        "remain":3,
    }
    extNum = dataType[ext]
    sortNum = dataType[sort_by]

    for i in data:
        if i[extNum]<= val_ext:
            answer.append(i)

    answer = sorted(answer, key=lambda x:x[sortNum])
    return answer

# ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))