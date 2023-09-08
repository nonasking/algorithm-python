# 유전법칙 (PCCP 모의고사 1회 - 3번)
# https://school.programmers.co.kr/learn/courses/15008/lessons/121685


def get_next_node(before, node):
    if before == 'RR':
        return 'RR'
    elif before == 'rr':
        return 'rr'
    else:
        if node[1] % 4 == 0:
            return 'RR'
        elif node[1] % 4 == 3:
            return 'rr'
        else:
            return 'Rr'

def get_nodes(last_node):
    if last_node[0]==1 and last_node[1] == 1:
        return [[0,0]]
    n, p = last_node[0]-1, last_node[1]-1
    result = [[n,p]]
    while n != 0 or p != 0:
        n -= 1
        p //= 4
        result.append([n,p])
    return result    
        
def solution(queries):
    
    answer = []
    for query in queries:
        nodes = get_nodes(query)[::-1]
        before = 'Rr'
        if len(nodes) == 1:
            answer.append(before)
        else:
            node = nodes[1]
            for i in range(1, len(nodes)):
                node = nodes[i]
                before = get_next_node(before, node)
            answer.append(before)

    return answer