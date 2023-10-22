# 뉴스 클러스터링(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17677


import math


def slice_string(str):
    str = str.lower()
    result = {}
    for i in range(len(str)-1):
        if str[i:i+2] in result:
            result[str[i:i+2]] += 1
        else:
            result[str[i:i+2]] = 1
    for s in list(result.keys()):
        if not s.isalpha():
            del result[s]
    return result

def get_common_and_union(dict1, dict2):
    common = {}
    union = {}
    for str,count in dict1.items():
        if str in dict2:
            common[str] = min(dict1[str], dict2[str])
            union[str] = max(dict1[str], dict2[str])
        else:
            union[str] = dict1[str]
            
    for str,count in dict2.items():
        if str not in dict1:
            union[str] = dict2[str]
    
    if sum(union.values()) == 0:
        return 65536
    return math.trunc((sum(common.values()) / sum(union.values())) * 65536)

def solution(str1, str2):
    
    dict1 = slice_string(str1)
    dict2 = slice_string(str2)
    
    result = get_common_and_union(dict1, dict2)
    
    return result