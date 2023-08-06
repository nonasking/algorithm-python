# 기본 정렬 메서드
a = [4, 3, 1, 2, 5]

# 정렬된 새 배열 생성
sorted_a = a.sorted() # 1 2 3 4 5
reverse_sorted_a = a.sorted(reverse=True) # 5 4 3 2 1

# 원본 배열 정렬(변경)
a.sorted() # 1 2 3 4 5
a.sorted(reverse=True) # 5 4 3 2 1

# swap
array = ['a', 'b']
array[0], array[1] = array[1], array[0]
print(array) # ['b', 'a']