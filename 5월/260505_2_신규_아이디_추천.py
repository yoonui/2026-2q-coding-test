import re

def solution(new_id):
    # 1단계: 대문자 > 소문자
    new_id = new_id.lower()

    # 2단계: 특수기호 제거
    new_id = re.sub(r"[~!@#$%^&*()=+\[\]{}:?,<>/]", "", new_id)

    # 3단계: 마침표 제거
    new_id = re.sub(r"\.+", ".", new_id)

    # 4단계: 처음이나 끝의 마침표 제거
    if len(new_id) > 0 and new_id[0] == ".": new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".": new_id = new_id[:-1]

    # 5단계: 빈 문자열 시 a 대입
    if len(new_id) == 0: new_id ="a"

    # 6단계: 16자 이상 시, 15자까지 자르기
    # 마침표가 끝에 있으면 제거
    if len(new_id) >= 16: new_id = new_id[:15]
    if len(new_id) > 0 and new_id[-1] == ".": new_id = new_id[:-1]

    # 7단계: 2자 이하 시, 마지막 문자를 길이 3까지 반복
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))