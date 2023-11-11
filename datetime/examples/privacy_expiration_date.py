# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370#


from datetime import datetime


def add_months_to_date(date, months):
    splitted = date.split('.')
    year = int(splitted[0])
    month = int(splitted[1])
    day = splitted[2]
    y, m = divmod(int(months) + month, 12)
    year += y
    month = m
    if month == 0:
        month = '12'
        year -= 1
    if len(str(month)) < 2:
        month = '0' + str(month)
    return '.'.join([str(year), str(month), day])

def solution(today, terms, privacies):
    terms_map = {term.split()[0]: term.split()[1] for term in terms}
    result = []
    for i in range(len(privacies)):
        splitted = privacies[i].split()
        date, type = splitted[0], splitted[1]
        expiration_date = add_months_to_date(date, terms_map[type])
        if datetime.strptime(today, '%Y.%m.%d') >= datetime.strptime(expiration_date, '%Y.%m.%d'):
            result.append(i+1)
    return result