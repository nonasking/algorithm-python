# 신고 결과 받기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/92334#


def solution(id_list, report, k):
    id_report_map = {id: [] for id in id_list}
    id_announce_map = {id: 0 for id in id_list}
    
    for log in report:
        splitted = log.split()
        reporter, respondent = splitted[0], splitted[1]
        if reporter not in id_report_map[respondent]:
            id_report_map[respondent].append(reporter)
        
    for key, value in id_report_map.items():
        if len(value) >= k:
            for id in value:
                id_announce_map[id] += 1
    
    return list(id_announce_map.values())