from collections import deque


def solution(people, limit):
    people.sort()
    answer = 0
    for i in range(len(people)):
      if people[i] >= limit:
        answer += (len(people)-i)
        people = people[:i]
        break

    people = deque(people)
    while len(people) > 0:
      if len(people) == 1:
        answer += 1
        break
      if (people[0] + people[-1]) > limit:
        answer += 1
        people.pop()
      else:
        answer += 1  
        people.popleft()
        people.pop()
    return answer