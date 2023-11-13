# 프로세스(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42587#


from collections import deque


def solution(priorities, location):
    indices = [i for i in range(len(priorities))]
    result = []
    queue = deque(priorities)
    index_queue = deque(indices)
    while location not in result:
        pending = queue.popleft()
        pending_index = index_queue.popleft()
        if len(queue) == 0 or pending >= max(queue):
            result.append(pending_index)
        else:
            queue.append(pending)
            index_queue.append(pending_index)
    
    return len(result)