# 로또의 최고 순위와 최저 순위(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    zero_count = 0
    match_count = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            match_count += 1
        elif lottos[i] == 0:
            zero_count += 1
    
    best_rank = 7-(match_count+zero_count) if match_count+zero_count > 0 else 6
    worst_rank = 7-match_count if match_count > 0 else 6
    
    return [best_rank, worst_rank]