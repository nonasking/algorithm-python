# 스킬트리(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/49993


def remake_skills(skill, skill_tree):
    result = []
    
    for alphabet in skill_tree:
        if alphabet in skill and alphabet not in result:
            result.append(skill.index(alphabet))
            
    if len(result) == 0:
        return True
     
    return result == sorted(result) and len(result) == (max(result)+1) and result[0] == 0


def solution(skill, skill_trees):
    answer = 0
        
    for skill_tree in skill_trees:
        if remake_skills(skill, skill_tree):
            answer += 1
        
    return answer