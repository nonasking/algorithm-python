# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def check_passed(words):
  for i in range(1,len(words)):
    if words[i][0] != words[i-1][-1] or words[i] in words[:i-1]:
      return i+1
  return 0

def solution(n, words):
    non_passed = check_passed(words)
    print(non_passed)
    if non_passed == 0:
      return [0,0]
    m,r = divmod(non_passed,n)
    if r == 0:
      r = n
    else:
      m += 1
    
    return [r, m]