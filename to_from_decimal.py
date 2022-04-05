def to_decimal(number, system):
    number_list = list(number)
    p = 0
    for c in number_list:
        if c == 'A':
            number_list[number_list.index(c)] = '10'
        if c == 'B':
            number_list[number_list.index(c)] = '11'
        if c == 'C':
            number_list[number_list.index(c)] = '12'  
        if c == 'D':
            number_list[number_list.index(c)] = '13'
        if c == 'E':
            number_list[number_list.index(c)] = '14'
        if c == 'F':
            number_list[number_list.index(c)] = '15'
    for i in range(-1, -len(number_list) - 1, -1):
        number_list[i] = int(number_list[i]) * sys ** p
        p += 1
    return sum(number_list)

def from_decimal(number, divisor):
    result = []
    while number >= divisor:
        result.append(number % divisor)
        number = number // divisor
    result.append(number)
    for i in range(len(result)):
        result[i] = str(result[i])
        if result[i] == '10':
            result[i] = 'A'
        if result[i] == '11':
            result[i] = 'B'
        if result[i] == '12':
            result[i] = 'C'   
        if result[i] == '13':
            result[i] = 'D'
        if result[i] == '14':
            result[i] = 'E'  
        if result[i] == '15':
            result[i] = 'F'        
    return ''.join(result[::-1])
    
n = input('Введите целое число.')
sys = int(input('Какой системы число?'))
if sys == 10:
    divisor = int(input('В какую систему переводить?'))
    number_result = from_decimal(int(n), divisor)
else:
    number_result = to_decimal(n, sys)
print(number_result)