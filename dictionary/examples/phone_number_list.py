# 전화번호 목록(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
        
    d = {}
    for phone_number in phone_book:
        if phone_number[0] in d:
            d[phone_number[0]].append(phone_number)
        else:
            d[phone_number[0]] = [phone_number]
    
    for v in d.values():
        v.sort()
        for j in range(len(v)-1):
            for k in range(j+1,len(v)):
                if j<k:
                    if v[k].startswith(v[j]):
                        return False
                    else:
                        break

    return True