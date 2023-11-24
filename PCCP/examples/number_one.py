# 1번(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/250137


def solution(bandage, health, attacks):    
    maximum = health
    attack_map = {attack[0]: attack[1] for attack in attacks}
    first_attack = attacks[0][0]
    last_attack = attacks[-1][0]
    bonus = 0
      
    for sec in range(1, last_attack+1):
        if sec in attack_map:
            bonus = 0
            health -= attack_map[sec]
        else:
            bonus += 1
            health += bandage[1]
            if bonus == bandage[0]:
                health += bandage[2]
                bonus = 0
        if health > maximum:
            health = maximum
        if health <= 0:
            return -1
                
    return health