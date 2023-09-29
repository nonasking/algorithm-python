def convert_number(number):
    result = ''
    while number != 0:
        number, r = divmod(number, 3)
        result += str(r)
    return result
            
def solution(n):
    answer = convert_number(n)
    return int(answer,3)