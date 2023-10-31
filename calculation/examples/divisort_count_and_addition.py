def get_divisors_count(number):
    result = 0
    for i in range(1, number+1):
        if number % i == 0:
            result += 1
    return result

def solution(left, right):
    result = 0
    
    for number in range(left, right+1):
        divisors_count = get_divisors_count(number)
        if divisors_count % 2 == 0:
            result += number
        else:
            result -= number
            
    return result