# 뒤에 있는 큰 수 찾기(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# def find_bigger(i, numbers):
#     if i == len(numbers):
#         return -1
#     for j in range(i+1, len(numbers)):
#         if numbers[j] > numbers[i]:
#             return numbers[j]
#     return -1

# def solution(numbers):
#     return [find_bigger(i, numbers) for i in range(len(numbers))]


# def solution(numbers):    
#     result = []    
    
#     for i, v in enumerate(numbers):
#         j = i + 1
#         while True:
#             if v >= max(numbers[i:]):
#                 result.append(-1)
#                 break
#             elif j == len(numbers):
#                 result.append(-1)
#                 break
#             elif numbers[j] > v:
#                 result.append(numbers[j])
#                 break
#             else:
#                 j += 1
                
#     return result