def solution(data, ext, val_ext, sort_by):
    dataList = []

    for i in data:
        tmp = {
            "code":i[0],
            "date":i[1],
            "maximum":i[2],
            "remain":i[3],
            }
        dataList.append(tmp)
    
    result = [x for x in dataList if x[ext] < val_ext]
    result = sorted(result, key=lambda x:x[sort_by])

    answer = [list(x.values()) for x in result]
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))