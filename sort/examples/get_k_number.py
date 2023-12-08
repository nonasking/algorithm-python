# K번째수(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def get_k_number(array, i, j, k):
  sliced_array = sorted(array[i-1:j])
  return sliced_array[k-1]

def solution(array, commands):
    return [get_k_number(array, command[0],command[1],command[2]) for command in commands]