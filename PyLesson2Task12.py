# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого 
# Петя # делает две подсказки. Он называет сумму этих чисел S и
# их произведение P. Помогите Кате отгадать задуманные Петей числа.
import random
def intNumEnter(msg=''):
    num_str = '0'
    num = 0
    run_again = True
    while run_again:
        num_str = input(msg)
        if num_str.isdigit(): 
            num = int(num_str)
            run_again = False if num > 0 else True
    return num
# random.seed(a=None, version=2)
num_mul = intNumEnter('Please enter multuply of two numbers: ')
num_sum = intNumEnter('Please enter sum of two numbers: ')
i, j, res = 0, 0, 0
NotFound = True
while i <= num_mul and NotFound:
    j = 1
    i += 1
    while j <= num_sum and NotFound:
        j += 1
        if (i * j == num_mul) and (i + j == num_sum):
            NotFound = False
            # print('i = ', i, '  j = ', j) # debug print
if NotFound:
    print('Source numbers combination for multuplication: ', num_mul,', and sum: ', num_sum,' -  not found.')
else:
    print('Source numbers combination for multuplication: ', num_mul,', and sum: ', num_sum,' -  found!')
    print('Tsese numbers are^ i = ', i, '  j = ', j,'.')

